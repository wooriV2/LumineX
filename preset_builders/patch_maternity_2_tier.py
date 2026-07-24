# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "maternity_kintsugi_superbbw_crimson_side",
    "maternity_irezumi_bubblebutt_blackgold_rear",
    "maternity_lace_runway_white_side",
    "maternity_bodypaint_hourglass_blue_frontal",
    "maternity_irezumi_superbbw_cobalt_side",
    "maternity_lace_hourglass_black_rear",
    "maternity_kintsugi_hourglass_emerald_kneeling",
    "maternity_kintsugi_muscular_copper_side",
    "maternity_bodypaint_superbbw_galaxy_side",
    "maternity_henna_hourglass_terracotta_kneeling",
    "maternity_glitter_bubblebutt_rose_rear",
    "maternity_bodypaint_superbbw_lava_side",
    "maternity_irezumi_hourglass_redgold_kneeling",
    "maternity_lace_superbbw_gold_side",
    "maternity_bodypaint_runway_aurora_side",
    "maternity_bodypaint_superbbw_deepocean_side",
    "maternity_bodypaint_hourglass_sakura_kneeling",
    "maternity_bodypaint_bubblebutt_fire_rear",
    "maternity_bodypaint_muscular_arctic_side",
    "maternity_irezumi_korean_imoogi_side",
    "maternity_irezumi_korean_crane_kneeling",
    "maternity_irezumi_korean_tiger_rear",
    "maternity_irezumi_korean_lotus_frontal",
    "maternity_irezumi_korean_bonghwang_side",
    "maternity_bodypaint_korean_galaxy_side",
    "maternity_bodypaint_korean_deepocean_kneeling",
    "maternity_bodypaint_korean_aurora_side",
    "maternity_neon_superbbw_uv_side",
    "maternity_watercolor_runway_pastel_kneeling",
    "maternity_mandala_hourglass_gold_frontal",
    "maternity_goldleaf_muscular_pure_side",
    "maternity_dancheong_korean_traditional_kneeling",
    "maternity_neon_superbbw_uv_squat",
    "maternity_neon_muscular_uv_doublebicep",
    "maternity_neon_hourglass_uv_kneeling",
    "maternity_neon_runway_uv_side",
    "maternity_neon_superbbw_uv_planet_side",
    "maternity_neon_bubblebutt_uv_mandala_rear",
    "maternity_neon_hourglass_uv_phoenix_kneeling",
    "maternity_neon_muscular_uv_dragon_frontal",
    "maternity_neon_runway_uv_cosmic_goddess_kneeling",
]

SSS_KEYS = [
    "maternity_kintsugi_hourglass_gold_kneeling",
    "maternity_glitter_superbbw_silver_side",
    "maternity_bodypaint_runway_tropical_kneeling",
    "maternity_glitter_bubblebutt_gold_kneeling",
    "maternity_kintsugi_muscular_violet_kneeling",
    "maternity_kintsugi_superbbw_cobalt_frontal",
    "maternity_kintsugi_superbbw_violet_squat",
    "maternity_bodypaint_korean_phoenix_rear",
    "maternity_bodypaint_korean_lava_frontal",
    "maternity_neon_bubblebutt_uv_rear",
    "maternity_glitter_bubblebutt_rose_kneeling",
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

print("\n✅ Maternity tier 패치 완료")
print(f"   HOF: {len(HOF_KEYS)}개")
print(f"   SSS: {len(SSS_KEYS)}개")
