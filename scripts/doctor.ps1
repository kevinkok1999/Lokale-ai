$ErrorActionPreference='Stop'
$out = if ($args.Count) {$args[0]} else { '.ai/evidence/doctor-windows.json' }
$os=Get-CimInstance Win32_OperatingSystem; $cs=Get-CimInstance Win32_ComputerSystem
[ordered]@{schema_version='v1'; verified_at=(Get-Date).ToUniversalTime().ToString('o'); os=$os.Caption; version=$os.Version; cpu=$cs.NumberOfLogicalProcessors; ram_bytes=$cs.TotalPhysicalMemory; note='Run on target node; redact before sharing'} | ConvertTo-Json | Set-Content -Encoding UTF8 $out
Write-Output $out
