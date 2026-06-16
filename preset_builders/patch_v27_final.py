"""
patch_v27_final.py
v27 최종 정리:
- 삭제 7개: wet_white_shirt, rain_bodysuit, professor_after_class,
            bartender_closing, pilot_uniform_edit, gym_mirror_pump, yoga_stretch_sheer
- SSS 2개: dressing_room_mirror, vip_booth_neon
- SS 8개: pool_edge_wet, ocean_wave_body, penthouse_bath, silk_sheets_morning,
          spa_private_steam, bar_counter_glam, after_party_suite, tennis_short_dress

실행: python preset_builders/patch_v27_final.py
"""

import json
import re
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")
DASHBOARD   = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 삭제 목록 ─────────────────────────────────────────────
DELETE = [
    "wet_white_shirt",
    "rain_bodysuit",
    "professor_after_class",
    "bartender_closing",
    "pilot_uniform_edit",
    "gym_mirror_pump",
    "yoga_stretch_sheer",
]

# ── tier 확정 목록 ─────────────────────────────────────────
NEW_SSS = [
    "dressing_room_mirror",
    "vip_booth_neon",
]

NEW_SS = [
    "pool_edge_wet",
    "ocean_wave_body",
    "penthouse_bath",
    "silk_sheets_morning",
    "spa_private_steam",
    "bar_counter_glam",
    "after_party_suite",
    "tennis_short_dress",
]

# ── 1. presets JSON 삭제 ───────────────────────────────────
print("=" * 50)
print("STEP 1: presets JSON 삭제")
print("=" * 50)
for name in DELETE:
    path = PRESETS_DIR / f"{name}.json"
    if path.exists():
        path.unlink()
        print(f"  🗑️  {name}.json 삭제")
    else:
        print(f"  ⚠️  {name}.json 없음 (이미 삭제됨)")

# ── 2. dashboard.py SSS_TIER / SS_TIER 추가 ──────────────
print("\n" + "=" * 50)
print("STEP 2: dashboard.py tier 패치")
print("=" * 50)

src = DASHBOARD.read_text(encoding="utf-8")

# SSS_TIER에 추가
SSS_BLOCK = "    # 2026-06-13 v27 핫&섹시 SSS 확정\n"
for p in NEW_SSS:
    SSS_BLOCK += f'    "{p}",\n'

src = re.sub(
    r'("palmyra_colonnade",\n)(\s*})',
    lambda m: m.group(1) + SSS_BLOCK + m.group(2),
    src, count=1
)

# SS_TIER에 추가 (SSS 포함 + 순수 SS)
SS_BLOCK = "    # 2026-06-13 v27 핫&섹시 SS/SSS 확정\n"
for p in NEW_SSS + NEW_SS:
    SS_BLOCK += f'    "{p}",\n'

src = re.sub(
    r'("gobekli_tepe",\n)(\s*})',
    lambda m: m.group(1) + SS_BLOCK + m.group(2),
    src, count=1
)

# dashboard.py 카테고리에서 삭제 항목 제거
for name in DELETE:
    src = re.sub(rf'\s*"{name}",\n', '\n', src)

DASHBOARD.write_text(src, encoding="utf-8")

print(f"\nSSS 추가 ({len(NEW_SSS)}개):")
for p in NEW_SSS:
    print(f"  + {p}")
print(f"\nSS 추가 ({len(NEW_SS)}개):")
for p in NEW_SS:
    print(f"  + {p}")
print(f"\n카테고리에서 삭제 ({len(DELETE)}개):")
for p in DELETE:
    print(f"  - {p}")

print("\n✅ 완료")
print("\n검증:")
print('  Select-String -Path dashboard.py -Pattern "dressing_room_mirror|vip_booth_neon|wet_white_shirt" | Select-Object LineNumber, Line')
