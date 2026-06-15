"""
patch_season_theme_and_sss.py
=============================
적용 대상: C:\\Dev\\LumineX\\dashboard.py
커밋 베이스: 28d7894

변경 내용:
1. SSS_TIER — harajuku_doll 승격 (SS→SSS)
2. SSS_TIER — greenhouse_eden 승격 (SS→SSS)
3. SS_TIER  — 계절&테마 그룹1 SS 추가
   cherry_blossom, lavender_field, spring_rain, tulip_field, autumn_forest
4. SS_TIER  — 계절&테마 그룹2 SS 추가
   sunflower_field, greenhouse_eden, tropical_night, first_snow, golden_autumn

실행:
    python preset_builders/patch_season_theme_and_sss.py
"""

import re
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 1. SSS_TIER 블록에 추가할 엔트리 ──────────────────────────────────────
SSS_NEW = '''\
    # 2026-06-15 harajuku_doll SSS 승격 (팝&카와이 — 다케시타 거리 싱크 4장 검증)
    "harajuku_doll",
    # 2026-06-15 greenhouse_eden SSS 승격 (계절&테마 — 잎사귀 드레스=온실 생태계 융합 6장 검증)
    "greenhouse_eden",
'''

# SSS_TIER 블록 끝 바로 앞 (닫는 "}" 직전) 에 삽입
SSS_ANCHOR = '''\
}

# SS tier'''

SSS_REPLACEMENT = SSS_NEW + '''}

# SS tier'''

# ── 2. SS_TIER 블록에 추가할 엔트리 ──────────────────────────────────────
SS_NEW = '''\
    # 2026-06-15 계절&테마 그룹1 SS 확정 (cherry_blossom~autumn_forest)
    "cherry_blossom",
    "lavender_field",
    "spring_rain",
    "tulip_field",
    "autumn_forest",
    # 2026-06-15 계절&테마 그룹2 SS 확정 (sunflower_field~golden_autumn)
    "sunflower_field",
    "greenhouse_eden",   # SSS도 SS에 포함 (format_preset 로직)
    "tropical_night",
    "first_snow",
    "golden_autumn",
    # 2026-06-15 harajuku_doll SSS도 SS에 포함
    "harajuku_doll",
'''

# SS_TIER 닫는 "}" 직전에 삽입
# 기존 마지막 SS 엔트리 바로 뒤 (tennis_short_dress 블록 끝) 를 앵커로 사용
SS_ANCHOR = '''\
    "tennis_short_dress",
}'''

SS_REPLACEMENT = '''\
    "tennis_short_dress",
''' + SS_NEW + '''}'''


def patch():
    src = DASHBOARD.read_text(encoding="utf-8")

    # ── SSS_TIER 패치 ──
    if '"harajuku_doll",' in src and '"greenhouse_eden",' in src \
            and "2026-06-15 harajuku_doll SSS" in src:
        print("[SKIP] SSS_TIER 패치 이미 적용됨")
    else:
        if SSS_ANCHOR not in src:
            raise ValueError("SSS_TIER 앵커 문자열을 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SSS_ANCHOR, SSS_REPLACEMENT, 1)
        print("[OK] SSS_TIER 패치 완료 (harajuku_doll, greenhouse_eden 추가)")

    # ── SS_TIER 패치 ──
    if "2026-06-15 계절&테마 그룹1" in src:
        print("[SKIP] SS_TIER 계절&테마 패치 이미 적용됨")
    else:
        if SS_ANCHOR not in src:
            raise ValueError("SS_TIER 앵커 문자열을 찾을 수 없습니다. dashboard.py 버전을 확인하세요.")
        src = src.replace(SS_ANCHOR, SS_REPLACEMENT, 1)
        print("[OK] SS_TIER 패치 완료 (계절&테마 그룹1+2 추가)")

    DASHBOARD.write_text(src, encoding="utf-8")
    print(f"\n✅ 패치 완료 → {DASHBOARD}")
    print("다음 단계: Select-String 검증 후 커밋&푸시")


if __name__ == "__main__":
    patch()
