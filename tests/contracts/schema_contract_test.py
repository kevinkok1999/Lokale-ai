import json, pathlib, unittest
ROOT=pathlib.Path(__file__).resolve().parents[2]
class ContractTest(unittest.TestCase):
 def test_all_required_properties_are_declared(self):
  for p in (ROOT/'.ai/schemas').glob('*.schema.json'):
   d=json.loads(p.read_text()); self.assertIn('schema_version',d['required']); self.assertFalse(d['additionalProperties'])
   for key in d['required']: self.assertIn(key,d['properties'],p.name)
 def test_unknown_fields_rejected_by_policy(self):
  for p in (ROOT/'.ai/schemas').glob('*.schema.json'):
   d=json.loads(p.read_text()); self.assertFalse(d['additionalProperties'],p.name)
if __name__=='__main__': unittest.main()
