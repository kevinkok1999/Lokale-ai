from ai_platform_contracts import GoalContract, JobEnvelope, ResourceClass
from app.repository import _payload_from_envelope


def test_repository_payload_preserves_contract_shape() -> None:
    envelope = JobEnvelope(
        producer="orchestrator",
        goal=GoalContract(goal="Render a verified scene"),
        resource_class=ResourceClass.GPU_HEAVY,
        required_capabilities={"gpu": "rtx"},
        payload={"scene_id": "scene-01"},
    )

    payload = _payload_from_envelope(envelope)

    assert payload["required_capabilities"] == {"gpu": "rtx"}
    assert payload["resource_class"] == "gpu_heavy"
    assert payload["payload"] == {"scene_id": "scene-01"}
