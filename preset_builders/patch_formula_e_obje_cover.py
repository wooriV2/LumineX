# -*- coding: utf-8 -*-
"""
LumineX 패치 스크립트
공식 E — 오브제 커버 9종 HOF/SSS/SS 패치

검증 결과:
  HOF 7종: feather_body_cover, mushroom_moss_cover, butterfly_swarm_cover,
            seashell_body_cover, silver_chain_mirror_room, desert_sand_sculpture,
            ice_crystal_gown
  SSS 1종: autumn_leaves_cover
  SS  1종: leaf_draping_cover

실행: python patch_formula_e_obje_cover.py
위치: C:\\Dev\\LumineX\\preset_builders\\
"""

import re
from pathlib import Path

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 티어 분류 ──
HOF_NEW = [
    "feather_body_cover",
    "mushroom_moss_cover",
    "butterfly_swarm_cover",
    "seashell_body_cover",
    "silver_chain_mirror_room",
    "desert_sand_sculpture",
    "ice_crystal_gown",
]

SSS_NEW = [
    "autumn_leaves_cover",
]

SS_NEW = [
    "leaf_draping_cover",
]

# ── HOF는 SSS에도, SSS는 SS에도 포함 (LumineX 규칙) ──
SSS_ALL = HOF_NEW + SSS_NEW   # HOF도 SSS_TIER에 포함
SS_ALL  = HOF_NEW + SSS_NEW + SS_NEW  # 전체 SS_TIER에 포함


def make_entries(names: list[str], indent: str = "    ") -> str:
    return "\n".join(f'{indent}"{name}",' for name in names)


def patch_dashboard(path: Path) -> None:
    text = path.read_text(encoding="utf-8")

    # ── 1. HOF_TIER 패치 ──
    hof_anchor = '"trio_inside_outside_bodypaint",        # 해부학 3레이어(피부/근육/골격) + 박물관 배경 HOF'
    hof_insert = (
        "    # 2026-07-06 공식E 오브제 커버 HOF 7종\n"
        + make_entries(HOF_NEW)
        + "\n"
        + f"    {hof_anchor}"
    )
    if hof_anchor in text:
        text = text.replace(
            f"    {hof_anchor}",
            hof_insert,
        )
        print(f"[HOF_TIER] {len(HOF_NEW)}종 추가 완료")
    else:
        print("[HOF_TIER] 앵커를 찾지 못했습니다 — 수동 확인 필요")

    # ── 2. SSS_TIER 패치 ──
    sss_anchor = '"trio_inside_outside_bodypaint",    "quad_fashion_capitals_bodypaint",'
    # SSS_TIER 첫 번째 등장 위치에 삽입
    sss_insert = (
        "    # 2026-07-06 공식E 오브제 커버 HOF→SSS 포함 (7종) + SSS 1종\n"
        + make_entries(SSS_ALL)
        + "\n"
        + f"    {sss_anchor}"
    )
    # SSS_TIER 블록 내 앵커 (중복 등장하므로 첫 번째만 교체)
    idx = text.find(f"    {sss_anchor}")
    if idx != -1:
        text = text[:idx] + sss_insert + text[idx + len(f"    {sss_anchor}"):]
        print(f"[SSS_TIER] {len(SSS_ALL)}종 추가 완료")
    else:
        print("[SSS_TIER] 앵커를 찾지 못했습니다 — 수동 확인 필요")

    # ── 3. SS_TIER 패치 ──
    ss_anchor = '"quad_four_goddesses_bodypaint",'
    ss_insert = (
        "    # 2026-07-06 공식E 오브제 커버 전체 SS 포함 (9종)\n"
        + make_entries(SS_ALL)
        + "\n"
        + f"    {ss_anchor}"
    )
    idx2 = text.find(f"    {ss_anchor}")
    if idx2 != -1:
        text = text[:idx2] + ss_insert + text[idx2 + len(f"    {ss_anchor}"):]
        print(f"[SS_TIER] {len(SS_ALL)}종 추가 완료")
    else:
        print("[SS_TIER] 앵커를 찾지 못했습니다 — 수동 확인 필요")

    path.write_text(text, encoding="utf-8")
    print("\n✅ dashboard.py 패치 완료")


def verify(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    print("\n── 검증 ──")
    for name in HOF_NEW:
        hof_ok = f'"{name}"' in text
        print(f"  HOF {name}: {'✅' if hof_ok else '❌'}")
    for name in SSS_NEW:
        sss_ok = f'"{name}"' in text
        print(f"  SSS {name}: {'✅' if sss_ok else '❌'}")
    for name in SS_NEW:
        ss_ok = f'"{name}"' in text
        print(f"  SS  {name}: {'✅' if ss_ok else '❌'}")


if __name__ == "__main__":
    if not DASHBOARD.exists():
        print(f"❌ 파일을 찾을 수 없습니다: {DASHBOARD}")
    else:
        patch_dashboard(DASHBOARD)
        verify(DASHBOARD)
        print("\n다음 단계:")
        print('  cd C:\\Dev\\LumineX')
        print('  git add dashboard.py; git commit -m "공식E 오브제 커버 9종 HOF/SSS/SS 패치"')
        print('  git push')
