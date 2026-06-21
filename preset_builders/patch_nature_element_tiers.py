"""
자연&원소 카테고리 tier 패치 스크립트
검증일: 2026-06-21
대상: dashboard.py SSS_TIER / SS_TIER (set 형식)

G1~G4: 기존 검증 완료분 (SSS_TIER/SS_TIER 미등록 확인)
G5~G10: 금일 신규 검증분

앵커: SSS_TIER set의 마지막 기존 항목 뒤에 삽입
"""

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ── 자연&원소 SSS 프리셋 (G1~G10) ──────────────────────────
NATURE_SSS = [
    # G1 용암/화산/열기
    "lava_flow", "heat_shimmer", "solar_flare", "desert_mirage",
    # G2 물/파도/폭포
    "ocean_surge", "waterfall_goddess", "water_reflection", "liquid_gold_pour",
    # G3 얼음/눈 (전종 SSS)
    "ice_palace", "ice_refraction", "frozen_latex", "blizzard_queen",
    "arctic_minimal", "frozen_baikal",
    # G4 사막/안개
    "sandstorm_veil", "desert_oracle", "desert_sand_glam",
    "smoke_veil", "mist_goddess",
    # G5 폭풍/번개
    "storm_couture", "storm_lightning", "lightning_body", "zero_gravity",
    # G6 숲/동굴/지형 (전종 SSS)
    "winter_forest", "cliff_edge", "deep_cave", "dawn_awakening", "liquid_mirror",
    # G7 빛/프리즘/오로라 (전종 SSS)
    "aurora_drape", "aurora_spirit", "prism_light", "shattered_glass", "dead_vlei_ghost",
    # G8 세계 자연 랜드마크 (전종 SSS)
    "son_doong_jungle", "waitomo_glow", "danxia_rainbow", "cenote_sacred",
    "socotra_alien", "lake_natron", "namib_star_desert", "zhangjiajie_avatar",
    # G9 세계 자연 절경 (전종 SSS)
    "pamukkale_white", "plitvice_cascade", "rainbow_mountain",
    "kelimutu_crater", "victoria_falls",
    # G10 분위기/테마 자연 (전종 SSS)
    "wisteria_tunnel", "torres_del_paine", "ha_long_bay",
    "fairy_pools", "tunnel_of_love", "chocolate_hills",
]

# ── 자연&원소 SS 전용 (SSS 아닌 것) ──────────────────────────
NATURE_SS_ONLY = [
    # G1 SS
    "volcanic_goddess", "santorini_lightning",
    # G2 SS
    "tidal_wave", "rain_soaked",
    # G4 SS
    "mist_vanguard",
    # G5 SS
    "tropical_storm",
]

# SS_TIER = SSS + SS 모두 포함
NATURE_SS_TIER = NATURE_SSS + NATURE_SS_ONLY

print(f"[자연&원소] SSS: {len(NATURE_SSS)}종, SS전용: {len(NATURE_SS_ONLY)}종")

# ── dashboard.py 읽기 ────────────────────────────────────────
with open(DASHBOARD_PATH, "r", encoding="utf-8") as f:
    content = f.read()

original = content

# ── SSS_TIER 패치 ────────────────────────────────────────────
# 앵커: 엘리멘탈 갓데스 SSS 마지막 항목 "black_sea_midnight" 뒤
SSS_ANCHOR = '    "black_sea_midnight",'

sss_new_lines = "\n    # 2026-06-21 자연&원소 G1~G10 전체 tier 패치\n"
for p in NATURE_SSS:
    if f'"{p}"' not in content:
        sss_new_lines += f'    "{p}",\n'
    else:
        print(f"[SSS_TIER] 스킵(이미 존재): {p}")

if SSS_ANCHOR not in content:
    print(f"[ERROR] SSS 앵커를 찾을 수 없습니다: {SSS_ANCHOR}")
else:
    content = content.replace(
        SSS_ANCHOR,
        SSS_ANCHOR + sss_new_lines,
        1
    )
    print(f"[SSS_TIER] 패치 완료")

# ── SS_TIER 패치 ─────────────────────────────────────────────
# 앵커: SS_TIER set의 마지막 항목 "noir_femme_fatale" 뒤
SS_ANCHOR = '    "noir_femme_fatale",    # SSS도 SS에 포함\n}'

ss_new_lines = "    # 2026-06-21 자연&원소 G1~G10 SS_TIER 패치\n"
for p in NATURE_SS_TIER:
    if f'"{p}"' not in content.split("SS_TIER")[1][:5000]:  # SS_TIER 블록 내 체크
        ss_new_lines += f'    "{p}",\n'
    else:
        print(f"[SS_TIER] 스킵(이미 존재): {p}")

if SS_ANCHOR not in content:
    print(f"[ERROR] SS 앵커를 찾을 수 없습니다")
    # 폴백: SS_TIER 닫는 } 바로 앞
    SS_ANCHOR2 = '\n}\n\n# ─── 다크 테마 CSS'
    if SS_ANCHOR2 in content:
        content = content.replace(
            SS_ANCHOR2,
            "\n" + ss_new_lines + "}\n\n# ─── 다크 테마 CSS",
            1
        )
        print(f"[SS_TIER] 폴백 앵커로 패치 완료")
else:
    content = content.replace(
        SS_ANCHOR,
        "    \"noir_femme_fatale\",    # SSS도 SS에 포함\n" + ss_new_lines + "}",
        1
    )
    print(f"[SS_TIER] 패치 완료")

# ── 저장 ────────────────────────────────────────────────────
if content != original:
    with open(DASHBOARD_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("\n✅ dashboard.py 패치 완료")
else:
    print("\n⚠️  변경사항 없음")

# ── 디스크 검증 명령어 출력 ──────────────────────────────────
print("\n─── PowerShell 검증 명령어 ───")
samples = NATURE_SSS[:3] + NATURE_SS_ONLY[:2]
for p in samples:
    print(f'Select-String -Path dashboard.py -Pattern \'"{p}"\'')

print(f"\n[요약] SSS {len(NATURE_SSS)}종 / SS전용 {len(NATURE_SS_ONLY)}종 패치 시도")
