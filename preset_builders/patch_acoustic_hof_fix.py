"""
patch_acoustic_hof_fix.py
==========================
작업 내용:
  1. hof_tier.py — Acoustic Levitation HOF 4종 추가
  2. hof_tier.py — plasma_plus_size_solar_flare_crown 정상 위치로 이동
                   (현재 add_hof 함수 밖에 고립된 문자열로 존재 → HOF_TIER 셋에 삽입)

저장 위치: C:\\Dev\\LumineX\\preset_builders\\patch_acoustic_hof_fix.py
실행: python preset_builders/patch_acoustic_hof_fix.py
"""

from pathlib import Path

HOF_PATH = Path("C:/Dev/LumineX/core/hof_tier.py")

# 추가할 항목들
NEW_HOF_ENTRIES = [
    "acoustic_amazon_mercury_drop_curtain",
    "acoustic_athletic_fire_ember_levitation",
    "acoustic_amazon_flower_petal_vortex",
    "acoustic_plus_size_ice_shard_armor",
    "plasma_plus_size_solar_flare_crown",
]

# 삽입 앵커 — Plasma HOF 5종 블록 마지막 항목 뒤
ANCHOR = '    "plasma_curvy_solar_wind_wet",'

def patch():
    print("=" * 60)
    print("patch_acoustic_hof_fix.py 시작")
    print("=" * 60)

    content = HOF_PATH.read_text(encoding="utf-8")

    if ANCHOR not in content:
        print(f"❌ 앵커 찾기 실패: {ANCHOR}")
        print("hof_tier.py 구조 확인 필요")
        return

    # 이미 추가된 항목 제외
    to_add = [e for e in NEW_HOF_ENTRIES if e not in content]
    if not to_add:
        print("⚠️  모든 항목이 이미 존재 — SKIP")
        return

    # 고립된 plasma 문자열 제거 (add_hof 함수 밖의 잔여 문자열)
    orphan = '\n    "plasma_plus_size_solar_flare_crown",'
    if orphan in content:
        content = content.replace(orphan, "")
        print("  🧹 고립된 plasma 문자열 제거 완료")

    # 앵커 뒤에 새 항목 삽입
    new_block = "\n\n    # ── 🔊 Acoustic Levitation Glamour HOF 4종 + Plasma 추가 1종 ──"
    for entry in to_add:
        new_block += f'\n    "{entry}",'

    new_content = content.replace(
        ANCHOR,
        ANCHOR + new_block
    )

    if new_content == content:
        print("❌ 교체 실패 — 수동 확인 필요")
        return

    HOF_PATH.write_text(new_content, encoding="utf-8")
    print("✅ 패치 완료\n")

    # 검증
    verify = HOF_PATH.read_text(encoding="utf-8")
    all_ok = True
    for entry in NEW_HOF_ENTRIES:
        ok = entry in verify
        print(f"  {'✅' if ok else '❌'} {entry}")
        if not ok:
            all_ok = False

    print(f"\n{'✅ 전체 검증 통과' if all_ok else '❌ 일부 누락 — 수동 확인 필요'}")
    print("\n다음 단계:")
    print("  Select-String 'acoustic_amazon_mercury_drop_curtain' core\\hof_tier.py")
    print("  Select-String 'plasma_plus_size_solar_flare_crown' core\\hof_tier.py")
    print("  git add core/presets_meta.py core/hof_tier.py")
    print('  git commit -m "feat: Acoustic Levitation Glamour 12종 추가 HOF 4종 + plasma HOF 승격"')
    print("  git push")

if __name__ == "__main__":
    patch()
