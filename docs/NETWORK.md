# Network design

Local/private by default. CONTROL exposes an authenticated gateway; COMPUTE exposes only the worker protocol on the trusted LAN/VPN. Discovery may use mDNS/UDP only for non-secret presence; pairing uses a short-lived code plus mutual cryptographic identity. Internet is an optional egress capability for research, downloads, sync and deployment. Firewall changes require approval and are installer-reported.
