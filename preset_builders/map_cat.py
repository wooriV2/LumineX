import json, re, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import core.presets_meta as M

def broken(s): return "?" in s or re.search(r"[\u4E00-\u9FFF]", s)
def tail(s):   return re.sub(r"^[^A-Za-z]+", "", s).strip()

# JSON에서 온전한 카테고리 수집
good = {}
for f in (ROOT / "presets").glob("*.json"):
    try: d = json.loads(f.read_text(encoding="utf-8-sig"))
    except Exception: continue
    if isinstance(d, dict):
        c = d.get("category")
        if isinstance(c, str) and c and not broken(c):
            good.setdefault(tail(c), c)

# presets_meta 손상 키
bad = []
for n, v in vars(M).items():
    if isinstance(v, dict) and not n.startswith("__"):
        for k in v:
            if isinstance(k, str) and broken(k): bad.append((n, k))

out, m, u = [], 0, 0
out.append(f"JSON 온전 카테고리 {len(good)}종 / 손상 키 {len(bad)}개\n")
out.append("── 매칭됨 ──")
for src, k in bad:
    g = good.get(tail(k))
    if g: out.append(f"  {k!r}\n    -> {g!r}"); m += 1
out.append("\n── 매칭 실패 ──")
for src, k in bad:
    if not good.get(tail(k)): out.append(f"  [{src}] {k!r}  (tail={tail(k)!r})"); u += 1
out.append(f"\n매칭 {m} / 실패 {u}")

Path("cat_map.txt").write_text("\n".join(out), encoding="utf-8")
print(f"매칭 {m} / 실패 {u}  -> cat_map.txt")
