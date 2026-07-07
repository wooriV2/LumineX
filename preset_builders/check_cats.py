# -*- coding: utf-8 -*-
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from core.presets_meta import PRESET_CATEGORIES
new_p = ['club_vip_neon_goddess','club_rooftop_citylight','micro_sequin_club','rooftop_micro_night','silk_slip_dawn_hotel','satin_slip_vanity_noir','satin_slip_micro','leopard_power_editorial','leopard_micro_studio','snake_micro_marble','snakeskin_latex_glam']
kw = ['도시','나이트','핫','섹시','에로틱','페티쉬','럭셔리']
all_p = [p for v in PRESET_CATEGORIES.values() for p in v]
print('=== 신규 중복 체크 ===')
for p in new_p:
    print('중복' if p in all_p else '신규', p)
print()
print('=== 유사 카테고리 ===')
for cat, presets in PRESET_CATEGORIES.items():
    if any(k in cat for k in kw):
        print(cat, len(presets))
        for p in presets: print(' ', p)
        print()
