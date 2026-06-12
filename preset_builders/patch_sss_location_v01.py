"""
패치: 배경 프리셋 SSS/SS tier 등록
실행: python preset_builders/patch_sss_location_v01.py
"""
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")
content = DASHBOARD.read_text(encoding="utf-8")

# SSS_TIER에 4개 추가
OLD = 'SSS_TIER = {\n    "body_paint_nude",\n}'

NEW = '''SSS_TIER = {
    "body_paint_nude",
    # 2026-06-11 배경 프리셋 SSS 확정
    "cenote_sacred",    # 물속 수직 덩굴 + 에메랄드 반사, 4장 일관성
    "tikal_skyrise",    # 정글 위 피라미드 + 운해 + 골든아워 역광
    "angkor_dawn",      # 연못 반사 + 황금 일출 + 크메르 조각, 구도 교과서급
    "waitomo_glow",     # 생물발광 은하수 천장 + 수면 반사, 독보적 비주얼
}'''

content = content.replace(OLD, NEW, 1)

# SS_TIER에 배경 프리셋 추가
OLD2 = '    "lava_field_latex",\n}'

NEW2 = '''    "lava_field_latex",
    # 2026-06-11 배경 프리셋 SS 확정
    "son_doong_jungle", "petra_rose", "danxia_rainbow",
    "dead_vlei_ghost", "lake_natron",
    "angkor_dawn", "tikal_skyrise", "cenote_sacred", "waitomo_glow",
}'''

content = content.replace(OLD2, NEW2, 1)

DASHBOARD.write_text(content, encoding="utf-8")
print("✅ SSS/SS tier 등록 완료!")
print()
print("SSS 추가 (4개): cenote_sacred, tikal_skyrise, angkor_dawn, waitomo_glow")
print("SS  추가 (5개): son_doong_jungle, petra_rose, danxia_rainbow, dead_vlei_ghost, lake_natron")
print("(SS에 SSS 4개도 중복 등록 — dashboard format_preset 로직상 SSS 우선 표시)")
