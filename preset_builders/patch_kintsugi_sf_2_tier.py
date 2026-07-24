# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "ksf_bp_001", "ksf_bp_002", "ksf_bp_003", "ksf_bp_004", "ksf_bp_005",
    "ksf_bp_006", "ksf_bp_007", "ksf_bp_008", "ksf_bp_009", "ksf_bp_010",
    "ksf_bp_016", "ksf_bp_018", "ksf_bp_021", "ksf_bp_022", "ksf_bp_024",
    "ksf_bp_025", "ksf_bp_026", "ksf_bp_028", "ksf_bp_029", "ksf_bp_031",
    "ksf_bp_032", "ksf_bp_033", "ksf_bp_034", "ksf_bp_035",
]

SSS_KEYS = [
    "ksf_bp_011", "ksf_bp_012", "ksf_bp_013", "ksf_bp_014", "ksf_bp_015",
    "ksf_bp_017", "ksf_bp_019", "ksf_bp_020", "ksf_bp_023", "ksf_bp_027",
    "ksf_bp_030",
]

META_KEYS = HOF_KEYS + SSS_KEYS

# ── hof_tier.py 패치 ──
HOF_PATH = r"C:\Dev\LumineX\core\hof_tier.py"
with open(HOF_PATH, encoding="utf-8-sig") as f:
    src = f.read()
insert = "\n" + "\n".join(f'    "{k}",' for k in HOF_KEYS) + "\n"
src = src.rstrip()
src = re.sub(r'(\})\s*$', insert + r'\1', src)
with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(src)
ast.parse(open(HOF_PATH, encoding="utf-8").read())
print("✅ hof_tier.py 패치 완료")

# ── sss_tier.py 패치 ──
SSS_PATH = r"C:\Dev\LumineX\core\sss_tier.py"
with open(SSS_PATH, encoding="utf-8-sig") as f:
    src = f.read()
insert = "\n" + "\n".join(f'    "{k}",' for k in SSS_KEYS) + "\n"
src = src.rstrip()
src = re.sub(r'(\})\s*$', insert + r'\1', src)
with open(SSS_PATH, "w", encoding="utf-8") as f:
    f.write(src)
ast.parse(open(SSS_PATH, encoding="utf-8").read())
print("✅ sss_tier.py 패치 완료")

# ── presets_meta.py 패치 ──
META_PATH = r"C:\Dev\LumineX\core\presets_meta.py"
with open(META_PATH, encoding="utf-8-sig") as f:
    src = f.read()
insert = "\n" + "\n".join(f'    "{k}",' for k in META_KEYS) + "\n"
src = src.rstrip()
src = re.sub(r'(\})\s*$', insert + r'\1', src)
with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(src)
ast.parse(open(META_PATH, encoding="utf-8").read())
print("✅ presets_meta.py 패치 완료")

print("\n✅ Kintsugi Silver Fox tier 패치 완료")
print(f"   HOF: {len(HOF_KEYS)}개")
print(f"   SSS: {len(SSS_KEYS)}개")
