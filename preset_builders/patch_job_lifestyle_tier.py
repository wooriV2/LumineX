"""
직업&라이프스타일 tier 패치 스크립트
SSS 24종 / SS 10종 (SS에는 SSS도 포함)
앵커: SSS_TIER = { 와 SS_TIER = { 바로 뒤에 삽입
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

SSS_BLOCK = '''
    # 2026-06-20 직업&라이프스타일 SSS 24종 확정
    # A그룹 — 항공/해양/럭셔리
    "flight_attendant", "pilot_glamour", "yacht_captain",
    "private_jet", "helipad", "hotel_concierge",
    # B그룹 — 전문직
    "lawyer_power", "architect_chic", "casino_dealer", "gallery_curator",
    # C그룹 — 스포츠/피트니스
    "golf_glam", "tennis_luxe", "tennis_referee", "tennis_champion",
    "f1_grid_girl", "equestrian_glam", "horse_racing", "yoga_goddess",
    # D그룹 — 퍼포먼스/스포츠2
    "cheerleader", "ballet_prima", "gymnastics_editorial",
    "figure_skater", "carnival_rio", "luxury_shopping",
'''

SS_BLOCK = '''
    # 2026-06-20 직업&라이프스타일 SS전용 10종 + SSS 24종 포함
    # SS전용
    "cruise_hostess", "yacht_club",
    "nurse_glamour", "sommelier", "wine_tasting", "barista_chic",
    "golf_caddie", "fitness_power", "scuba_instructor", "archery_goddess",
    # SSS도 SS에 포함 (규칙)
    "flight_attendant", "pilot_glamour", "yacht_captain",
    "private_jet", "helipad", "hotel_concierge",
    "lawyer_power", "architect_chic", "casino_dealer", "gallery_curator",
    "golf_glam", "tennis_luxe", "tennis_referee", "tennis_champion",
    "f1_grid_girl", "equestrian_glam", "horse_racing", "yoga_goddess",
    "cheerleader", "ballet_prima", "gymnastics_editorial",
    "figure_skater", "carnival_rio", "luxury_shopping",
'''

with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

# SSS_TIER 앵커 삽입
SSS_ANCHOR = "SSS_TIER = {"
if SSS_ANCHOR not in content:
    print("[ERROR] SSS_TIER 앵커 없음"); exit(1)
content = content.replace(SSS_ANCHOR, SSS_ANCHOR + SSS_BLOCK, 1)
print("[OK] SSS_TIER 24종 삽입")

# SS_TIER 앵커 삽입
SS_ANCHOR = "SS_TIER = {"
if SS_ANCHOR not in content:
    print("[ERROR] SS_TIER 앵커 없음"); exit(1)
content = content.replace(SS_ANCHOR, SS_ANCHOR + SS_BLOCK, 1)
print("[OK] SS_TIER 34종 삽입")

with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
    f.write(content)

print("\n[완료] dashboard.py 패치 성공")
