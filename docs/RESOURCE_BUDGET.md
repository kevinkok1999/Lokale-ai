# Resource budget and adaptive calibration

The stated hardware is a planning input, never a runtime fact. At install and boot the doctor records CPU cores, RAM, free disk, GPU/VRAM, driver, model residency, queue depth and service footprint.

Thresholds are calibrated per node:

- **safe baseline:** normal admission; reserve CONTROL ≥25% RAM and ≥20% disk, COMPUTE ≥20% VRAM and ≥25% RAM;
- **warning:** queue new heavy work and emit `resource.pressure`;
- **backpressure:** lower concurrency, unload idle models and prefer a validated smaller model;
- **hard:** admit only CONTROL-critical work;
- **emergency reserve:** stop optional work and preserve state/diagnostics.

These percentages are initial policy defaults, not claims about actual capacity.

## Concurrency defaults

Until live measurement proves a higher safe value:

- heavy GPU jobs: **1**;
- GitHub Actions runner-consuming jobs: **1**;
- Git writers per repository: **1**;
- local CPU parallelism: adaptive after measuring host pressure.

Read-only analysis and isolated lightweight checks may parallelize when they do not threaten reserves.

The scheduler never responds to pressure by spawning more workers. Queueing is preferred over overcommit.

## Cache/resource economy

Keep reusable dependency/build/model caches when disk budgets allow, but never preserve a cache at the expense of the emergency reserve. Unload idle heavyweight model/process resources before admitting another heavy job.
