with open('core/hof_tier.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '}\n\n\n\n\n\n    # 2026-07-16 Runway Slim + Young Adult HOF\n'
new = '\n    # 2026-07-16 Runway Slim + Young Adult HOF\n'

# } 안으로 이동 - beach_powerlifter_seychelles 다음에 삽입
old2 = '    "beach_powerlifter_seychelles",\n}\n'
new2 = '''    "beach_powerlifter_seychelles",\n    # 2026-07-16 Runway Slim + Young Adult HOF\n    "runway_korean_slim_milan_catwalk",\n    "runway_korean_slim_tokyo_shibuya_rain",\n    "runway_korean_slim_amalfi_cliff",\n    "runway_korean_slim_bali_temple_gold",\n    "runway_korean_slim_kyoto_autumn",\n    "runway_korean_slim_aurora_finland",\n    "runway_korean_slim_sahara_wind",\n    "runway_korean_slim_crystal_gala",\n    "young_korean_midnight_rooftop_seoul",\n    "young_korean_debut_red_carpet",\n}\n'''

content = content.replace(old, '')
content = content.replace(old2, new2)

with open('core/hof_tier.py', 'w', encoding='utf-8') as f:
    f.write(content)
print('수정 완료!')
