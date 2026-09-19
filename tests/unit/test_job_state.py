import pytest

from ai_platform_contracts import JobStatus
from app.job_state import InvalidJobTransition, can_transition, require_transition


def test_happy_path_requires_verification_stages() -> None:
    path = [
        JobStatus.QUEUED,
        JobStatus.LEASED,
        JobStatus.RUNNING,
        JobStatus.TESTING,
        JobStatus.REVIEWING,
        JobStatus.COMPLETED,
    ]

    for current, target in zip(path, path[1:]):
        assert can_transition(current, target)


def test_running_cannot_skip_directly_to_completed() -> None:
    assert can_transition(JobStatus.RUNNING, JobStatus.COMPLETED) is False

    with pytest.raises(InvalidJobTransition):
        require_transition(JobStatus.RUNNING, JobStatus.COMPLETED)


def test_terminal_states_are_terminal() -> None:
    for status in (JobStatus.COMPLETED, JobStatus.FAILED, JobStatus.CANCELLED):
        assert all(not can_transition(status, target) for target in JobStatus)
