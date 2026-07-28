from pathlib import Path
import ast, shutil

P = Path("dashboard.py")
raw = P.read_bytes()
BOM = raw.startswith(b"\xef\xbb\xbf")
src = raw.decode("utf-8-sig")

OLD = "wearing_line  = _build_wearing_line(outfit_text, material_text, footwear_text)"
NEW = "wearing_line  = _build_wearing_line(outfit_text, material_text, footwear_text, p.get('environment', ''))"

if OLD not in src:
    raise SystemExit("대상 없음 — 이미 수정됐거나 문구가 다릅니다")
if src.count(OLD) != 1:
    raise SystemExit(f"매칭 {src.count(OLD)}회 (1회여야 함)")

new = src.replace(OLD, NEW)
ast.parse(new)

shutil.copy2(P, P.with_suffix(".py.bak2"))
P.write_bytes((b"\xef\xbb\xbf" if BOM else b"") + new.encode("utf-8"))
print(f"OK — env_text 전달 추가 (BOM={BOM})")
