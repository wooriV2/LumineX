# -*- coding: utf-8 -*-
import ast, re

META_PATH = r"C:\Dev\LumineX\core\presets_meta.py"

with open(META_PATH, encoding="utf-8-sig") as f:
    src = f.read()

# 잘못 삽입된 키만 있는 라인들 제거 (값 없는 dict 키)
# "ksf_bp_001", 형태의 라인 제거
src = re.sub(r'\n\s+"ksf_bp_\d+",', '', src)
src = re.sub(r'\n\s+"maternity_[a-z0-9_]+",', '', src)

# 올바른 dict 형태로 삽입
KSF_KEYS = [
    "ksf_bp_001", "ksf_bp_002", "ksf_bp_003", "ksf_bp_004", "ksf_bp_005",
    "ksf_bp_006", "ksf_bp_007", "ksf_bp_008", "ksf_bp_009", "ksf_bp_010",
    "ksf_bp_016", "ksf_bp_018", "ksf_bp_021", "ksf_bp_022", "ksf_bp_024",
    "ksf_bp_025", "ksf_bp_026", "ksf_bp_028", "ksf_bp_029", "ksf_bp_031",
    "ksf_bp_032", "ksf_bp_033", "ksf_bp_034", "ksf_bp_035",
]

MATERNITY_HOF_KEYS = [
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

MATERNITY_SSS_KEYS = [
    "maternity_kintsugi_hourglass_gold_kneeling",
    "maternity_glitter_superbbw_silver_side",
    "maternity_bodypaint_runway_tropical_kneeling",
    "maternity_glitter_bubblebutt_gold_kneeling",
    "maternity_kintsugi_muscular_violet_kneeling",
    "maternity_bodypaint_korean_phoenix_rear",
    "maternity_bodypaint_korean_lava_frontal",
    "maternity_neon_bubblebutt_uv_rear",
    "maternity_glitter_bubblebutt_rose_kneeling",
]

ALL_KEYS = KSF_KEYS + MATERNITY_HOF_KEYS + MATERNITY_SSS_KEYS

# dict 형태로 삽입
insert = "\n" + "\n".join(
    f'    "{k}": {{"key": "{k}", "category": "🎨 Kintsugi Silver Fox"}},'
    if k.startswith("ksf_")
    else f'    "{k}": {{"key": "{k}", "category": "🤰 Maternity"}},'
    for k in ALL_KEYS
) + "\n"

src = src.rstrip()
src = re.sub(r'(\})\s*$', insert + r'\1', src)

with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(src)

# AST 검증
ast.parse(open(META_PATH, encoding="utf-8").read())
print("✅ presets_meta.py 수정 완료")
print(f"   총 {len(ALL_KEYS)}개 키 삽입")
