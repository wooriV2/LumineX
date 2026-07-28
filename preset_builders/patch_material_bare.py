import json, re, shutil, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from core.builders import _env_has_footwear

ROOT = Path(__file__).resolve().parents[1]
PAT = re.compile(r",?\s*with\s+hands\s+and\s+feet\s+bare|,?\s*hands\s+and\s+feet\s+bare", re.I)

hit, skip = [], 0
for f in sorted((ROOT / "presets").glob("*.json")):
    try:
        d = json.loads(f.read_text(encoding="utf-8-sig"))
    except Exception:
        continue
    if not isinstance(d, dict): continue
    env, mat = d.get("environment", ""), d.get("material", "")
    if not (env and mat and _env_has_footwear(env)): continue
    if not PAT.search(mat): continue
    new = re.sub(r"\s{2,}", " ", PAT.sub("", mat)).replace(" ,", ",").strip()
    hit.append((f, d, mat, new))

if not hit:
    raise SystemExit("대상 없음")

print(f"대상 {len(hit)}개\n")
for f, d, old, new in hit:
    print(f"--- {f.stem}")
    print(f"  전: ...{old[-110:]}")
    print(f"  후: ...{new[-110:]}\n")

for f, d, old, new in hit:
    shutil.copy2(f, f.with_suffix(".json.bak"))
    d["material"] = new
    f.write_text(json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")

print(f"OK — {len(hit)}개 수정 (.bak 생성)")
