#!/usr/bin/env bash
set -euo pipefail
out="${1:-.ai/evidence/doctor-$(date -u +%Y%m%dT%H%M%SZ).json}"
mkdir -p "$(dirname "$out")"
python3 - "$out" <<'PY'
import json,platform,shutil,subprocess,sys
out=sys.argv[1]
def run(c):
 try:return subprocess.check_output(c,stderr=subprocess.STDOUT,text=True,timeout=5).strip()
 except Exception:return None
r={"schema_version":"v1","scope":"repository-workspace","verified_at":__import__('datetime').datetime.now(__import__('datetime').timezone.utc).isoformat(),"os":platform.platform(),"python":platform.python_version(),"cpu":platform.processor(),"git":run(["git","rev-parse","--show-toplevel"]),"tools":{x:shutil.which(x) for x in ["git","docker","node","npm","python3"]},"notes":["Workspace report only; not evidence about target CONTROL or COMPUTE machines."]}
open(out,'w').write(json.dumps(r,indent=2)+"\n");print(out)
PY
