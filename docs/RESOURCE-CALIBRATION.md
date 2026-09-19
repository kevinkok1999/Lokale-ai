# Adaptive Resource Calibration

The architecture does not depend on manually entered fixed resource limits.

The installer calibrates the actual machines and writes a versioned resource profile.

## Measurements

AI-Core:
- logical CPU count
- available RAM
- free/total disk
- current baseline service memory
- container health
- network reachability
- persistent-service restart behavior

RTX node:
- logical CPU count
- available RAM
- free/total disk
- GPU model
- total VRAM
- driver/runtime availability
- Ollama health
- representative inference memory/load
- media engine availability

## Default safety thresholds

Initial admission ceilings:
- RAM high-water: 80%
- RAM critical: 90%
- sustained CPU high-water: 85%
- VRAM high-water: 85%
- VRAM critical: 92%
- minimum free disk: 15%

These are safety defaults, not promises that every workload is safe up to the exact percentage.

Calibration may lower limits.

## Work classes

- control_critical
- cpu_light
- cpu_heavy
- gpu_light
- gpu_heavy
- media_render
- runner
- background_maintenance

Priority:
control-critical services always retain a reserved budget.

## RTX scheduling

Initial rule:
- one gpu_heavy/media_render workload at a time.

Concurrency can only be increased after measured benchmark evidence shows safe headroom.

## Backpressure

If resource admission fails:
- job remains queued;
- user-facing control remains responsive;
- no overcommit is attempted;
- reason is recorded;
- retry occurs after resources return.

## Disk protection

Below free-space threshold:
- block model downloads;
- block large builds;
- block final media renders;
- preserve health/repair/cleanup functions.

## Calibration lifecycle

Calibration runs:
- after initial install;
- after detected major hardware change;
- after explicit recalibration;
- after major runtime/model change when policy requires it.

Previous profile is retained for comparison.
