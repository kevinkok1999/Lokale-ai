# Resource budget and adaptive calibration

The stated hardware is a planning input, never a runtime fact. At install and boot the doctor records CPU cores, RAM, free disk, GPU/VRAM, driver, model residency, queue depth and service footprint.

Thresholds are calibrated per node:

- **safe baseline:** normal admission; reserve CONTROL ≥25% RAM and ≥20% disk, COMPUTE ≥20% VRAM and ≥25% RAM;
- **warning:** queue new heavy work and emit `resource.pressure`;
- **backpressure:** lower concurrency, unload idle models and prefer a validated smaller model;
- **hard:** admit only CONTROL-critical work;
- **emergency reserve:** stop optional work and preserve state/diagnostics.

These percentages are initial policy defaults, not claims about actual capacity. Heavy GPU concurrency starts at one and increases only after measured latency, VRAM headroom and recovery evidence. The scheduler never responds to pressure by spawning more workers.
