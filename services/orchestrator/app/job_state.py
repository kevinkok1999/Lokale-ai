from __future__ import annotations

from ai_platform_contracts import JobStatus


class InvalidJobTransition(ValueError):
    pass


_ALLOWED: dict[JobStatus, frozenset[JobStatus]] = {
    JobStatus.QUEUED: frozenset({JobStatus.BLOCKED, JobStatus.LEASED, JobStatus.CANCELLED}),
    JobStatus.BLOCKED: frozenset({JobStatus.QUEUED, JobStatus.CANCELLED}),
    JobStatus.LEASED: frozenset({JobStatus.RUNNING, JobStatus.RETRY_WAIT, JobStatus.CANCELLED}),
    JobStatus.RUNNING: frozenset(
        {JobStatus.TESTING, JobStatus.RETRY_WAIT, JobStatus.FAILED, JobStatus.CANCELLED}
    ),
    JobStatus.TESTING: frozenset(
        {JobStatus.REVIEWING, JobStatus.RETRY_WAIT, JobStatus.FAILED, JobStatus.CANCELLED}
    ),
    JobStatus.REVIEWING: frozenset(
        {
            JobStatus.WAITING_APPROVAL,
            JobStatus.COMPLETED,
            JobStatus.RETRY_WAIT,
            JobStatus.FAILED,
            JobStatus.CANCELLED,
        }
    ),
    JobStatus.WAITING_APPROVAL: frozenset(
        {JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED}
    ),
    JobStatus.RETRY_WAIT: frozenset({JobStatus.QUEUED, JobStatus.CANCELLED}),
    JobStatus.COMPLETED: frozenset(),
    JobStatus.FAILED: frozenset(),
    JobStatus.CANCELLED: frozenset(),
}


def can_transition(current: JobStatus, target: JobStatus) -> bool:
    return target in _ALLOWED[current]


def require_transition(current: JobStatus, target: JobStatus) -> None:
    if not can_transition(current, target):
        raise InvalidJobTransition(f"invalid job transition: {current.value} -> {target.value}")
