"""
patch_20260626_G3toG12.py
에로틱&페티쉬 G3~G12 51종 SSS + SS 패치
검증일: 2026-06-26
커밋: 2928572 이후 적용
"""

import re

TARGET = r"C:\Dev\LumineX\dashboard.py"

# ── G3~G12 신규 SSS 51종 ──
G3_to_G12_SSS = [
    # G3 하네스/본디지 7종
    "bondage_fashion", "strappy_harness", "harness_only", "rope_bondage_art",
    "suspension_art", "tape_bondage", "metal_bondage",
    # G4 메쉬/시스루 7종
    "mesh_bodysuit", "bodystocking", "fishnet_bodysuit", "transparent_dress",
    "sheer_catsuit", "catsuit_zipper", "pvc_transparent_full",
    # G5 도미나트릭스 5종
    "dominatrix_glam", "dominatrix_full_armor", "dominatrix_red",
    "goddess_throne", "pole_art",
    # G6 퍼포먼스/쇼걸 7종
    "burlesque", "showgirl", "cabaret_star", "candy_rave",
    "lap_dance_glam", "lap_dance_extreme", "striptease_art",
    # G7 폴/댄스/배스 4종
    "pole_dance_power", "pole_dance_extreme", "midnight_bath", "belly_dance_glam",
    # G8 판타지/다크 6종
    "dark_succubus", "vampire_seduction", "witch_sensual",
    "dark_fairy_erotic", "shadow_seductress", "succubus_full",
    # G9 다크앤젤/SF 3종
    "dark_angel_fallen", "alien_queen_body", "fire_goddess",
    # G10 직업 판타지 7종
    "secretary_after_hours", "nurse_sensual", "maid_sensual",
    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",
    # G11 바디/미니멀 3종 (body_paint_nude 제외 — 기검증)
    "oil_goddess", "micro_thong_only", "fetish_boots_only",
    # G12 코르셋 1종
    "corset_stockings",
]

SSS_ANCHOR = '"liquid_metal_body",'
SSS_INSERT = "\n\n    # 2026-06-26 에로틱&페티쉬 G3~G12 SSS 51종\n" + \
             "    # G3 하네스/본디지\n" + \
             '    "bondage_fashion", "strappy_harness", "harness_only", "rope_bondage_art",\n' + \
             '    "suspension_art", "tape_bondage", "metal_bondage",\n' + \
             "    # G4 메쉬/시스루\n" + \
             '    "mesh_bodysuit", "bodystocking", "fishnet_bodysuit", "transparent_dress",\n' + \
             '    "sheer_catsuit", "catsuit_zipper", "pvc_transparent_full",\n' + \
             "    # G5 도미나트릭스\n" + \
             '    "dominatrix_glam", "dominatrix_full_armor", "dominatrix_red",\n' + \
             '    "goddess_throne", "pole_art",\n' + \
             "    # G6 퍼포먼스/쇼걸\n" + \
             '    "burlesque", "showgirl", "cabaret_star", "candy_rave",\n' + \
             '    "lap_dance_glam", "lap_dance_extreme", "striptease_art",\n' + \
             "    # G7 폴/댄스/배스\n" + \
             '    "pole_dance_power", "pole_dance_extreme", "midnight_bath", "belly_dance_glam",\n' + \
             "    # G8 판타지/다크\n" + \
             '    "dark_succubus", "vampire_seduction", "witch_sensual",\n' + \
             '    "dark_fairy_erotic", "shadow_seductress", "succubus_full",\n' + \
             "    # G9 다크앤젤/SF\n" + \
             '    "dark_angel_fallen", "alien_queen_body", "fire_goddess",\n' + \
             "    # G10 직업 판타지\n" + \
             '    "secretary_after_hours", "nurse_sensual", "maid_sensual",\n' + \
             '    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",\n' + \
             "    # G11 바디/미니멀\n" + \
             '    "oil_goddess", "micro_thong_only", "fetish_boots_only",\n' + \
             "    # G12 코르셋\n" + \
             '    "corset_stockings",'

