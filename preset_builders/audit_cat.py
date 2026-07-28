import re, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import core.presets_meta as M

cats = []
for n, v in vars(M).items():
    if isinstance(v, dict) and not n.startswith("__"):
        for k in v:
            if isinstance(k, str): cats.append((n, k))

ok, bad = [], []
for src, k in cats:
    if "?" in k or re.search(r"[\u4E00-\u9FFF]", k):
        bad.append((src, k))
    else:
        ok.append((src, k))

out = [f"총 키 {len(cats)}  정상 {len(ok)}  손상 {len(bad)}", "", "── 손상 ──"]
for s, k in bad: out.append(f"  [{s}] {k!r}")
out += ["", "── 정상 ──"]
for s, k in ok[:40]: out.append(f"  [{s}] {k}")

Path("cat_audit.txt").write_text("\n".join(out), encoding="utf-8")
print(out[0])
