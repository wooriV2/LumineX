# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "irezumi_dragon_wisteria_vs_angel_kyoto",
    "irezumi_dragon_wisteria_mature_onsen",
    "irezumi_dragon_wisteria_runway_neon",
    "irezumi_dragon_wisteria_colombian_versailles",
    "irezumi_dragon_wisteria_bbw_monaco",
    "irezumi_dragon_wisteria_hourglass_dubai",
    "irezumi_dragon_wisteria_fitness_strobe",
    "irezumi_dragon_wisteria_mature_paris",
    "irezumi_dragon_wisteria_ballerina_void",
]

SSS_KEYS = [
    "irezumi_dragon_wisteria_sports_glam_void",
    "irezumi_dragon_wisteria_petite_aurora",
    "irezumi_dragon_wisteria_muscular_void",
    "irezumi_dragon_wisteria_superbbw_bali",
    "irezumi_dragon_wisteria_slim_santorini",
    "irezumi_dragon_wisteria_hourglass_rio",
    "irezumi_dragon_wisteria_milf_budapest",
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
patch_meta(r"C:\Dev\LumineX\core\presets_meta.py", ALL_KEYS, "🐉 이레즈미")
print("🎉 이레즈미 H 모티프 tier 패치 완료")
