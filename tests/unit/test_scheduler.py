from ai_platform_contracts import ResourceClass
from ai_scheduler import AdmissionController, ResourceRequest, ResourceSnapshot


def snapshot(**overrides: object) -> ResourceSnapshot:
    values = {
        "cpu_percent": 20.0,
        "ram_used_mb": 8_000,
        "ram_total_mb": 32_000,
        "disk_free_percent": 50.0,
        "gpu_present": True,
        "vram_used_mb": 4_000,
        "vram_total_mb": 16_000,
        "active_gpu_heavy": 0,
    }
    values.update(overrides)
    return ResourceSnapshot(**values)


def test_control_critical_keeps_recovery_path_under_pressure() -> None:
    controller = AdmissionController()
    decision = controller.evaluate(
        ResourceRequest(ResourceClass.CONTROL_CRITICAL),
        snapshot(
            cpu_percent=100.0,
            ram_used_mb=31_000,
            disk_free_percent=2.0,
            vram_used_mb=15_900,
        ),
    )
    assert decision.admitted is True


def test_second_heavy_gpu_job_is_backpressured() -> None:
    controller = AdmissionController()
    decision = controller.evaluate(
        ResourceRequest(ResourceClass.GPU_HEAVY),
        snapshot(active_gpu_heavy=1),
    )
    assert decision.admitted is False
    assert "slot" in decision.reason


def test_media_render_obeys_vram_high_water() -> None:
    controller = AdmissionController()
    decision = controller.evaluate(
        ResourceRequest(ResourceClass.MEDIA_RENDER),
        snapshot(vram_used_mb=14_000, vram_total_mb=16_000),
    )
    assert decision.admitted is False
    assert "VRAM" in decision.reason


def test_heavy_work_stops_on_low_disk() -> None:
    controller = AdmissionController()
    decision = controller.evaluate(
        ResourceRequest(ResourceClass.CPU_HEAVY),
        snapshot(disk_free_percent=10.0),
    )
    assert decision.admitted is False
    assert "disk" in decision.reason
