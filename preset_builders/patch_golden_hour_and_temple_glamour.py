# -*- coding: utf-8 -*-
# patch_golden_hour_and_temple_glamour.py
# 저장 위치: C:\Dev\LumineX\preset_builders\patch_golden_hour_and_temple_glamour.py

target = r'C:\Dev\LumineX\core\presets_meta.py'
hof_target = r'C:\Dev\LumineX\core\hof_tier.py'

# ── 새 카테고리 2종 ─────────────────────────────────────────────

NEW_CATEGORIES = '''    "🌅 Golden Hour Glamour": [
        "golden_hour_cliff_goddess",
        "golden_hour_salt_flat_goddess",
        "golden_hour_dune_goddess",
        "golden_hour_wheat_field",
        "golden_hour_iceland_waterfall",
        "golden_hour_lavender_field",
        "golden_hour_amazon_cliff",
        "golden_hour_curvy_desert",
        "golden_hour_latina_wheat",
        "golden_hour_bust_salt_flat",
        "golden_hour_pear_tulip_field",
        "golden_hour_petite_iceland",
        "golden_hour_hourglass_volcano",
    ],

    "🏛️ Ancient Temple Glamour": [
        "marble_awakening_goddess",
        "karnak_gold_fusion",
        "angkor_relief_emergence",
        "petra_sandstone_dissolve",
        "ephesus_marble_split",
        "chichen_itza_serpent_merge",
        "nefertiti_gold_petrify",
    ],'''

# ── HOF 추가 20종 ───────────────────────────────────────────────

NEW_HOF = '''    # ── 🌅 Golden Hour Glamour HOF 13종 ────────────────────────
    "golden_hour_cliff_goddess",
    "golden_hour_salt_flat_goddess",
    "golden_hour_dune_goddess",
    "golden_hour_wheat_field",
    "golden_hour_iceland_waterfall",
    "golden_hour_lavender_field",
    "golden_hour_amazon_cliff",
    "golden_hour_curvy_desert",
    "golden_hour_latina_wheat",
    "golden_hour_bust_salt_flat",
    "golden_hour_pear_tulip_field",
    "golden_hour_petite_iceland",
    "golden_hour_hourglass_volcano",
    # ── 🏛️ Ancient Temple Glamour HOF 7종 ─────────────────────
    "marble_awakening_goddess",
    "karnak_gold_fusion",
    "angkor_relief_emergence",
    "petra_sandstone_dissolve",
    "ephesus_marble_split",
    "chichen_itza_serpent_merge",
    "nefertiti_gold_petrify",'''

# ── presets_meta.py 패치 ────────────────────────────────────────

with open(target, 'r', encoding='utf-8') as f:
    content = f.read()

anchor = '"💎 Figure Glamour": ['
content = content.replace(anchor, NEW_CATEGORIES + '\n\n    ' + anchor)

with open(target, 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ presets_meta.py 카테고리 2종 추가 완료")

# ── hof_tier.py 패치 ────────────────────────────────────────────

with open(hof_target, 'r', encoding='utf-8') as f:
    hof_content = f.read()

hof_anchor = '    # ── 💎 Figure Glamour HOF 37종'
hof_content = hof_content.replace(hof_anchor, NEW_HOF + '\n\n' + hof_anchor)

with open(hof_target, 'w', encoding='utf-8') as f:
    f.write(hof_content)

print("✅ hof_tier.py HOF 20종 추가 완료")
print("총 HOF: 200 → 220종")

# ── 검증 ────────────────────────────────────────────────────────

print("\n검증 명령어:")
print('Select-String -Path "C:\\Dev\\LumineX\\core\\hof_tier.py" -Pattern "golden_hour_cliff_goddess"')
print('Select-String -Path "C:\\Dev\\LumineX\\core\\hof_tier.py" -Pattern "marble_awakening_goddess"')
print('Select-String -Path "C:\\Dev\\LumineX\\core\\presets_meta.py" -Pattern "Golden Hour Glamour"')
print('Select-String -Path "C:\\Dev\\LumineX\\core\\presets_meta.py" -Pattern "Ancient Temple Glamour"')
