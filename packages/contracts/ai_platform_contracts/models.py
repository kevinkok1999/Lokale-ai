from __future__ import annotations

from datetime import datetime, timezone
from enum import StrEnum
from typing import Any
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


class RiskLevel(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class ApprovalRequirement(StrEnum):
    NONE = "none"
    USER = "user"
    PRODUCTION = "production"


class ResourceClass(StrEnum):
    CONTROL_CRITICAL = "control_critical"
    CPU_LIGHT = "cpu_light"
    CPU_HEAVY = "cpu_heavy"
    GPU_LIGHT = "gpu_light"
    GPU_HEAVY = "gpu_heavy"
    MEDIA_RENDER = "media_render"
    RUNNER = "runner"
    BACKGROUND_MAINTENANCE = "background_maintenance"


class JobStatus(StrEnum):
    QUEUED = "queued"
    BLOCKED = "blocked"
    LEASED = "leased"
    RUNNING = "running"
    TESTING = "testing"
    REVIEWING = "reviewing"
    WAITING_APPROVAL = "waiting_approval"
    RETRY_WAIT = "retry_wait"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class GoalContract(StrictModel):
    goal: str = Field(min_length=1, max_length=4000)
    constraints: tuple[str, ...] = ()
    definition_of_done: tuple[str, ...] = ()
    priority: int = Field(default=3, ge=1, le=5)
    risk_level: RiskLevel = RiskLevel.LOW
    approval: ApprovalRequirement = ApprovalRequirement.NONE


class JobEnvelope(StrictModel):
    schema_version: str = "1.0"
    message_id: UUID = Field(default_factory=uuid4)
    correlation_id: UUID = Field(default_factory=uuid4)
    producer: str = Field(min_length=1, max_length=128)
    created_at: datetime = Field(default_factory=utc_now)
    goal: GoalContract
    resource_class: ResourceClass = ResourceClass.CPU_LIGHT
    timeout_seconds: int = Field(default=600, ge=1, le=86_400)
    max_attempts: int = Field(default=3, ge=1, le=10)
    required_capabilities: dict[str, Any] = Field(default_factory=dict)
    payload: dict[str, Any] = Field(default_factory=dict)
