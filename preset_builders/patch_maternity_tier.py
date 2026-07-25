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
patch_meta(r"C:\Dev\LumineX\core\presets_meta.py", HOF_KEYS, "🤰 Maternity")
print("🎉 Maternity tier 패치 완료")
