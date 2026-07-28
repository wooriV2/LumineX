import re, subprocess
from pathlib import Path

revs = subprocess.run(["git", "log", "--format=%h", "--reverse", "--", "core/presets_meta.py"],
                      capture_output=True, text=True).stdout.split()

rows = []
for r in revs:
    raw = subprocess.run(["git", "show", f"{r}:core/presets_meta.py"],
                         capture_output=True).stdout
    s = raw.decode("utf-8", errors="replace")
    keys = re.findall(r'^\s*"([^"]+)"\s*:\s*\[', s, re.M)
    bad = [k for k in keys if "?" in k or re.search(r"[\u4E00-\u9FFF]", k)]
    rows.append((r, len(keys), len(bad)))

out = ["rev       총   손상"]
prev = 0
first = None
for r, t, b in rows:
    mark = ""
    if b and not prev:
        mark = "  <<< 손상 시작"
        first = r
    out.append(f"{r}  {t:4d} {b:4d}{mark}")
    prev = b

Path("cat_history.txt").write_text("\n".join(out), encoding="utf-8")
print("\n".join(out[-25:]))
print(f"\n손상 시작 커밋: {first}")
