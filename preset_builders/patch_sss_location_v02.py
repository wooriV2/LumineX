"""
패치: 배경 프리셋 SSS/SS tier 전체 등록 (v02)
실행: python preset_builders/patch_sss_location_v02.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")
content = DASHBOARD.read_text(encoding="utf-8")

# SSS_TIER에 추가
OLD = '''    # 2026-06-11 배경 프리셋 SSS 확정
    "cenote_sacred",    # 물속 수직 덩굴 + 에메랄드 반사, 4장 일관성
    "tikal_skyrise",    # 정글 위 피라미드 + 운해 + 골든아워 역광
    "angkor_dawn",      # 연못 반사 + 황금 일출 + 크메르 조각, 구도 교과서급
    "waitomo_glow",     # 생물발광 은하수 천장 + 수면 반사, 독보적 비주얼
}'''

NEW = '''    # 2026-06-11 배경 프리셋 SSS 확정 (1차)
    "cenote_sacred",         # 물속 수직 덩굴 + 에메랄드 반사, 4장 일관성
    "tikal_skyrise",         # 정글 위 피라미드 + 운해 + 골든아워 역광
    "angkor_dawn",           # 연못 반사 + 황금 일출 + 크메르 조각, 구도 교과서급
    "waitomo_glow",          # 생물발광 은하수 천장 + 수면 반사, 독보적 비주얼
    # 2026-06-11 배경 프리셋 SSS 확정 (2차)
    "marble_caves_water",    # 대리석 패턴 + 터콰이즈 수면, 의상이 배경색 흡수
    "bagan_balloon",         # 열기구 + 황금 일출 + 불탑 평원, 4요소 완벽
    "tigers_nest_cliff",     # 절벽 수도원 + 기도 깃발 + 히말라야 설산
    "sheikh_zayed_dawn",     # 흰 돔 + 모자이크 바닥 + 반사 연못 + 블루아워
    "livraria_lello_staircase", # 테라코타 드레스 + 레드 계단 + 스테인드글라스 3중 동기화
    "namib_star_desert",     # 은하수 아치 + 사구 능선 + 백포즈 구도
    "ellora_rock_temple",    # 힌두 조각 벽 + 테라코타 드레스 완전 동화
}'''

content = content.replace(OLD, NEW, 1)

# SS_TIER에 나머지 SS 추가
OLD2 = '''    # 2026-06-11 배경 프리셋 SS 확정
    "son_doong_jungle", "petra_rose", "danxia_rainbow",
    "dead_vlei_ghost", "lake_natron",
    "angkor_dawn", "tikal_skyrise", "cenote_sacred", "waitomo_glow",
}'''

NEW2 = '''    # 2026-06-11 배경 프리셋 SS 확정
    "son_doong_jungle", "petra_rose", "danxia_rainbow",
    "dead_vlei_ghost", "lake_natron",
    "socotra_alien", "richat_eye", "derinkuyu_underground",
    "palacio_de_sal", "naoshima_art_island",
    # SSS도 SS에 포함 (format_preset 로직)
    "angkor_dawn", "tikal_skyrise", "cenote_sacred", "waitomo_glow",
    "marble_caves_water", "bagan_balloon", "tigers_nest_cliff",
    "sheikh_zayed_dawn", "livraria_lello_staircase",
    "namib_star_desert", "ellora_rock_temple",
}'''

content = content.replace(OLD2, NEW2, 1)

DASHBOARD.write_text(content, encoding="utf-8")
print("✅ 배경 프리셋 SSS/SS tier 전체 등록 완료!")
print()
print("SSS 확정 (11개):")
sss = [
    "cenote_sacred","tikal_skyrise","angkor_dawn","waitomo_glow",
    "marble_caves_water","bagan_balloon","tigers_nest_cliff",
    "sheikh_zayed_dawn","livraria_lello_staircase",
    "namib_star_desert","ellora_rock_temple",
]
for p in sss:
    print(f"  ⭐⭐⭐ {p}")
print()
print("SS 확정 (10개):")
ss = [
    "son_doong_jungle","petra_rose","danxia_rainbow",
    "dead_vlei_ghost","lake_natron","socotra_alien",
    "richat_eye","derinkuyu_underground","palacio_de_sal","naoshima_art_island",
]
for p in ss:
    print(f"  ⭐⭐ {p}")
