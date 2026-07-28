import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core.hof_tier import HOF_TIER
import core.presets_meta as M

ROOT = Path(__file__).resolve().parents[1]
meta = {}
for n, v in vars(M).items():
    if isinstance(v, dict) and not n.startswith("__"):
        meta.update(v)

files = {p.stem for p in (ROOT / "presets").glob("ksf_*.json")}
hof   = {k for k in HOF_TIER if k.startswith("ksf")}
mk    = {k for k in meta if isinstance(k, str) and k.startswith("ksf")}

print(f"JSON {len(files)} / HOF {len(hof)} / META {len(mk)}")
print(f"구키 잔존 — HOF:{sum('ksf_bp_' in k for k in hof)}  META:{sum('ksf_bp_' in k for k in mk)}")
print(f"HOF에만: {sorted(hof - files)}")
print(f"META에만: {sorted(mk - files)}")
print(f"META 누락: {sorted(files - mk)}")
bad = [f.stem for f in (ROOT/'presets').glob('ksf_*.json')
       if json.loads(f.read_text(encoding='utf-8-sig')).get('key') != f.stem]
print(f"key 불일치: {bad}")
