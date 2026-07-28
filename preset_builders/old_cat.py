import re, subprocess
from pathlib import Path

REV = "c91ddb8"
raw = subprocess.run(["git", "show", f"{REV}:core/presets_meta.py"],
                     capture_output=True).stdout
s = raw.decode("utf-8", errors="replace")

pat = re.compile(r'^\s*"([^"]+)"\s*:\s*\[', re.M)
keys = pat.findall(s)
bad = [k for k in keys if "?" in k or re.search(r"[\u4E00-\u9FFF]", k)]

out = [f"{REV} 기준  총 카테고리 {len(keys)}  손상 {len(bad)}", ""]
out.append("── 손상 ──")
out += [f"  {k!r}" for k in bad]
out.append("")
out.append("── 정상 ──")
out += [f"  {k}" for k in keys if k not in bad]
Path("old_cat.txt").write_text("\n".join(out), encoding="utf-8")
print(out[0])
