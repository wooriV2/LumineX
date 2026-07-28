import re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = []
BAD = re.compile(r"[\uAC00-\uD7A3\u4E00-\u9FFF?]*(빽|截|븳|뮌|븧|뵾|뷀|뜀|땀|뤄)[^\"']*")
for name in ("dashboard.py", "core/presets_meta.py", "core/data.py"):
    p = ROOT / name
    if not p.exists(): continue
    for i, l in enumerate(p.read_text(encoding="utf-8").split("\n"), 1):
        if re.search(r"빽|截|븳|뮌", l):
            OUT.append(f"{name} L{i}: {l.strip()[:150]}")
Path("mojibake.txt").write_text("\n".join(OUT), encoding="utf-8")
print("\n".join(OUT))
