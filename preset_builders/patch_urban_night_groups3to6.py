"""
도시&나이트 그룹 3~6 티어 패치
검증 결과 반영: SSS/SS/S 등급 적용 + SSS는 SS_TIER에도 포함

실행: python preset_builders/patch_urban_night_groups3to6.py
디스크 검증: Select-String 으로 앵커 확인 후 실행
"""

import re

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ──────────────────────────────────────────────
# 최종 등급표
# ──────────────────────────────────────────────
# 그룹 3 — 도시 글래머/재즈
#   monaco_nights  SSS
#   miami_afterglow  S
#   azure_nights  SS
#   blue_hour_goddess  SS
#   candlelight_noir  SSS
#   jazz_club  SSS
#   jazz_age  SS
#   disco_goddess  SS
#
# 그룹 4 — 에디토리얼/무드
#   noir_ballet  SSS
#   urban_vanguard  SS
#   brutalist_glam  SSS
#   music_festival  SS
#   new_year_countdown  SSS
#   emerald_city  SSS
#   subway_editorial  SS
#
# 그룹 5 — 도시 랜드마크
#   tokyo_shibuya  SSS
#   paris_midnight  SSS
#   penthouse_view  SSS
#   sheikh_zayed_dawn  SSS
#   livraria_lello_staircase  SSS
#   palacio_de_sal  SSS
#   chefchaouen_blue  SSS
#
# 그룹 6 — 유럽 풍경
#   santorini_sunset  SS
#   cappadocia_balloons  SS
#   hallstatt_lake  SSS
#   shirakawa_snow  SSS
#   positano_cliff  SS
#   bruges_canal  SSS
#   cinque_terre_harbor  SSS
# ──────────────────────────────────────────────

SSS_PRESETS = [
    "monaco_nights",
    "candlelight_noir",
    "jazz_club",
    "noir_ballet",
    "brutalist_glam",
    "new_year_countdown",
    "emerald_city",
    "tokyo_shibuya",
    "paris_midnight",
    "penthouse_view",
    "sheikh_zayed_dawn",
    "livraria_lello_staircase",
    "palacio_de_sal",
    "chefchaouen_blue",
    "hallstatt_lake",
    "shirakawa_snow",
    "bruges_canal",
    "cinque_terre_harbor",
]

SS_PRESETS = [
    "azure_nights",
    "blue_hour_goddess",
    "jazz_age",
    "disco_goddess",
    "urban_vanguard",
    "music_festival",
    "subway_editorial",
    "santorini_sunset",
    "cappadocia_balloons",
    "positano_cliff",
]

S_PRESETS = [
    "miami_afterglow",
]


def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def patch_preset_tier(content, preset_name, tier):
    """
    preset dict 안의 "tier": "..." 값을 교체.
    앵커: "name": "<preset_name>" 이후 첫 번째 "tier": 라인
    """
    # 패턴: 프리셋 블록 내 tier 값 교체
    pattern = r'("name"\s*:\s*"' + re.escape(preset_name) + r'".*?"tier"\s*:\s*")[^"]*(")'
    replacement = r'\g<1>' + tier + r'\2'
    new_content, count = re.subn(pattern, replacement, content, count=1, flags=re.DOTALL)
    if count == 0:
        print(f"  [WARN] 앵커 미발견: {preset_name}")
    else:
        print(f"  [OK] {preset_name} → {tier}")
    return new_content


def patch_ss_tier_list(content, sss_presets):
    """
    SS_TIER 리스트에 SSS 프리셋 추가 (중복 방지)
    앵커: SS_TIER = [ ... ] 블록
    """
    # SS_TIER 블록 찾기
    ss_tier_pattern = r'(SS_TIER\s*=\s*\[)(.*?)(\])'
    match = re.search(ss_tier_pattern, content, re.DOTALL)
    if not match:
        print("[WARN] SS_TIER 블록 미발견 — 수동 확인 필요")
        return content

    existing_block = match.group(2)
    added = []
    new_entries = ""

    for preset in sss_presets:
        if f'"{preset}"' not in existing_block:
            new_entries += f'\n    "{preset}",'
            added.append(preset)
        else:
            print(f"  [SKIP] SS_TIER 이미 포함: {preset}")

    if added:
        new_block = match.group(1) + existing_block + new_entries + "\n" + match.group(3)
        content = content[:match.start()] + new_block + content[match.end():]
        print(f"  [OK] SS_TIER 추가: {added}")

    return content


def main():
    print(f"파일 읽기: {DASHBOARD_PATH}")
    content = read_file(DASHBOARD_PATH)
    original_len = len(content)

    print("\n[1단계] 개별 프리셋 tier 값 패치")
    for p in SSS_PRESETS:
        content = patch_preset_tier(content, p, "SSS")
    for p in SS_PRESETS:
        content = patch_preset_tier(content, p, "SS")
    for p in S_PRESETS:
        content = patch_preset_tier(content, p, "S")

    print("\n[2단계] SS_TIER 리스트에 SSS 프리셋 추가")
    content = patch_ss_tier_list(content, SSS_PRESETS)

    print(f"\n파일 쓰기: {DASHBOARD_PATH}")
    print(f"  변경 전 길이: {original_len}")
    print(f"  변경 후 길이: {len(content)}")
    write_file(DASHBOARD_PATH, content)
    print("완료.")


if __name__ == "__main__":
    main()
