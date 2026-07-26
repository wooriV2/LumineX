import re, ast

HOF_KEYS = [
    # KSF 추가분
    "silverfox_trio_aurora_tiger_plasma_void",
    "silverfox_trio_superbbw_superbbw_muscular_bioluminescent_solar_holographic",
    "silverfox_trio_superbbw_hourglass_muscular_violet_murmuration_plasma",
    "silverfox_trio_superbbw_pregnant_muscular_plasma_murmuration_crimson",
    # Ancient Gods HOF
    "ancient_gods_kali_hindu_void",
    "ancient_gods_artemis_greece_void",
    "ancient_gods_freya_nordic_void",
    "ancient_gods_isis_egypt_void",
    "ancient_gods_oshun_yoruba_void",
    "ancient_gods_durga_hindu_void",
    "ancient_gods_morrigan_celtic_void",
    "ancient_gods_inanna_sumerian_void",
    "ancient_gods_hera_greece_ivory_void",
    "ancient_gods_persephone_greece_ivory_void",
    "ancient_gods_athena_greece_ivory_void",
    "ancient_gods_nyx_greek_void",
    "ancient_gods_hera_black_superbbw_void",
]

SSS_KEYS = [
    # Ancient Gods SSS
    "ancient_gods_hathor_egypt_void",
    "ancient_gods_aphrodite_greece_ivory_void",
    "ancient_gods_tiamat_babylon_superbbw_void",
]

KSF_KEYS = [
    "silverfox_trio_aurora_tiger_plasma_void",
    "silverfox_trio_superbbw_superbbw_muscular_bioluminescent_solar_holographic",
    "silverfox_trio_superbbw_hourglass_muscular_violet_murmuration_plasma",
    "silverfox_trio_superbbw_pregnant_muscular_plasma_murmuration_crimson",
]

AG_KEYS = [
    "ancient_gods_kali_hindu_void",
    "ancient_gods_artemis_greece_void",
    "ancient_gods_freya_nordic_void",
    "ancient_gods_isis_egypt_void",
    "ancient_gods_oshun_yoruba_void",
    "ancient_gods_durga_hindu_void",
    "ancient_gods_morrigan_celtic_void",
    "ancient_gods_inanna_sumerian_void",
    "ancient_gods_hera_greece_ivory_void",
    "ancient_gods_persephone_greece_ivory_void",
    "ancient_gods_athena_greece_ivory_void",
    "ancient_gods_nyx_greek_void",
    "ancient_gods_hera_black_superbbw_void",
    "ancient_gods_hathor_egypt_void",
    "ancient_gods_aphrodite_greece_ivory_void",
    "ancient_gods_tiamat_babylon_superbbw_void",
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


patch_set_file("core/hof_tier.py", HOF_KEYS)
patch_set_file("core/sss_tier.py", SSS_KEYS)
patch_meta("core/presets_meta.py", KSF_KEYS, "🦊 Silver Fox TRIO")
patch_meta("core/presets_meta.py", AG_KEYS, "⚡ Ancient Gods")

print("\n✅ KSF 추가분 + Ancient Gods 패치 완료")
print(f"  HOF: {len(HOF_KEYS)}개")
print(f"  SSS: {len(SSS_KEYS)}개")
print(f"  KSF 신규: {len(KSF_KEYS)}개")
print(f"  Ancient Gods 신규: {len(AG_KEYS)}개")
