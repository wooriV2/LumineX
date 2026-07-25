# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "ksf_bp_001", "ksf_bp_002", "ksf_bp_003", "ksf_bp_004", "ksf_bp_005",
    "ksf_bp_006", "ksf_bp_007", "ksf_bp_008", "ksf_bp_009", "ksf_bp_010",
    "ksf_bp_016", "ksf_bp_018", "ksf_bp_021", "ksf_bp_022", "ksf_bp_024",
    "ksf_bp_025", "ksf_bp_026", "ksf_bp_028", "ksf_bp_029", "ksf_bp_031",
    "ksf_bp_032", "ksf_bp_033", "ksf_bp_034", "ksf_bp_035",
]

def patch_set_file(path, keys):
    with open(path, encoding="utf-8-sig") as f:
        src = f.read()
    insert = "\n" + "\n".join(f'    "{k}",' for k in keys) + "\n"
    src = src.rstrip()
    src = re.sub(r'(\})\s*$', insert + r'\1', src)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    ast.parse(open(path, encoding="utf-8").read())
    print(f"✅ {path} 패치 완료")

def patch_meta(path, keys, category):
    with open(path, encoding="utf-8-sig") as f:
        src = f.read()
    insert = "\n" + "\n".join(
        f'    "{k}": {{"key": "{k}", "category": "{category}"}},'
        for k in keys
    ) + "\n"
    src = src.rstrip()
    src = re.sub(r'(\})\s*$', insert + r'\1', src)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    ast.parse(open(path, encoding="utf-8").read())
    print(f"✅ {path} 패치 완료")

patch_set_file(r"C:\Dev\LumineX\core\hof_tier.py", HOF_KEYS)
patch_meta(r"C:\Dev\LumineX\core\presets_meta.py", HOF_KEYS, "🎨 Kintsugi Silver Fox")
print("🎉 Kintsugi Silver Fox tier 패치 완료")
