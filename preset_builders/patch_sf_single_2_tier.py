# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "sf_single_empress_dragon",
    "sf_single_carnival_jaguar",
    "sf_single_viking_byzantine",
    "sf_single_celtic_amazon",
    "sf_single_nubian_bbw",
    "sf_single_roman_supermodel",
    "sf_single_bubble_corset",
    "sf_single_widehip_thigh",
    "sf_single_thracian_warrior",
    "sf_single_babylon_fire",
    "sf_single_dacian_empress",
    "sf_single_nubian_phoenix",
    "sf_single_aztec_muscle",
    "sf_single_viking_hourglass",
    "sf_single_nubian_bbw_empress",
    "sf_single_ottoman_corset",
    "sf_single_celtic_legend",
    "sf_single_aztec_muscular_hourglass",
    "sf_single_inca_bbw_widehip",
    "sf_single_egyptian_bbw_folds",
    "sf_single_nordic_runway_slim",
    "sf_single_serbian_muscle",
    "sf_single_nubian_super_bbw_elder",
    "sf_single_irish_runway_redhead",
    "sf_single_hungarian_hourglass_sitting",
    "sf_single_yoruba_muscle_kneel",
    "sf_single_polish_bbw_leaning",
    "sf_single_romanian_runway_silver",
    "sf_single_lebanese_hourglass_floor",
    "sf_single_bulgarian_bbw_back",
    "sf_single_neon_babylon",
]

SSS_KEYS = [
    "sf_single_magyar_ottoman",
    "sf_single_ishtar_persian",
    "sf_single_persian_petite",
    "sf_single_mongolian_warrior",
    "sf_single_corset_empress",
    "sf_single_ukrainian_bbw_young",
    "sf_single_nubian_water_reflection",
    "sf_single_russian_marble_reflection",
]

META_KEYS = HOF_KEYS + SSS_KEYS

# ── 1. hof_tier.py 패치 ──────────────────────────────────────────
HOF_PATH = r"C:\Dev\LumineX\core\hof_tier.py"
with open(HOF_PATH, encoding="utf-8-sig") as f:
    hof_src = f.read()

hof_insert = "\n" + "\n".join(f'    "{k}",' for k in HOF_KEYS) + "\n"
hof_src = hof_src.rstrip()
hof_src = re.sub(r'(\})\s*$', hof_insert + r'\1', hof_src)

with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof_src)

ast.parse(open(HOF_PATH, encoding="utf-8").read())
print("✅ hof_tier.py 패치 및 AST 검증 완료")

# ── 2. sss_tier.py 패치 ──────────────────────────────────────────
SSS_PATH = r"C:\Dev\LumineX\core\sss_tier.py"
with open(SSS_PATH, encoding="utf-8-sig") as f:
    sss_src = f.read()

sss_insert = "\n" + "\n".join(f'    "{k}",' for k in SSS_KEYS) + "\n"
sss_src = sss_src.rstrip()
sss_src = re.sub(r'(\})\s*$', sss_insert + r'\1', sss_src)

with open(SSS_PATH, "w", encoding="utf-8") as f:
    f.write(sss_src)

ast.parse(open(SSS_PATH, encoding="utf-8").read())
print("✅ sss_tier.py 패치 및 AST 검증 완료")

# ── 3. presets_meta.py 패치 ──────────────────────────────────────
META_PATH = r"C:\Dev\LumineX\core\presets_meta.py"
with open(META_PATH, encoding="utf-8-sig") as f:
    meta_src = f.read()

meta_insert = "\n" + "\n".join(f'    "{k}": {{"key": "{k}", "category": "👤 Silver Fox SINGLE"}},' for k in META_KEYS) + "\n"
meta_src = meta_src.rstrip()
meta_src = re.sub(r'(\})\s*$', meta_insert + r'\1', meta_src)

with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta_src)

ast.parse(open(META_PATH, encoding="utf-8").read())
print("✅ presets_meta.py 패치 및 AST 검증 완료")

print(f"\n🎉 전체 패치 완료! HOF {len(HOF_KEYS)}개 / SSS {len(SSS_KEYS)}개")
