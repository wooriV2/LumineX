import re, ast

# ── HOF 키 목록 ──────────────────────────────────────────────
HOF_KEYS = [
    # H 신규
    "irezumi_dragon_wisteria_milf_budapest",
    "irezumi_dragon_wisteria_hourglass_marrakech",
    "irezumi_dragon_wisteria_petite_kyoto",
    "irezumi_dragon_wisteria_mature_bbw_istanbul",
    "irezumi_dragon_wisteria_superbbw_void",
    "irezumi_dragon_wisteria_hourglass_santorini",
    # I 모티프
    "irezumi_skull_chrysanthemum_black_glam_void",
    "irezumi_skull_chrysanthemum_aurora_nordic",
    "irezumi_skull_chrysanthemum_hourglass_istanbul",
    "irezumi_skull_chrysanthemum_superbbw_void",
    "irezumi_skull_chrysanthemum_mature_bbw_paris",
    "irezumi_skull_chrysanthemum_hourglass_mexico",
    "irezumi_skull_chrysanthemum_superbbw_dubai",
    "irezumi_skull_chrysanthemum_superbbw_kyoto",
    "irezumi_skull_chrysanthemum_superbbw_marrakech",
    "irezumi_skull_chrysanthemum_crimson_void",
    "irezumi_skull_chrysanthemum_violet_istanbul",
]

# ── SSS 키 목록 ─────────────────────────────────────────────
SSS_KEYS = [
    # H 신규
    "irezumi_dragon_wisteria_bbw_cape_town",
    "irezumi_dragon_wisteria_superbbw_rio",
    "irezumi_dragon_wisteria_muscular_tokyo",
    "irezumi_dragon_wisteria_athletic_void",
    "irezumi_dragon_wisteria_bbw_dubai",
    "irezumi_dragon_wisteria_athletic_new_york",
    "irezumi_dragon_wisteria_mature_hourglass_void",
    # I 모티프
    "irezumi_skull_chrysanthemum_bbw_versailles",
    "irezumi_skull_chrysanthemum_hourglass_tokyo",
    "irezumi_skull_chrysanthemum_superbbw_void2",
    "irezumi_skull_chrysanthemum_gold_void",
    "irezumi_skull_chrysanthemum_copper_marrakech",
    "irezumi_skull_chrysanthemum_folds_void_side",
    "irezumi_skull_chrysanthemum_folds_istanbul",
]

# ── 전체 키 목록 (meta용) ────────────────────────────────────
ALL_H_KEYS = [
    "irezumi_dragon_wisteria_milf_budapest",
    "irezumi_dragon_wisteria_bbw_cape_town",
    "irezumi_dragon_wisteria_superbbw_rio",
    "irezumi_dragon_wisteria_muscular_tokyo",
    "irezumi_dragon_wisteria_hourglass_marrakech",
    "irezumi_dragon_wisteria_runway_seoul",
    "irezumi_dragon_wisteria_petite_kyoto",
    "irezumi_dragon_wisteria_mature_bbw_istanbul",
    "irezumi_dragon_wisteria_athletic_void",
    "irezumi_dragon_wisteria_superbbw_void",
    "irezumi_dragon_wisteria_bbw_dubai",
    "irezumi_dragon_wisteria_hourglass_santorini",
    "irezumi_dragon_wisteria_athletic_new_york",
    "irezumi_dragon_wisteria_mature_hourglass_void",
]

ALL_I_KEYS = [
    "irezumi_skull_chrysanthemum_black_glam_void",
    "irezumi_skull_chrysanthemum_aurora_nordic",
    "irezumi_skull_chrysanthemum_bbw_versailles",
    "irezumi_skull_chrysanthemum_runway_void",
    "irezumi_skull_chrysanthemum_hourglass_istanbul",
    "irezumi_skull_chrysanthemum_superbbw_void",
    "irezumi_skull_chrysanthemum_hourglass_tokyo",
    "irezumi_skull_chrysanthemum_mature_bbw_paris",
    "irezumi_skull_chrysanthemum_athletic_void",
    "irezumi_skull_chrysanthemum_hourglass_mexico",
    "irezumi_skull_chrysanthemum_superbbw_void2",
    "irezumi_skull_chrysanthemum_superbbw_dubai",
    "irezumi_skull_chrysanthemum_superbbw_kyoto",
    "irezumi_skull_chrysanthemum_superbbw_marrakech",
    "irezumi_skull_chrysanthemum_gold_void",
    "irezumi_skull_chrysanthemum_crimson_void",
    "irezumi_skull_chrysanthemum_violet_istanbul",
    "irezumi_skull_chrysanthemum_copper_marrakech",
    "irezumi_skull_chrysanthemum_white_void",
    "irezumi_skull_chrysanthemum_folds_void_side",
    "irezumi_skull_chrysanthemum_folds_istanbul",
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
    print(f"✅ {path} 패치 완료 ({len(keys)}개)")


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
    print(f"✅ {path} 패치 완료 ({len(keys)}개)")


# 실행
patch_set_file("core/hof_tier.py", HOF_KEYS)
patch_set_file("core/sss_tier.py", SSS_KEYS)
patch_meta("core/presets_meta.py", ALL_H_KEYS, "🐉 Irezumi Motif H")
patch_meta("core/presets_meta.py", ALL_I_KEYS, "💀 Irezumi Motif I")

print("\n✅ H/I 이레즈미 패치 전체 완료")
print(f"  HOF: {len(HOF_KEYS)}개")
print(f"  SSS: {len(SSS_KEYS)}개")
print(f"  전체: {len(ALL_H_KEYS) + len(ALL_I_KEYS)}개")
