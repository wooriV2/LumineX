"""
patch_g5g6_remove_and_convert.py
G5/G6 미생성/탈락 프리셋 JSON 삭제 + duo_odalisque_gisaeng 생성 + dashboard.py 수정
실행: python preset_builders/patch_g5g6_remove_and_convert.py
"""

import json
import re
from pathlib import Path

BASE = Path("C:/Dev/LumineX")
PRESETS = BASE / "presets"
DASH = BASE / "dashboard.py"

# ============================================================
# STEP 1: 제거 대상 JSON 삭제 (12종)
# ============================================================

REMOVE = [
    "duo_lightning_rainbow_bodypaint.json",
    "duo_shark_whale_bodypaint.json",
    "duo_sistine_hands_bodypaint.json",
    "duo_map_east_west_bodypaint.json",
    "duo_shadow_light_figure_bodypaint.json",
    "trio_past_present_future_self_bodypaint.json",
    "trio_dawn_noon_dusk_bodypaint.json",
    "trio_earth_water_sky_bodypaint.json",
    "trio_neon_pastel_dark_bodypaint.json",
    "trio_predator_prey_scavenger_bodypaint.json",
    "trio_geisha_odalisque_gisaeng_bodypaint.json",
]

print("=== STEP 1: JSON 삭제 ===")
for f in REMOVE:
    p = PRESETS / f
    if p.exists():
        p.unlink()
        print(f"  삭제: {f}")
    else:
        print(f"  없음(스킵): {f}")

# ============================================================
# STEP 2: duo_odalisque_gisaeng JSON 생성
# ============================================================

print("\n=== STEP 2: duo_odalisque_gisaeng JSON 생성 ===")

new_preset = {
    "tag": "Duo Odalisque Gisaeng Bodypaint",
    "subject": "two cultural goddesses in split-world editorial, facing each other in elegant contrast",
    "body": "left figure — Mediterranean curves with Ottoman blue tilework bodypaint / right figure — East Asian grace with Korean plum blossom bodypaint",
    "outfit": "left model entire body painted in Ottoman odalisque style — Iznik blue tilework floral arabesques, cobalt and turquoise geometric medallions, gold filigree accents, barefoot, NO clothing NO fabric / right model entire body painted in Joseon gisaeng style — magnolia and plum blossom motifs in soft pink and white, dancheong color accents, Korean brushwork calligraphy on legs, barefoot, NO clothing NO fabric",
    "material": "bodypaint pigment directly on bare skin NOT clothing, both barefoot, cultural bodypaint aesthetic",
    "environment": "split composition — left Ottoman harem chamber with mosaic tile arches and amber lanterns / right Joseon pavilion with cherry blossom garden and moonlit paper screens",
    "lighting": "warm amber left side, cool moonlit blue right side, elegant cultural contrast lighting",
    "style": "surreal cultural contrast editorial, East-West bodypaint duo, Vogue Arabia meets Korean Vogue",
    "quality": "shot on Phase One XF IQ4, ultra-detailed cultural pattern bodypaint, portrait 2:3 vertical, 8K hyperrealistic"
}

out = PRESETS / "duo_odalisque_gisaeng_bodypaint.json"
with open(out, "w", encoding="utf-8") as f:
    json.dump(new_preset, f, ensure_ascii=False, indent=2)
print(f"  생성: duo_odalisque_gisaeng_bodypaint.json")

# ============================================================
# STEP 3: dashboard.py 수정
# ============================================================

print("\n=== STEP 3: dashboard.py 수정 ===")

content = DASH.read_text(encoding="utf-8")

# 제거 대상 키 목록 (따옴표 포함)
REMOVE_KEYS = [
    '"duo_lightning_rainbow_bodypaint"',
    '"duo_shark_whale_bodypaint"',
    '"duo_sistine_hands_bodypaint"',
    '"duo_map_east_west_bodypaint"',
    '"duo_shadow_light_figure_bodypaint"',
    '"trio_past_present_future_self_bodypaint"',
    '"trio_dawn_noon_dusk_bodypaint"',
    '"trio_earth_water_sky_bodypaint"',
    '"trio_neon_pastel_dark_bodypaint"',
    '"trio_predator_prey_scavenger_bodypaint"',
    '"trio_geisha_odalisque_gisaeng_bodypaint"',
]

for key in REMOVE_KEYS:
    clean = key.strip('"')
    before = content
    # 쉼표+줄바꿈 앞에 오는 경우
    content = re.sub(r'\s*' + re.escape(key) + r',?\s*\n', '\n', content)
    # 쉼표 뒤에 오는 경우 (줄 끝)
    content = re.sub(r',\s*' + re.escape(key), '', content)
    if content != before:
        print(f"  제거: {clean}")
    else:
        print(f"  미발견(스킵): {clean}")

# duo_odalisque_gisaeng을 PRESET_CATEGORIES에 추가
# 앵커: duo_ink_wash_split_bodypaint 다음에 삽입
anchor = '"duo_ink_wash_split_bodypaint"'
new_entry = '"duo_ink_wash_split_bodypaint",\n            "duo_odalisque_gisaeng_bodypaint"'

if anchor in content and "duo_odalisque_gisaeng_bodypaint" not in content:
    content = content.replace(anchor, new_entry)
    print("  추가: duo_odalisque_gisaeng_bodypaint → PRESET_CATEGORIES")
elif "duo_odalisque_gisaeng_bodypaint" in content:
    print("  이미 등록됨: duo_odalisque_gisaeng_bodypaint")
else:
    print("  !! 앵커 못찾음 — 수동 추가 필요")

DASH.write_text(content, encoding="utf-8")
print("  dashboard.py 저장 완료")

# ============================================================
# STEP 4: 검증
# ============================================================

print("\n=== STEP 4: 검증 ===")

content_check = DASH.read_text(encoding="utf-8")

print("  [제거 확인]")
for key in REMOVE_KEYS:
    clean = key.strip('"')
    if clean in content_check:
        print(f"  !! 잔존: {clean}")
    else:
        print(f"  OK 제거됨: {clean}")

print("  [신규 확인]")
if "duo_odalisque_gisaeng_bodypaint" in content_check:
    print("  OK dashboard.py 등록됨")
else:
    print("  !! dashboard.py 등록 실패")

if out.exists():
    print("  OK JSON 파일 존재")
else:
    print("  !! JSON 파일 없음")

print("\n=== 완료. 다음: git add -A && git commit && git push ===")
