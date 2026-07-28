import re, subprocess
from pathlib import Path

BAD_REV = "6c8b5e1"
prev = subprocess.run(["git", "rev-parse", "--short", f"{BAD_REV}^"],
                      capture_output=True, text=True).stdout.strip()

def cats(rev):
    raw = subprocess.run(["git", "show", f"{rev}:core/presets_meta.py"],
                         capture_output=True).stdout
    s = raw.decode("utf-8", errors="replace")
    return re.findall(r'^\s*"([^"]+)"\s*:\s*\[', s, re.M)

def broken(k): return bool("?" in k or re.search(r"[\u4E00-\u9FFF]", k))
def tail(k):   return re.sub(r"^[^A-Za-z]+", "", k).strip()

before, after = cats(prev), cats(BAD_REV)
good = {tail(k): k for k in before if not broken(k)}

out = [f"직전 {prev}: {len(before)}개 (손상 {sum(broken(k) for k in before)})",
       f"손상 {BAD_REV}: {len(after)}개 (손상 {sum(broken(k) for k in after)})", ""]

cur = cats("HEAD")
m = u = 0
out.append("── 복원 매핑 ──")
for k in cur:
    if not broken(k): continue
    g = good.get(tail(k))
    if g:
        out.append(f"  {k!r}\n    -> {g!r}"); m += 1
out.append("\n── 실패 ──")
for k in cur:
    if broken(k) and not good.get(tail(k)):
        out.append(f"  {k!r}  tail={tail(k)!r}"); u += 1
out.append(f"\n복원가능 {m} / 실패 {u}")

Path("cat_restore.txt").write_text("\n".join(out), encoding="utf-8")
print(f"직전 커밋 {prev} / 복원가능 {m} / 실패 {u}")
