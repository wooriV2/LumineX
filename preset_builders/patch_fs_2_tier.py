# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "fs_001", "fs_002", "fs_003", "fs_004", "fs_005",
    "fs_007", "fs_008", "fs_009", "fs_011", "fs_012",
    "fs_014", "fs_015", "fs_017", "fs_018", "fs_019",
    "fs_020", "fs_022", "fs_023", "fs_024", "fs_028",
    "fs_029", "fs_030", "fs_031", "fs_032", "fs_033",
    "fs_034", "fs_035", "fs_037", "fs_038", "fs_039",
    "fs_041", "fs_042", "fs_044", "fs_045", "fs_047",
    "fs_048", "fs_050",
]

SSS_KEYS = [
    "fs_006", "fs_010", "fs_013", "fs_016", "fs_025",
    "fs_027", "fs_036", "fs_040", "fs_043", "fs_049",
]

ALL_KEYS = HOF_KEYS + SSS_KEYS

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
patch_set_file(r"C:\Dev\LumineX\core\sss_tier.py", SSS_KEYS)
patch_meta(r"C:\Dev\LumineX\core\presets_meta.py", ALL_KEYS, "⚡ Fracture Split")
print("🎉 Fracture Split tier 패치 완료")
