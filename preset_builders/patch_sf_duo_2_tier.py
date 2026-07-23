"""
SF_Duo tier + presets_meta 패치 스크립트
저장 위치: C:\Dev\LumineX\preset_builders\patch_sf_duo_2_tier.py
실행: python preset_builders\patch_sf_duo_2_tier.py
"""

import re
import ast

# ============================================================
# HOF 키 목록 (27개)
# ============================================================
HOF_KEYS = [
    "sf_duo_lion_queen",
    "sf_duo_panther_goddess",
    "sf_duo_eagle_empress",
    "sf_duo_wolf_moon_goddess",
    "sf_duo_solar_mandala",
    "sf_duo_dragon_pearl",
    "sf_duo_phoenix_rising",
    "sf_duo_sakura_storm",
    "sf_duo_celtic_fire",
    "sf_duo_samurai_rose",
    "sf_duo_amazon_thunder",
    "sf_duo_silk_road",
    "sf_duo_ottoman_rose",
    "sf_duo_persian_fire",
    "sf_duo_hanbok_queen",
    "sf_duo_inuit_aurora",
    "sf_duo_aztec_moon",
    "sf_duo_bengal_tiger",
    "sf_duo_venetian_mask",
    "sf_duo_cambodian_apsara",
    "sf_duo_flamenco_fire",
    "sf_duo_balinese_goddess",
    "sf_duo_aztec_jaguar",
    "sf_duo_pharaoh_queen",
    "sf_duo_amazon_queen",
    "sf_duo_siberian_wolf",
    "sf_duo_aztec_eagle",
]

# ============================================================
# SSS 키 목록 (8개)
# ============================================================
SSS_KEYS = [
    "sf_duo_cobra_empress",
    "sf_duo_geisha_moon",
    "sf_duo_mughal_empress",
    "sf_duo_northern_star",
    "sf_duo_nile_goddess",
    "sf_duo_yoruba_goddess",
    "sf_duo_georgian_vine",
    "sf_duo_zulu_lion",
]

# ============================================================
# 1. hof_tier.py 패치
# ============================================================
HOF_FILE = "core/hof_tier.py"

with open(HOF_FILE, encoding="utf-8-sig") as f:
    hof_content = f.read()

hof_insert = "\n".join(f'    "{k}",' for k in HOF_KEYS)
hof_content = hof_content.rstrip()

# 마지막 } 앞에 삽입
if hof_content.endswith("}"):
    hof_content = hof_content[:-1].rstrip() + "\n\n    # 🦁 Silver Fox DUO HOF\n" + hof_insert + "\n}"
else:
    raise ValueError("hof_tier.py 마지막 문자가 }가 아닙니다!")

with open(HOF_FILE, "w", encoding="utf-8") as f:
    f.write(hof_content)

print("✅ hof_tier.py 패치 완료")

# ============================================================
# 2. sss_tier.py 패치
# ============================================================
SSS_FILE = "core/sss_tier.py"

with open(SSS_FILE, encoding="utf-8-sig") as f:
    sss_content = f.read()

sss_insert = "\n".join(f'    "{k}",' for k in SSS_KEYS)
sss_content = sss_content.rstrip()

if sss_content.endswith("}"):
    sss_content = sss_content[:-1].rstrip() + "\n\n    # 🦁 Silver Fox DUO SSS\n" + sss_insert + "\n}"
else:
    raise ValueError("sss_tier.py 마지막 문자가 }가 아닙니다!")

with open(SSS_FILE, "w", encoding="utf-8") as f:
    f.write(sss_content)

print("✅ sss_tier.py 패치 완료")

# ============================================================
# 3. presets_meta.py 패치 — 카테고리 추가
# ============================================================
META_FILE = "core/presets_meta.py"

with open(META_FILE, encoding="utf-8-sig") as f:
    meta_content = f.read()

ALL_KEYS = HOF_KEYS + SSS_KEYS

category_entry = '''
    "🦁 Silver Fox DUO": [
''' + "\n".join(f'        "{k}",' for k in ALL_KEYS) + '''
    ],'''

# PRESET_CATEGORIES 딕셔너리 마지막 } 앞에 삽입
insert_anchor = "}\n"
last_idx = meta_content.rfind(insert_anchor)

if last_idx == -1:
    raise ValueError("presets_meta.py에서 삽입 위치를 찾을 수 없습니다!")

meta_content = (
    meta_content[:last_idx]
    + category_entry
    + "\n"
    + meta_content[last_idx:]
)

with open(META_FILE, "w", encoding="utf-8") as f:
    f.write(meta_content)

print("✅ presets_meta.py 패치 완료")

# ============================================================
# 4. AST 검증
# ============================================================
for filepath in [HOF_FILE, SSS_FILE, META_FILE]:
    with open(filepath, encoding="utf-8") as f:
        source = f.read()
    try:
        ast.parse(source)
        print(f"✅ AST OK: {filepath}")
    except SyntaxError as e:
        print(f"❌ AST FAIL: {filepath} — {e}")

print("\n🎉 패치 완료!")
print(f"   HOF 추가: {len(HOF_KEYS)}개")
print(f"   SSS 추가: {len(SSS_KEYS)}개")
print(f"   카테고리: 🦁 Silver Fox DUO")
