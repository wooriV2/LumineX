"""
불가능&초현실 카테고리 Tier 패치 스크립트
대상: C:\Dev\LumineX\dashboard.py
최신 커밋 기준: 06f3894

검증 결과 요약 (29종):
  SSS: 23종
  SS:   6종 (flame_dress, reflection_rebel, macro_goddess, micro_world, dissolution, richat_eye)

적용 방식: str.replace 앵커 방식 (기존 워크플로우 동일)
"""

import re

DASHBOARD_PATH = r"C:\Dev\LumineX\dashboard.py"

# ──────────────────────────────────────────────
# 불가능&초현실 SSS 프리셋 (23종)
# ──────────────────────────────────────────────
SSS_PRESETS = [
    # 자연현상 의상화 (4종)
    "waterfall_gown",
    "cloud_couture",
    "weather_maker",
    "aurora_embodied",
    # 거울/반사/분열 (3종)
    "mirror_shatter_dress",
    "double_exposure_self",
    "shadow_independent",
    # 우주/천체 (3종)
    "supernova_burst",
    "nebula_goddess",
    "magnetic_field_goddess",
    # 생물/자연 스케일 (2종)
    "giant_flora",
    "crystallization",
    # 초현실 연출 (4종)
    "storm_eye_editorial",
    "living_fabric",
    "portal_threshold",
    "escher_staircase",
    # 랜드마크 배경 (1종)
    "marble_caves_water",
    # 물리 법칙 파괴 (6종) — 이전 세션 완료분 재확인 포함
    "gravity_defiance",
    "gravity_well",
    "time_freeze_editorial",
    "time_lapse_body",
    "invisible_outline",
    "negative_space",
]

# ──────────────────────────────────────────────
# 불가능&초현실 SS 프리셋 (6종)
# SSS는 SS_TIER에도 포함하는 규칙 적용
# ──────────────────────────────────────────────
SS_ONLY_PRESETS = [
    # SS 단독 (SSS 미달)
    "flame_dress",
    "reflection_rebel",
    "macro_goddess",
    "micro_world",
    "dissolution",
    "richat_eye",
]

# SS_TIER = SSS 전체 + SS 단독
SS_PRESETS = SSS_PRESETS + SS_ONLY_PRESETS


def build_set_entries(preset_list: list[str], indent: int = 4) -> str:
    """프리셋 리스트를 set 항목 문자열로 변환"""
    pad = " " * indent
    return "\n".join(f'{pad}"{p}",' for p in preset_list)


def apply_patch(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    original = content  # 롤백용

    # ── 1. SSS_TIER 패치 ──────────────────────────────
    # 앵커: 기존 SSS_TIER set 내 마지막 항목 뒤에 추가
    # 기존 패턴: SSS_TIER = { ... "negative_space", }  ← 물리법칙 마지막 항목
    sss_anchor = '"negative_space",'
    sss_new_entries = build_set_entries(
        [p for p in SSS_PRESETS if p != "negative_space"
         and p not in [  # 이미 포함된 물리법칙 6종 제외
             "gravity_defiance", "gravity_well", "time_freeze_editorial",
             "time_lapse_body", "invisible_outline",
         ]]
    )

    if sss_anchor not in content:
        print(f"[ERROR] SSS_TIER 앵커를 찾을 수 없습니다: {sss_anchor!r}")
        print("  → dashboard.py에서 SSS_TIER set의 마지막 항목을 확인하세요.")
        return

    sss_replacement = f'{sss_anchor}\n{sss_new_entries}'
    content = content.replace(sss_anchor, sss_replacement, 1)
    print(f"[OK] SSS_TIER 패치 완료 — {len(SSS_PRESETS) - 6}종 추가")

    # ── 2. SS_TIER 패치 ───────────────────────────────
    # 앵커: SS_TIER set 내 마지막 항목 뒤에 추가
    # (SS_TIER는 SSS를 포함하므로 negative_space가 이미 있다고 가정)
    ss_anchor = '"negative_space",'

    # SS_TIER 블록이 두 번째로 등장하는 위치를 찾아야 함
    # (SSS_TIER에도 negative_space가 있으므로 두 번째 occurrence 타겟)
    first_pos = content.find(ss_anchor)
    second_pos = content.find(ss_anchor, first_pos + 1)

    if second_pos == -1:
        print(f"[ERROR] SS_TIER 앵커 두 번째 위치를 찾을 수 없습니다: {ss_anchor!r}")
        print("  → SS_TIER와 SSS_TIER가 별도 set으로 선언되어 있는지 확인하세요.")
        # 롤백
        with open(path, "w", encoding="utf-8") as f:
            f.write(original)
        return

    ss_new_entries = build_set_entries(SS_PRESETS)
    # 두 번째 occurrence 교체
    content = content[:second_pos] + \
              ss_anchor + "\n" + ss_new_entries + \
              content[second_pos + len(ss_anchor):]
    print(f"[OK] SS_TIER 패치 완료 — {len(SS_PRESETS)}종 (SSS {len(SSS_PRESETS)}종 + SS전용 {len(SS_ONLY_PRESETS)}종)")

    # ── 3. 저장 ──────────────────────────────────────
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"\n[DONE] 패치 저장 완료 → {path}")
    print(f"  SSS_TIER 추가: {len(SSS_PRESETS) - 6}종")
    print(f"  SS_TIER  추가: {len(SS_PRESETS)}종 (물리법칙 6종 포함)")


def verify_patch(path: str) -> None:
    """패치 결과 검증"""
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    print("\n[VERIFY] SSS_TIER 포함 여부:")
    for p in SSS_PRESETS:
        mark = "✅" if f'"{p}"' in content else "❌"
        print(f"  {mark} {p}")

    print("\n[VERIFY] SS_TIER 포함 여부 (SS 전용):")
    for p in SS_ONLY_PRESETS:
        mark = "✅" if f'"{p}"' in content else "❌"
        print(f"  {mark} {p}")


if __name__ == "__main__":
    print("=" * 60)
    print("불가능&초현실 Tier 패치 시작")
    print("=" * 60)
    apply_patch(DASHBOARD_PATH)
    verify_patch(DASHBOARD_PATH)
