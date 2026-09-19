from __future__ import annotations

from dataclasses import dataclass

from ai_platform_contracts import ResourceClass


@dataclass(frozen=True, slots=True)
class SafetyThresholds:
    ram_high_water_percent: float = 80.0
    ram_critical_percent: float = 90.0
    cpu_high_water_percent: float = 85.0
    vram_high_water_percent: float = 85.0
    vram_critical_percent: float = 92.0
    disk_min_free_percent: float = 15.0
    max_parallel_gpu_heavy: int = 1


@dataclass(frozen=True, slots=True)
class ResourceSnapshot:
    cpu_percent: float
    ram_used_mb: int
    ram_total_mb: int
    disk_free_percent: float
    gpu_present: bool = False
    vram_used_mb: int = 0
    vram_total_mb: int = 0
    active_gpu_heavy: int = 0

    @property
    def ram_percent(self) -> float:
        if self.ram_total_mb <= 0:
            return 100.0
        return (self.ram_used_mb / self.ram_total_mb) * 100.0

    @property
    def vram_percent(self) -> float:
        if not self.gpu_present or self.vram_total_mb <= 0:
            return 0.0
        return (self.vram_used_mb / self.vram_total_mb) * 100.0


@dataclass(frozen=True, slots=True)
class ResourceRequest:
    resource_class: ResourceClass


@dataclass(frozen=True, slots=True)
class AdmissionDecision:
    admitted: bool
    reason: str


class AdmissionController:
    def __init__(self, thresholds: SafetyThresholds | None = None) -> None:
        self.thresholds = thresholds or SafetyThresholds()

    def evaluate(
        self,
        request: ResourceRequest,
        snapshot: ResourceSnapshot,
    ) -> AdmissionDecision:
        t = self.thresholds
        rc = request.resource_class

        # Health, repair and control traffic must retain a path even under pressure.
        if rc is ResourceClass.CONTROL_CRITICAL:
            return AdmissionDecision(True, "control-critical reserve")

        if snapshot.disk_free_percent < t.disk_min_free_percent:
            return AdmissionDecision(False, "disk protection active")

        if snapshot.ram_percent >= t.ram_critical_percent:
            return AdmissionDecision(False, "RAM critical threshold reached")

        if rc in {
            ResourceClass.CPU_HEAVY,
            ResourceClass.GPU_LIGHT,
            ResourceClass.GPU_HEAVY,
            ResourceClass.MEDIA_RENDER,
            ResourceClass.RUNNER,
            ResourceClass.BACKGROUND_MAINTENANCE,
        } and snapshot.ram_percent >= t.ram_high_water_percent:
            return AdmissionDecision(False, "RAM high-water backpressure")

        if rc in {
            ResourceClass.CPU_HEAVY,
            ResourceClass.BACKGROUND_MAINTENANCE,
        } and snapshot.cpu_percent >= t.cpu_high_water_percent:
            return AdmissionDecision(False, "CPU high-water backpressure")

        if rc in {ResourceClass.GPU_LIGHT, ResourceClass.GPU_HEAVY, ResourceClass.MEDIA_RENDER}:
            if not snapshot.gpu_present or snapshot.vram_total_mb <= 0:
                return AdmissionDecision(False, "GPU capability unavailable")

            if snapshot.vram_percent >= t.vram_critical_percent:
                return AdmissionDecision(False, "VRAM critical threshold reached")

        if rc in {ResourceClass.GPU_HEAVY, ResourceClass.MEDIA_RENDER}:
            if snapshot.active_gpu_heavy >= t.max_parallel_gpu_heavy:
                return AdmissionDecision(False, "heavy GPU slot occupied")
            if snapshot.vram_percent >= t.vram_high_water_percent:
                return AdmissionDecision(False, "VRAM high-water backpressure")

        return AdmissionDecision(True, "resource budget available")
