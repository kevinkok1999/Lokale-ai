# Hardware and node design

The stated target is an HP EliteDesk 800 G3 Mini (i5-7600, 16 GB) as CONTROL and Ryzen 7 7700 / RTX 5070 Ti / 32 GB as COMPUTE. These are planning inputs only. The installer must detect actual OS, CPU, RAM, disk, GPU, VRAM, driver, runtime and network state.

CONTROL should host only measured-light services. COMPUTE hosts local inference and GPU workloads behind an authenticated worker API. Roles CONTROL, COMPUTE, DEVELOPER and FULL are recommendations produced by detection, not assumptions.
