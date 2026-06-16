"""
patch_dashboard_v27.py
dashboard.py 🔥 핫 & 섹시 카테고리에 v27 프리셋 17개 추가

실행: python preset_builders/patch_dashboard_v27.py
"""

from pathlib import Path
import re

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

NEW_PRESETS = [
    # 웻 & 바디
    "wet_white_shirt",
    "rain_bodysuit",
    "pool_edge_wet",
    "ocean_wave_body",
    # 인테리어 섹시
    "penthouse_bath",
    "dressing_room_mirror",
    "silk_sheets_morning",
    "spa_private_steam",
    # 나이트라이프
    "bar_counter_glam",
    "vip_booth_neon",
    "after_party_suite",
    # 직업 섹시
    "professor_after_class",
    "bartender_closing",
    "pilot_uniform_edit",
    # 스포츠 섹시
    "gym_mirror_pump",
    "yoga_stretch_sheer",
    "tennis_short_dress",
]

src = DASHBOARD.read_text(encoding="utf-8")

# 🔥 핫 & 섹시 카테고리 마지막 항목 "wet_editorial" 뒤에 삽입
INSERT_COMMENT = "        # v27 — 핫 & 섹시 신규 17개\n"
INSERT_LINES = INSERT_COMMENT
for p in NEW_PRESETS:
    INSERT_LINES += f'        "{p}",\n'

src = re.sub(
    r'("wet_editorial",\n)(\s+\],)',
    lambda m: m.group(1) + INSERT_LINES + m.group(2),
    src,
    count=1
)

DASHBOARD.write_text(src, encoding="utf-8")

print("=" * 50)
print("LumineX v27 — dashboard.py 패치")
print("=" * 50)
print(f"\n🔥 핫 & 섹시에 추가 ({len(NEW_PRESETS)}개):")
for p in NEW_PRESETS:
    print(f"  + {p}")
print("\n✅ 완료")
print("\n검증:")
print('  Select-String -Path dashboard.py -Pattern "wet_white_shirt|penthouse_bath|gym_mirror_pump" | Select-Object LineNumber, Line')
