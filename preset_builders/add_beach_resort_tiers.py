"""
LumineX — 비치&리조트 tier 패치 스크립트
대상 파일: dashboard.py
실행: python add_beach_resort_tiers.py

패치 내용:
  SSS 신규 4개: infinity_pool, scuba_goddess, spa_noir, sunset_cruise
  SS  신규 12개: summer_beach, surfer_goddess, pool_goddess, poolside_noir,
                 glass_floor, glass_house, ski_chalet, beach_bonfire,
                 balcony_goddess, coral_diving, beach_bonfire_night, hammock_resort
"""

from pathlib import Path
import re, sys

TARGET = Path("dashboard.py")

if not TARGET.exists():
    print(f"❌ {TARGET} 파일을 찾을 수 없습니다. dashboard.py가 있는 디렉토리에서 실행하세요.")
    sys.exit(1)

src = TARGET.read_text(encoding="utf-8")

# ──────────────────────────────────────────────────────────
# 1. SSS_TIER — 비치 SSS 4개 추가
# ──────────────────────────────────────────────────────────

SSS_ANCHOR = '    # 2026-06-13 v27 핫&섹시 SSS 확정\n    "dressing_room_mirror",\n    "vip_booth_neon",\n}'

SSS_INSERT = '''\
    # 2026-06-13 v27 핫&섹시 SSS 확정
    "dressing_room_mirror",
    "vip_booth_neon",
    # 2026-06-13 비치&리조트 SSS 확정
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
}'''

if SSS_ANCHOR not in src:
    print("❌ SSS_TIER 앵커를 찾지 못했습니다. dashboard.py 내용을 확인하세요.")
    sys.exit(1)

src = src.replace(SSS_ANCHOR, SSS_INSERT)
print("✅ SSS_TIER 패치 완료 (infinity_pool, scuba_goddess, spa_noir, sunset_cruise)")

# ──────────────────────────────────────────────────────────
# 2. SS_TIER — 비치 SS 12개 추가 (SSS 포함 블록 직전에 삽입)
# ──────────────────────────────────────────────────────────

SS_ANCHOR = '    # SSS도 SS에 포함 (format_preset 로직)'

SS_NEW_BLOCK = '''\
    # 2026-06-13 비치&리조트 SS/SSS 확정
    "summer_beach",
    "surfer_goddess",
    "pool_goddess",
    "poolside_noir",
    "glass_floor",
    "glass_house",
    "ski_chalet",
    "beach_bonfire",
    "balcony_goddess",
    "coral_diving",
    "beach_bonfire_night",
    "hammock_resort",
    # SSS 비치 4종도 SS에 포함
    "infinity_pool",
    "scuba_goddess",
    "spa_noir",
    "sunset_cruise",
    # SSS도 SS에 포함 (format_preset 로직)'''

if SS_ANCHOR not in src:
    print("❌ SS_TIER 앵커를 찾지 못했습니다. dashboard.py 내용을 확인하세요.")
    sys.exit(1)

src = src.replace(SS_ANCHOR, SS_NEW_BLOCK)
print("✅ SS_TIER 패치 완료 (비치&리조트 12종 + SSS 4종)")

# ──────────────────────────────────────────────────────────
# 3. 저장
# ──────────────────────────────────────────────────────────

TARGET.write_text(src, encoding="utf-8")
print(f"\n✅ {TARGET} 저장 완료!")
print("\n📋 패치 요약:")
print("  SSS tier 신규: infinity_pool, scuba_goddess, spa_noir, sunset_cruise (+4)")
print("  SS  tier 신규: summer_beach, surfer_goddess, pool_goddess, poolside_noir,")
print("                 glass_floor, glass_house, ski_chalet, beach_bonfire,")
print("                 balcony_goddess, coral_diving, beach_bonfire_night, hammock_resort (+12)")
print("\n🔍 검증 명령어 (PowerShell):")
print('  Select-String -Path dashboard.py -Pattern "infinity_pool" | Select-Object LineNumber, Line')
print('  Select-String -Path dashboard.py -Pattern "hammock_resort" | Select-Object LineNumber, Line')
print("\n📌 다음 단계:")
print("  git add dashboard.py")
print('  git commit -m "tier: 비치&리조트 SSS 4개 + SS 12개 확정 패치"')
print("  git push")
