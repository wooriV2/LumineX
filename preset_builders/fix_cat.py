import ast, re, shutil, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREV = "f60715c"

raw = subprocess.run(["git", "show", f"{PREV}:core/presets_meta.py"],
                     capture_output=True).stdout
old = raw.decode("utf-8", errors="replace")
old_keys = re.findall(r'^\s*"([^"]+)"\s*:\s*\[', old, re.M)

def broken(k): return bool("?" in k or re.search(r"[\u4E00-\u9FFF\uD7A4-\uD7FF]", k))
def tail(k):
    t = re.sub(r"^[^A-Za-z]+", "", k).strip()
    return t.replace("횞", "×")          # 본문 깨짐 보정

good = {tail(k): k for k in old_keys if not broken(k)}

p = ROOT / "core" / "presets_meta.py"
src = p.read_bytes().decode("utf-8-sig")
cur = re.findall(r'^\s*"([^"]+)"\s*:\s*\[', src, re.M)

mapping, fail = {}, []
for k in cur:
    if not broken(k): continue
    g = good.get(tail(k))
    if g and g != k: mapping[k] = g
    elif not g: fail.append(k)

if fail:
    print("[매칭 실패]"); [print("  " + repr(f)) for f in fail]

new = src
for k, g in mapping.items():
    new = new.replace(f'"{k}"', f'"{g}"')

try:
    ast.parse(new)
except SyntaxError as e:
    sys.exit(f"[중단] AST 실패: {e}")

left = [k for k in re.findall(r'^\s*"([^"]+)"\s*:\s*\[', new, re.M) if broken(k)]
shutil.copy2(p, p.with_suffix(".py.bak3"))
p.write_bytes(new.encode("utf-8"))

print(f"\n복원 {len(mapping)}개 / 잔존 손상 {len(left)}개")
for k in left: print("  남음: " + repr(k))
