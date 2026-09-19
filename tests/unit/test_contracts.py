from ai_platform_contracts import (
    ApprovalRequirement,
    GoalContract,
    JobEnvelope,
    ResourceClass,
    RiskLevel,
)


def test_job_envelope_defaults_are_safe_and_versioned() -> None:
    goal = GoalContract(
        goal="Build a verified feature",
        definition_of_done=("tests pass", "review passes"),
        risk_level=RiskLevel.MEDIUM,
        approval=ApprovalRequirement.USER,
    )

    job = JobEnvelope(
        producer="orchestrator",
        goal=goal,
        resource_class=ResourceClass.CPU_LIGHT,
    )

    assert job.schema_version == "1.0"
    assert job.max_attempts == 3
    assert job.timeout_seconds == 600
    assert job.goal.priority == 3
    assert job.message_id != job.correlation_id
