from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Protocol
from uuid import UUID

from redis.exceptions import ResponseError

from ai_platform_contracts import ResourceClass


class RedisStreamClient(Protocol):
    async def xgroup_create(
        self,
        name: str,
        groupname: str,
        id: str,
        mkstream: bool,
    ) -> Any: ...

    async def xadd(self, name: str, fields: dict[str, str]) -> str | bytes: ...

    async def xreadgroup(
        self,
        groupname: str,
        consumername: str,
        streams: dict[str, str],
        count: int,
        block: int,
    ) -> Any: ...

    async def xack(self, name: str, groupname: str, *ids: str) -> int: ...

    async def xautoclaim(
        self,
        name: str,
        groupname: str,
        consumername: str,
        min_idle_time: int,
        start_id: str,
        count: int,
    ) -> Any: ...


@dataclass(frozen=True, slots=True)
class QueueMessage:
    entry_id: str
    job_id: UUID
    correlation_id: UUID
    resource_class: ResourceClass


@dataclass(frozen=True, slots=True)
class ReclaimResult:
    next_start_id: str
    messages: tuple[QueueMessage, ...]
    deleted_ids: tuple[str, ...]


class RedisStreamQueue:
    def __init__(
        self,
        client: RedisStreamClient,
        *,
        stream: str = "ai:jobs",
        group: str = "workers",
    ) -> None:
        self._client = client
        self.stream = stream
        self.group = group

    async def ensure_group(self) -> None:
        try:
            await self._client.xgroup_create(
                self.stream,
                self.group,
                id="0-0",
                mkstream=True,
            )
        except ResponseError as exc:
            if "BUSYGROUP" not in str(exc):
                raise

    async def enqueue(
        self,
        *,
        job_id: UUID,
        correlation_id: UUID,
        resource_class: ResourceClass,
    ) -> str:
        entry_id = await self._client.xadd(
            self.stream,
            {
                "job_id": str(job_id),
                "correlation_id": str(correlation_id),
                "resource_class": resource_class.value,
            },
        )
        return _as_text(entry_id)

    async def read_new(
        self,
        *,
        consumer: str,
        count: int = 10,
        block_ms: int = 5_000,
    ) -> tuple[QueueMessage, ...]:
        response = await self._client.xreadgroup(
            self.group,
            consumer,
            streams={self.stream: ">"},
            count=count,
            block=block_ms,
        )
        return _decode_read_response(response)

    async def ack(self, entry_id: str) -> int:
        return await self._client.xack(self.stream, self.group, entry_id)

    async def reclaim_stale(
        self,
        *,
        consumer: str,
        min_idle_ms: int = 120_000,
        start_id: str = "0-0",
        count: int = 100,
    ) -> ReclaimResult:
        next_start_id, claimed, deleted = await self._client.xautoclaim(
            self.stream,
            self.group,
            consumer,
            min_idle_time=min_idle_ms,
            start_id=start_id,
            count=count,
        )
        return ReclaimResult(
            next_start_id=_as_text(next_start_id),
            messages=tuple(_decode_entry(entry_id, fields) for entry_id, fields in claimed),
            deleted_ids=tuple(_as_text(entry_id) for entry_id in (deleted or [])),
        )


def _decode_read_response(response: Any) -> tuple[QueueMessage, ...]:
    messages: list[QueueMessage] = []
    for _stream_name, entries in response or []:
        for entry_id, fields in entries:
            messages.append(_decode_entry(entry_id, fields))
    return tuple(messages)


def _decode_entry(entry_id: Any, fields: dict[Any, Any]) -> QueueMessage:
    decoded = {_as_text(key): _as_text(value) for key, value in fields.items()}
    return QueueMessage(
        entry_id=_as_text(entry_id),
        job_id=UUID(decoded["job_id"]),
        correlation_id=UUID(decoded["correlation_id"]),
        resource_class=ResourceClass(decoded["resource_class"]),
    )


def _as_text(value: Any) -> str:
    if isinstance(value, bytes):
        return value.decode("utf-8")
    return str(value)
