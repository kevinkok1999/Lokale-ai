from uuid import UUID

import pytest
from redis.exceptions import ResponseError

from ai_platform_contracts import ResourceClass
from ai_scheduler.redis_queue import RedisStreamQueue


class FakeRedis:
    def __init__(self) -> None:
        self.group_error: Exception | None = None
        self.added: list[tuple[str, dict[str, str]]] = []
        self.read_response = []
        self.autoclaim_response = ("0-0", [], [])
        self.acked: list[tuple[str, str, tuple[str, ...]]] = []

    async def xgroup_create(self, name, groupname, id, mkstream):
        if self.group_error is not None:
            raise self.group_error
        return True

    async def xadd(self, name, fields):
        self.added.append((name, fields))
        return b"1700000000000-0"

    async def xreadgroup(self, groupname, consumername, streams, count, block):
        return self.read_response

    async def xack(self, name, groupname, *ids):
        self.acked.append((name, groupname, ids))
        return len(ids)

    async def xautoclaim(
        self,
        name,
        groupname,
        consumername,
        min_idle_time,
        start_id,
        count,
    ):
        return self.autoclaim_response


@pytest.mark.asyncio
async def test_group_creation_is_idempotent_for_busygroup() -> None:
    redis = FakeRedis()
    redis.group_error = ResponseError("BUSYGROUP Consumer Group name already exists")
    queue = RedisStreamQueue(redis)

    await queue.ensure_group()


@pytest.mark.asyncio
async def test_enqueue_contains_only_routing_metadata() -> None:
    redis = FakeRedis()
    queue = RedisStreamQueue(redis)
    job_id = UUID("00000000-0000-0000-0000-000000000001")
    correlation_id = UUID("00000000-0000-0000-0000-000000000002")

    entry_id = await queue.enqueue(
        job_id=job_id,
        correlation_id=correlation_id,
        resource_class=ResourceClass.GPU_HEAVY,
    )

    assert entry_id == "1700000000000-0"
    assert redis.added == [
        (
            "ai:jobs",
            {
                "job_id": str(job_id),
                "correlation_id": str(correlation_id),
                "resource_class": "gpu_heavy",
            },
        )
    ]


@pytest.mark.asyncio
async def test_read_new_decodes_bytes_and_resource_class() -> None:
    redis = FakeRedis()
    redis.read_response = [
        (
            b"ai:jobs",
            [
                (
                    b"1700000000000-0",
                    {
                        b"job_id": b"00000000-0000-0000-0000-000000000001",
                        b"correlation_id": b"00000000-0000-0000-0000-000000000002",
                        b"resource_class": b"cpu_light",
                    },
                )
            ],
        )
    ]
    queue = RedisStreamQueue(redis)

    messages = await queue.read_new(consumer="worker-a")

    assert len(messages) == 1
    assert messages[0].entry_id == "1700000000000-0"
    assert messages[0].resource_class is ResourceClass.CPU_LIGHT


@pytest.mark.asyncio
async def test_reclaim_returns_claimed_and_deleted_ids() -> None:
    redis = FakeRedis()
    redis.autoclaim_response = (
        b"0-0",
        [
            (
                b"1700000000000-0",
                {
                    b"job_id": b"00000000-0000-0000-0000-000000000001",
                    b"correlation_id": b"00000000-0000-0000-0000-000000000002",
                    b"resource_class": b"gpu_heavy",
                },
            )
        ],
        [b"1699999999999-0"],
    )
    queue = RedisStreamQueue(redis)

    result = await queue.reclaim_stale(consumer="worker-b")

    assert result.next_start_id == "0-0"
    assert result.messages[0].resource_class is ResourceClass.GPU_HEAVY
    assert result.deleted_ids == ("1699999999999-0",)
