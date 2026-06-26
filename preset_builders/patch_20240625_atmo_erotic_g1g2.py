"""
패치: 대기&파티클 30종 + 에로틱&페티쉬 G1/G2 검증 결과 반영
날짜: 2026-06-25
커밋 대상: dashboard.py

[대기&파티클 30종 — 전원 SSS]
G1 스모크/연기 6종: smoke_machine_club, dry_ice_floor, cigarette_smoke_noir,
                    incense_smoke_ritual, smoke_color_holi, fog_forest_mystery
G2 파우더/더스트 5종: gold_dust_pour, holi_powder_explosion, chalk_dust_sport,
                    flour_dust_studio, pigment_powder_art
G3 페더/페탈 5종:  feather_explosion, black_feather_dark, petal_storm_indoor,
                    cherry_blossom_burst, dried_flower_cascade
G4 글리터/파티클 5종: glitter_rain_studio, gold_confetti_burst, silver_glitter_body,
                    neon_particle_club, bubble_floating_studio
G5 불/스파크 4종:  sparkler_night_glam, fire_poi_dance, ember_glow_dark, firework_silhouette
G6 자연 파티클 5종: autumn_leaves_burst, snow_indoor_studio, dandelion_blow,
                    firefly_night_field, seed_pod_floating

[에로틱&페티쉬 G1 라텍스/PVC/비닐 — SSS 8 / SS 1]
SSS: latex_venom, latex_catsuit, latex_catsuit_red, pvc_transparent_full,
     latex_hood_full, latex_transparent, vinyl_goddess, rubber_goddess
SS전용: wet_latex

[에로틱&페티쉬 G2 가죽/체인/메탈 — 전원 SSS]
SSS: chrome_vixen, chain_goddess, savage_leather, leather_bodysuit,
     chrome_bodysuit, mirror_dress, liquid_metal_body
"""

import re

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ── 추가할 SSS 프리셋 목록 ──────────────────────────────────
NEW_SSS = [
    # 대기&파티클 G1
    "smoke_machine_club", "dry_ice_floor", "cigarette_smoke_noir",
    "incense_smoke_ritual", "smoke_color_holi", "fog_forest_mystery",
    # 대기&파티클 G2
    "gold_dust_pour", "holi_powder_explosion", "chalk_dust_sport",
    "flour_dust_studio", "pigment_powder_art",
    # 대기&파티클 G3
    "feather_explosion", "black_feather_dark", "petal_storm_indoor",
    "cherry_blossom_burst", "dried_flower_cascade",
    # 대기&파티클 G4
    "glitter_rain_studio", "gold_confetti_burst", "silver_glitter_body",
    "neon_particle_club", "bubble_floating_studio",
    # 대기&파티클 G5
    "sparkler_night_glam", "fire_poi_dance", "ember_glow_dark", "firework_silhouette",
    # 대기&파티클 G6
    "autumn_leaves_burst", "snow_indoor_studio", "dandelion_blow",
    "firefly_night_field", "seed_pod_floating",
    # 에로틱&페티쉬 G1 SSS
    "latex_venom", "latex_catsuit", "latex_catsuit_red", "pvc_transparent_full",
    "latex_hood_full", "latex_transparent", "vinyl_goddess", "rubber_goddess",
    # 에로틱&페티쉬 G2 전원 SSS
    "chrome_vixen", "chain_goddess", "savage_leather", "leather_bodysuit",
    "chrome_bodysuit", "mirror_dress", "liquid_metal_body",
]

# SS 전용 (SSS 아님, SS_TIER에만 추가)
NEW_SS_ONLY = [
    "wet_latex",
]

def patch_tier_set(content, set_name, new_items):
    """set_name = 'SSS_TIER' or 'SS_TIER' 마지막 항목 뒤에 새 항목 추가"""
    # 앵커: 해당 set의 마지막 닫는 } 직전 라인을 찾아 삽입
    # 전략: 마지막으로 등장하는 "}" 직전에 삽입
    # set 정의 블록을 찾아 closing } 바로 앞에 삽입

    # 이미 존재하는 항목 필터링
    already = [item for item in new_items if f'"{item}"' in content]
    to_add = [item for item in new_items if f'"{item}"' not in content]

    if already:
        print(f"[{set_name}] 이미 존재 (스킵): {already}")
    if not to_add:
        print(f"[{set_name}] 추가할 항목 없음")
        return content

    # 앵커 문자열: 해당 set 블록의 마지막 항목 근처
    # SSS_TIER 블록의 닫는 } 찾기
    # 패턴: set_name = { ... } 구조에서 마지막 } 직전에 삽입
    pattern = rf'({set_name}\s*=\s*\{{[^}}]*?)(\n\}}\s*\n# SS tier|\n\}}\s*\n\n#)'
    
    insert_lines = "\n    # 2026-06-25 대기&파티클 + 에로틱&페티쉬 G1/G2 패치\n"
    for item in to_add:
        insert_lines += f'    "{item}",\n'

    def replacer(m):
        return m.group(1) + insert_lines + m.group(2)

    new_content = re.sub(pattern, replacer, content, flags=re.DOTALL)
    if new_content == content:
        print(f"[{set_name}] 패턴 매칭 실패 — 수동 확인 필요")
    else:
        print(f"[{set_name}] 추가 완료: {to_add}")
    return new_content


def main():
    with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. SSS_TIER에 추가
    content = patch_tier_set(content, "SSS_TIER", NEW_SSS)

    # 2. SS_TIER에 SSS + SS전용 모두 추가 (format_preset 로직: SSS도 SS에 포함)
    content = patch_tier_set(content, "SS_TIER", NEW_SSS + NEW_SS_ONLY)

    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)

    print("\n✅ 패치 완료")
    print(f"   SSS 추가: {len(NEW_SSS)}종")
    print(f"   SS전용 추가: {len(NEW_SS_ONLY)}종")
    print(f"   SS_TIER 총 추가: {len(NEW_SSS) + len(NEW_SS_ONLY)}종")


if __name__ == "__main__":
    main()
