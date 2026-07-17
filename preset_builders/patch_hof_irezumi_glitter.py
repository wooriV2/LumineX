# -*- coding: utf-8 -*-
"""
HOF 패치: 이레즈미 14종 + 바디글리터 11종
총 25종 HOF 추가
"""

HOF_KEYS = [
    # 이레즈미 - 용+파도
    "irezumi_dragon_wave_black_glam_void",
    "irezumi_dragon_wave_sports_glam_onsen",
    "irezumi_dragon_wave_power_fitness_strobe",
    "irezumi_dragon_wave_vs_angel_santorini",
    "irezumi_dragon_wave_slim_runway_neon",
    # 이레즈미 - 봉황+국화
    "irezumi_phoenix_chrysanthemum_ballerina_steam",
    "irezumi_phoenix_chrysanthemum_hot_glam_riad",
    "irezumi_phoenix_chrysanthemum_black_glam_desert",
    # 이레즈미 - 잉어+벚꽃
    "irezumi_koi_sakura_vs_angel_kyoto_rain",
    "irezumi_koi_sakura_colombian_monaco",
    # 이레즈미 - 학+모란
    "irezumi_crane_peony_super_glam_versailles",
    # 이레즈미 - 호랑이+대나무
    "irezumi_tiger_bamboo_sports_glam_void",
    "irezumi_tiger_bamboo_vs_angel_dubai",
    "irezumi_tiger_bamboo_african_desert",
    # 바디글리터
    "bodyglitter_silver_neon_cyberpunk",
    "bodyglitter_gold_void_black_glam",
    "bodyglitter_rose_gold_versailles",
    "bodyglitter_blue_holographic_pool",
    "bodyglitter_silver_onsen_steam",
    "bodyglitter_rainbow_aurora_nordic",
    "bodyglitter_emerald_dubai_rooftop",
    "bodyglitter_copper_santorini_sunset",
    "bodyglitter_purple_monaco_night",
    "bodyglitter_red_void_colombian",
    "bodyglitter_ice_blue_void_ballerina",
]

with open('core/hof_tier.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 새 키들을 문자열로 조합
new_keys = ""
for key in HOF_KEYS:
    if f'"{key}"' not in content:
        new_keys += f'    "{key}",\n'

if not new_keys:
    print("이미 모든 키가 존재합니다.")
else:
    # 앵커: def add_hof 바로 앞의 } 닫힘
    anchor = '}\n\ndef add_hof'
    if anchor not in content:
        print("앵커를 찾을 수 없습니다. hof_tier.py 구조를 확인하세요.")
    else:
        new_content = content.replace(
            anchor,
            new_keys + anchor
        )
        with open('core/hof_tier.py', 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"완료: {len(HOF_KEYS)}종 HOF 추가")
        for key in HOF_KEYS:
            print(f"  + {key}")
