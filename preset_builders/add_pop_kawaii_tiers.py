"""
LumineX — 🍬 팝 & 카와이 카테고리 tier 패치 스크립트
저장 위치: preset_builders/add_pop_kawaii_tiers.py
실행 위치: C:\Dev\LumineX\ (루트에서 실행)
  python preset_builders/add_pop_kawaii_tiers.py

패치 내용:
  SSS 신규 10개:
    cherry_pop, hime_gyaru, decora_kei, lolita_gothic, space_babe,
    arcade_queen, virtual_idol, kdrama_villain_queen, bubble_tea, doll_house

  SS  신규 22개:
    y2k_fairy, pink_champagne, cotton_candy, angel_baby, idol_stage,
    kitty_glam, strawberry_milk, neon_kawaii, fairy_kei,
    gyaru_glam, kogal_style, maid_glamour,
    visual_kei, disco_barbie, bubblegum_pop,
    rainbow_rave, glitter_bomb, tokimeki_pop,
    kpop_girl_crush, hallyu_goddess,
    kdrama_chaebol_heir, gangnam_luxury_glam, harajuku_doll

  일반(A):
    kbeauty_glass_skin
"""

from pathlib import Path
import sys

TARGET = Path("dashboard.py")

if not TARGET.exists():
    print(f"❌ {TARGET} 파일을 찾을 수 없습니다. C:\\Dev\\LumineX\\ 루트에서 실행하세요.")
    sys.exit(1)

src = TARGET.read_text(encoding="utf-8")

# ──────────────────────────────────────────────────────────
# 1. SSS_TIER — 팝&카와이 SSS 10개 추가
# ──────────────────────────────────────────────────────────

SSS_ANCHOR = '    # 2026-06-13 비치&리조트 SSS 확정\n    "infinity_pool",\n    "scuba_goddess",\n    "spa_noir",\n    "sunset_cruise",\n}'

SSS_INSERT = '''\
    # 2026-06-13 비치&리조트 SSS 확정
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
    # 2026-06-14 팝&카와이 SSS 확정
    "cherry_pop",
    "hime_gyaru",
    "decora_kei",
    "lolita_gothic",
    "space_babe",
    "arcade_queen",
    "virtual_idol",
    "kdrama_villain_queen",
    "bubble_tea",
    "doll_house",
}'''

if SSS_ANCHOR not in src:
    print("❌ SSS_TIER 앵커를 찾지 못했습니다. dashboard.py 내용을 확인하세요.")
    sys.exit(1)

src = src.replace(SSS_ANCHOR, SSS_INSERT)
print("✅ SSS_TIER 패치 완료 (팝&카와이 SSS 10개)")

# ──────────────────────────────────────────────────────────
# 2. SS_TIER — 팝&카와이 SS 23개 + SSS 10개 추가
# ──────────────────────────────────────────────────────────

SS_ANCHOR = '    # SSS 비치 4종도 SS에 포함\n    "infinity_pool",\n    "scuba_goddess",\n    "spa_noir",\n    "sunset_cruise",\n    # SSS도 SS에 포함 (format_preset 로직)'

SS_NEW_BLOCK = '''\
    # SSS 비치 4종도 SS에 포함
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
    # 2026-06-14 팝&카와이 SS 확정
    "y2k_fairy",
    "pink_champagne",
    "cotton_candy",
    "angel_baby",
    "idol_stage",
    "kitty_glam",
    "strawberry_milk",
    "neon_kawaii",
    "fairy_kei",
    "gyaru_glam",
    "kogal_style",
    "maid_glamour",
    "visual_kei",
    "disco_barbie",
    "bubblegum_pop",
    "rainbow_rave",
    "glitter_bomb",
    "tokimeki_pop",
    "kpop_girl_crush",
    "hallyu_goddess",
    "kdrama_chaebol_heir",
    "gangnam_luxury_glam",
    "harajuku_doll",
    # 2026-06-14 팝&카와이 SSS 10종도 SS에 포함
    "cherry_pop",
    "hime_gyaru",
    "decora_kei",
    "lolita_gothic",
    "space_babe",
    "arcade_queen",
    "virtual_idol",
    "kdrama_villain_queen",
    "bubble_tea",
    "doll_house",
    # SSS도 SS에 포함 (format_preset 로직)'''

if SS_ANCHOR not in src:
    print("❌ SS_TIER 앵커를 찾지 못했습니다. dashboard.py 내용을 확인하세요.")
    sys.exit(1)

src = src.replace(SS_ANCHOR, SS_NEW_BLOCK)
print("✅ SS_TIER 패치 완료 (팝&카와이 SS 23개 + SSS 10개)")

# ──────────────────────────────────────────────────────────
# 3. 저장
# ──────────────────────────────────────────────────────────

TARGET.write_text(src, encoding="utf-8")
print(f"\n✅ {TARGET} 저장 완료!")
print("\n📋 패치 요약:")
print("  SSS tier 신규: cherry_pop, hime_gyaru, decora_kei, lolita_gothic,")
print("                 space_babe, arcade_queen, virtual_idol,")
print("                 kdrama_villain_queen, bubble_tea, doll_house (+10)")
print("  SS  tier 신규: y2k_fairy, pink_champagne, cotton_candy, angel_baby,")
print("                 idol_stage, kitty_glam, strawberry_milk, neon_kawaii,")
print("                 fairy_kei, gyaru_glam, kogal_style, maid_glamour,")
print("                 visual_kei, disco_barbie, bubblegum_pop, rainbow_rave,")
print("                 glitter_bomb, tokimeki_pop, kpop_girl_crush,")
print("                 hallyu_goddess, kdrama_chaebol_heir,")
print("                 gangnam_luxury_glam, harajuku_doll (+23)")
print("  일반(A): kbeauty_glass_skin")
print("\n🔍 검증 명령어 (PowerShell):")
print('  Select-String -Path dashboard.py -Pattern "cherry_pop" | Select-Object LineNumber, Line')
print('  Select-String -Path dashboard.py -Pattern "doll_house" | Select-Object LineNumber, Line')
print('  Select-String -Path dashboard.py -Pattern "harajuku_doll" | Select-Object LineNumber, Line')
print("\n📌 다음 단계:")
print("  git add dashboard.py")
print('  git commit -m "tier: 팝&카와이 SSS 10개 + SS 23개 확정 패치"')
print("  git push")
