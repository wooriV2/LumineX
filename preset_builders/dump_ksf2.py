import json, glob
from pathlib import Path
out = []
for f in sorted(glob.glob("presets/ksf_bp_*.json")):
    d = json.loads(open(f, encoding="utf-8-sig").read())
    key = Path(f).stem
    p = d.get("prompt", "")
    out.append(f"=== {key}   tier={d.get('tier','-')}   cat={d.get('category','-')}")
    out.append(f"  LABEL : {d.get('label','-')}")
    out.append(f"  KEY   : {d.get('key','-')}")
    out.append(f"  BODY  : {p[80:400]}")
    out.append(f"  PAINT : {p[400:900]}")
    out.append("")
Path("ksf_dump2.txt").write_text("\n".join(out), encoding="utf-8")
print(f"OK {len(out)}줄")
