# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "cb_001", "cb_002", "cb_003", "cb_004", "cb_008",
    "cb_009", "cb_011", "cb_013", "cb_015", "cb_016",
    "cb_017", "cb_018", "cb_019",
]

SSS_KEYS = [
    "cb_005", "cb_006", "cb_007", "cb_010", "cb_012",
    "cb_014", "cb_020",
]

ALL_KEYS = HOF_KEYS + SSS_KEYS

def patch_set_file(path, keys):
    with open(path, encoding="utf-8-sig") as f:
        src = f.read()
    insert = "\n" + "\n".join(f"    \"{k}\"," for k in keys) + "\n"
    src = src.rstrip()
    src = re.sub(r"(\})\s*$", insert + r"\1", src)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    ast.parse(open(path, encoding="utf-8").read())
    print(f"✅ {path} 패치 완료")

def patch_meta(path, keys, category):
    with open(path, encoding="utf-8-sig") as f:
        src = f.read()
    insert = "\n" + "\n".join(
        f"    \"{k}\": {{\"key\": \"{k}\", \"category\": \"{category}\"}},"
        for k in keys
    ) + "\n"
    src = src.rstrip()
    src = re.sub(r"(\})\s*$", insert + r"\1", src)
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)
    ast.parse(open(path, encoding="utf-8").read())
    print(f"✅ {path} 패치 완료")

patch_set_file(r"C:\Dev\LumineX\core\hof_tier.py", HOF_KEYS)
patch_set_file(r"C:\Dev\LumineX\core\sss_tier.py", SSS_KEYS)
patch_meta(r"C:\Dev\LumineX\core\presets_meta.py", ALL_KEYS, "🦾 Cyborg/Biomech")
print("🎉 Cyborg/Biomech tier 패치 완료")