SS_ANCHOR = '"liquid_metal_body",'
# SS_TIER에도 동일 51종 추가 (SSS는 SS에도 포함 규칙)
SS_INSERT = "\n\n    # 2026-06-26 에로틱&페티쉬 G3~G12 SS (SSS 포함 51종)\n" + \
            '    "bondage_fashion", "strappy_harness", "harness_only", "rope_bondage_art",\n' + \
            '    "suspension_art", "tape_bondage", "metal_bondage",\n' + \
            '    "mesh_bodysuit", "bodystocking", "fishnet_bodysuit", "transparent_dress",\n' + \
            '    "sheer_catsuit", "catsuit_zipper", "pvc_transparent_full",\n' + \
            '    "dominatrix_glam", "dominatrix_full_armor", "dominatrix_red",\n' + \
            '    "goddess_throne", "pole_art",\n' + \
            '    "burlesque", "showgirl", "cabaret_star", "candy_rave",\n' + \
            '    "lap_dance_glam", "lap_dance_extreme", "striptease_art",\n' + \
            '    "pole_dance_power", "pole_dance_extreme", "midnight_bath", "belly_dance_glam",\n' + \
            '    "dark_succubus", "vampire_seduction", "witch_sensual",\n' + \
            '    "dark_fairy_erotic", "shadow_seductress", "succubus_full",\n' + \
            '    "dark_angel_fallen", "alien_queen_body", "fire_goddess",\n' + \
            '    "secretary_after_hours", "nurse_sensual", "maid_sensual",\n' + \
            '    "teacher_after_class", "doctor_sensual", "police_dominatrix", "stewardess_dark",\n' + \
            '    "oil_goddess", "micro_thong_only", "fetish_boots_only",\n' + \
            '    "corset_stockings",'


def patch():
    with open(TARGET, "r", encoding="utf-8") as f:
        src = f.read()

    # ── SSS_TIER 패치 ──
    # SSS_TIER 블록 안의 G2 마지막 "liquid_metal_body", 뒤에 삽입
    # SSS_TIER 블록은 SS_TIER보다 먼저 나옴 → 첫 번째 occurrence만 교체
    sss_old = '"liquid_metal_body",\n\n\n    # 2026-06-24 판타지&다크'
    sss_new = '"liquid_metal_body",' + SSS_INSERT + "\n\n\n    # 2026-06-24 판타지&다크"

    if sss_old in src:
        src = src.replace(sss_old, sss_new, 1)
        print("✅ SSS_TIER 패치 완료")
    else:
        print("⚠️ SSS_TIER 앵커 미발견 — 수동 확인 필요")
        print("   찾는 문자열:", repr(sss_old[:60]))

    # ── SS_TIER 패치 ──
    ss_old = '"liquid_metal_body",\n\n\n    # 2026-06-24 판타지&다크'
    ss_new = '"liquid_metal_body",' + SS_INSERT + "\n\n\n    # 2026-06-24 판타지&다크"

    # SS_TIER는 SSS_TIER 이후에 나오는 두 번째 블록
    # SSS_TIER 패치 후 src에서 두 번째 "liquid_metal_body", 를 찾아야 함
    # 단순하게: SS_TIER = { 이후 영역에서 replace
    ss_block_start = src.find("SS_TIER = {")
    if ss_block_start == -1:
        print("⚠️ SS_TIER 블록 미발견")
        return

    ss_section = src[ss_block_start:]

    ss_anchor_in_ss = '"liquid_metal_body",\n\n\n    # 2026-06-24 판타지&다크'
    if ss_anchor_in_ss in ss_section:
        ss_section_new = ss_section.replace(ss_anchor_in_ss,
            '"liquid_metal_body",' + SS_INSERT + "\n\n\n    # 2026-06-24 판타지&다크", 1)
        src = src[:ss_block_start] + ss_section_new
        print("✅ SS_TIER 패치 완료")
    else:
        print("⚠️ SS_TIER 앵커 미발견")

    with open(TARGET, "w", encoding="utf-8") as f:
        f.write(src)
    print(f"\n📝 저장 완료: {TARGET}")
    print(f"   SSS 추가: {len(G3_to_G12_SSS)}종")


if __name__ == "__main__":
    patch()
