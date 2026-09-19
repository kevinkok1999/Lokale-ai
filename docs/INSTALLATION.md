# Installation architecture

`START-HERE.cmd` will launch a signed, integrity-checked, resumable PowerShell bootstrap on Windows; shell equivalent on Linux. It detects role, prerequisites and hardware, asks before privileged/material changes, generates local secrets, installs pinned dependencies, starts services, runs health and acceptance tests, and writes a redacted machine-readable report. Distribution packages contain no secrets.
