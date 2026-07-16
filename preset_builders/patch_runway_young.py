# -*- coding: utf-8 -*-
HOF_NEW = [
    "runway_korean_slim_milan_catwalk",
    "runway_korean_slim_tokyo_shibuya_rain",
    "runway_korean_slim_amalfi_cliff",
    "runway_korean_slim_bali_temple_gold",
    "runway_korean_slim_kyoto_autumn",
    "runway_korean_slim_aurora_finland",
    "runway_korean_slim_sahara_wind",
    "runway_korean_slim_crystal_gala",
    "young_korean_midnight_rooftop_seoul",
    "young_korean_debut_red_carpet",
]
SSS_NEW = [
    "runway_korean_slim_void_studio",
    "runway_korean_slim_paris_window",
    "runway_korean_slim_dubai_penthouse",
    "runway_korean_slim_nyc_rooftop",
    "runway_korean_slim_icelandic_glacier",
    "runway_korean_slim_berlin_underground",
    "runway_korean_slim_palawan_karst",
    "runway_korean_slim_seychelles_granite",
    "runway_korean_slim_tattoo_collarbone_void",
    "runway_korean_slim_newyork_snowstorm",
    "young_korean_jeju_sunrise",
    "young_korean_studio_black_minimal",
    "young_korean_maldives_first_trip",
    "young_korean_paris_first_europe",
    "young_korean_summer_busan",
    "young_korean_tattoo_ankle_jeju",
    "young_korean_nyc_first_american",
    "young_korean_tattoo_shoulder_okinawa",
    "young_korean_cherry_blossom",
    "young_korean_bali_first_solo",
    "young_korean_21_birthday_gold",
]
SS_NEW = [
    "runway_korean_slim_seoulforest_spring",
    "young_korean_pool_pastel",
    "young_korean_neon_first_night",
    "young_korean_tokyo_first_solo",
    "young_korean_tattoo_first_wrist",
    "young_korean_gym_first_gains",
    "young_korean_campus_spring",
]

with open('core/hof_tier.py', 'r', encoding='utf-8') as f:
    hof_content = f.read()

hof_lines = '\n'.join(f'    "{k}",' for k in HOF_NEW)
insert_block = f'\n    # 2026-07-16 Runway Slim + Young Adult HOF\n{hof_lines}\n'
hof_content = hof_content.replace('\ndef add_hof', insert_block + '\ndef add_hof')

with open('core/hof_tier.py', 'w', encoding='utf-8') as f:
    f.write(hof_content)
print(f"hof_tier.py 패치 완료: {len(HOF_NEW)}종")

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

sss_anchor = '# 2026-07-15 한국인 카테고리 신규 SSS'
sss_lines = '\n'.join(f'    "{k}",' for k in SSS_NEW)
sss_insert = f'    # 2026-07-16 Runway Slim + Young Adult SSS\n{sss_lines}\n\n'
content = content.replace(sss_anchor, sss_insert + sss_anchor)

ss_anchor = '# 2026-07-15 한국인 카테고리 신규 SS'
ss_lines = '\n'.join(f'    "{k}",' for k in SS_NEW)
ss_insert = f'    # 2026-07-16 Runway Slim + Young Adult SS\n{ss_lines}\n\n'
content = content.replace(ss_anchor, ss_insert + ss_anchor)

with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
    f.write(content)
print(f"presets_meta.py SSS {len(SSS_NEW)}종, SS {len(SS_NEW)}종 패치 완료")

import ast
with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    source = f.read()
try:
    ast.parse(source)
    print("문법 검사 OK!")
except SyntaxError as e:
    print(f"SyntaxError: {e.lineno} - {e.msg}")
    print(repr(e.text))
