#!/usr/bin/env python3
"""Dependency-light contract smoke validator; full JSON Schema validators may be added later."""
from __future__ import annotations
import json, pathlib, sys
ROOT=pathlib.Path(__file__).resolve().parents[1]
SCHEMAS=ROOT/'.ai/schemas'
errors=[]
for p in sorted(SCHEMAS.glob('*.schema.json')):
 try: d=json.loads(p.read_text())
 except Exception as e: errors.append(f'{p}: invalid JSON: {e}'); continue
 if d.get('type')!='object' or d.get('additionalProperties') is not False: errors.append(f'{p}: boundary must be closed object')
 if 'schema_version' not in d.get('required',[]): errors.append(f'{p}: missing schema_version requirement')
 for req in d.get('required',[]):
  if req not in d.get('properties',{}): errors.append(f'{p}: required property {req!r} not defined')
 if '$id' not in d: errors.append(f'{p}: missing $id')
if errors:
 print('\n'.join(errors)); sys.exit(1)
out=ROOT/'.ai/evidence/T001-schema-validation.json'; out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps({'schema_version':'v1','status':'pass','schema_count':len(list(SCHEMAS.glob('*.schema.json'))),'schemas':[p.name for p in sorted(SCHEMAS.glob('*.schema.json'))]},indent=2)+'\n')
print(f'PASS: {len(list(SCHEMAS.glob("*.schema.json")))} schemas structurally validated; evidence={out}')
