# Installer Freeze

## Target experience

Two role-specific installers:

1. AI-Core setup
2. RTX Compute Node setup

Normal users do not configure IP addresses, ports, Docker, databases, model routes or firewall rules.

## AI-Core

Supported paths:
- existing Ubuntu AI-Core host: guided remote bootstrap;
- fresh Proxmox: signed prebuilt AI-Core appliance with guided import.

Installer responsibilities:
- preflight
- dependency reconciliation
- secret generation
- control-plane services
- health checks
- short enrollment window
- rollback point
- diagnostics

## RTX Compute Node

Target: signed Windows installer.

Responsibilities:
- detect GPU, RAM, disk and driver
- install/reconcile compute dependencies
- discover AI-Core
- pair securely
- configure local firewall
- register capabilities
- calibrate resources
- perform end-to-end inference test

## Discovery and Pairing

Default discovery: mDNS/DNS-SD on the local network.

Default flow:
- node is discovered automatically;
- both sides display a matching short confirmation code;
- user confirms, normally without typing addresses or keys;
- AI-Core issues node identity;
- permanent communication uses TLS 1.3 mutual authentication.

Fallback:
- manual pairing code or advanced address entry.

Private keys remain local to the node.

Pairing is complete only when:
- mutual authentication passes;
- heartbeat passes;
- resource profile is registered;
- Ollama is reachable;
- end-to-end inference passes.

## Update Safety

Stable releases require:
- signed artifact
- integrity verification
- staged install
- health verification
- last-known-good rollback point
- automatic rollback on failed verification

## Resource Calibration

Limits are derived by runtime probe instead of hardcoded assumptions.

Baseline admission thresholds:
- RAM high-water: 80%
- RAM critical: 90%
- VRAM high-water: 85%
- VRAM critical: 92%
- sustained CPU high-water: 85%
- disk minimum free: 15%

The scheduler may become more conservative based on measured behavior.
