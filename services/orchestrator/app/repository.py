from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Protocol
from uuid import UUID, uuid4

from psycopg.rows import dict_row
from psycopg_pool import AsyncConnectionPool

from ai_platform_contracts import JobEnvelope, JobStatus

from .job_state import require_transition


@dataclass(frozen=True, slots=True)
class JobRecord:
    id: UUID
    status: JobStatus
    job_type: str
    priority: int
    requested_by: str
    max_attempts: int
    attempt_count: int
    created_at: datetime
    updated_at: datetime


class ConcurrentJobUpdate(RuntimeError):
    pass


class JobRepository(Protocol):
    async def create(self, *, job_type: str, envelope: JobEnvelope) -> JobRecord: ...
    async def get(self, job_id: UUID) -> JobRecord | None: ...
    async def transition(
        self,
        *,
        job_id: UUID,
        expected: JobStatus,
        target: JobStatus,
    ) -> JobRecord: ...


class PostgresJobRepository:
    def __init__(self, pool: AsyncConnectionPool) -> None:
        self._pool = pool

    async def create(self, *, job_type: str, envelope: JobEnvelope) -> JobRecord:
        job_id = uuid4()
        query = """
            INSERT INTO ai_control.jobs (
                id,
                idempotency_key,
                job_type,
                status,
                priority,
                requested_by,
                required_capabilities,
                payload,
                max_attempts
            )
            VALUES (
                %(id)s,
                %(idempotency_key)s,
                %(job_type)s,
                'queued',
                %(priority)s,
                %(requested_by)s,
                %(required_capabilities)s::jsonb,
                %(payload)s::jsonb,
                %(max_attempts)s
            )
            RETURNING
                id, status, job_type, priority, requested_by,
                max_attempts, attempt_count, created_at, updated_at
        """
        params = {
            "id": job_id,
            "idempotency_key": str(envelope.message_id),
            "job_type": job_type,
            "priority": envelope.goal.priority,
            "requested_by": envelope.producer,
            "required_capabilities": envelope.model_dump_json(include={"required_capabilities"}),
            "payload": envelope.model_dump_json(include={"payload", "goal", "resource_class"}),
            "max_attempts": envelope.max_attempts,
        }
        async with self._pool.connection() as conn:
            async with conn.cursor(row_factory=dict_row) as cur:
                await cur.execute(query, params)
                row = await cur.fetchone()
            await conn.commit()
        assert row is not None
        return _record_from_row(row)

    async def get(self, job_id: UUID) -> JobRecord | None:
        query = """
            SELECT
                id, status, job_type, priority, requested_by,
                max_attempts, attempt_count, created_at, updated_at
            FROM ai_control.jobs
            WHERE id = %s
        """
        async with self._pool.connection() as conn:
            async with conn.cursor(row_factory=dict_row) as cur:
                await cur.execute(query, (job_id,))
                row = await cur.fetchone()
        return None if row is None else _record_from_row(row)

    async def transition(
        self,
        *,
        job_id: UUID,
        expected: JobStatus,
        target: JobStatus,
    ) -> JobRecord:
        require_transition(expected, target)
        query = """
            UPDATE ai_control.jobs
            SET status = %(target)s, updated_at = now()
            WHERE id = %(id)s AND status = %(expected)s
            RETURNING
                id, status, job_type, priority, requested_by,
                max_attempts, attempt_count, created_at, updated_at
        """
        async with self._pool.connection() as conn:
            async with conn.cursor(row_factory=dict_row) as cur:
                await cur.execute(
                    query,
                    {
                        "id": job_id,
                        "expected": expected.value,
                        "target": target.value,
                    },
                )
                row = await cur.fetchone()
            await conn.commit()

        if row is None:
            raise ConcurrentJobUpdate(
                f"job {job_id} was not in expected state {expected.value}"
            )
        return _record_from_row(row)


def _record_from_row(row: dict[str, object]) -> JobRecord:
    return JobRecord(
        id=row["id"],  # type: ignore[arg-type]
        status=JobStatus(str(row["status"])),
        job_type=str(row["job_type"]),
        priority=int(row["priority"]),
        requested_by=str(row["requested_by"]),
        max_attempts=int(row["max_attempts"]),
        attempt_count=int(row["attempt_count"]),
        created_at=row["created_at"],  # type: ignore[arg-type]
        updated_at=row["updated_at"],  # type: ignore[arg-type]
    )
