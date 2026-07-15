# -*- coding: utf-8 -*-
"""
patch_plasma_category.py
========================
☀️ Plasma & Solar Flare Glamour 카테고리 신규 추가
+ HOF 5종 / SSS 8종 tier 패치

대상 파일:
  - C:\\Dev\\LumineX\\core\\presets_meta.py
  - C:\\Dev\\LumineX\\core\\hof_tier.py

HOF 확정 5종 (33% 선정률):
  plasma_athletic_flare_eruption
  plasma_amazon_chromosphere_gown
  plasma_plus_size_sunspot_vortex
  plasma_athletic_solar_minimum
  plasma_curvy_solar_wind_wet

SSS 8종:
  plasma_amazon_solar_wind_train
  plasma_plus_size_corona_loop_goddess
  plasma_petite_prominence_pillar
  plasma_curvy_granulation_skin
  plasma_petite_heliosphere_emergence
  plasma_curvy_magnetic_reconnection
  plasma_amazon_magnetosphere_armor
  plasma_plus_size_solar_flare_crown

실행:
  cd C:\\Dev\\LumineX
  python preset_builders\\patch_plasma_category.py
"""

import ast
import sys
from pathlib import Path

TARGET = Path(__file__).parent.parent / "core" / "presets_meta.py"
HOF_TARGET = Path(__file__).parent.parent / "core" / "hof_tier.py"

# ── 카테고리 프리셋 정의 ──
PLASMA_PRESETS = [
    "plasma_amazon_solar_wind_train",
    "plasma_plus_size_corona_loop_goddess",
    "plasma_petite_prominence_pillar",
    "plasma_curvy_granulation_skin",
    "plasma_athletic_flare_eruption",
    "plasma_amazon_chromosphere_gown",
    "plasma_plus_size_sunspot_vortex",
    "plasma_petite_heliosphere_emergence",
    "plasma_curvy_magnetic_reconnection",
    "plasma_athletic_solar_minimum",
    "plasma_amazon_magnetosphere_armor",
    "plasma_plus_size_solar_flare_crown",
    "plasma_curvy_solar_wind_wet",
]

# ── HOF 5종 ──
PLASMA_HOF = [
    "plasma_athletic_flare_eruption",
    "plasma_amazon_chromosphere_gown",
    "plasma_plus_size_sunspot_vortex",
    "plasma_athletic_solar_minimum",
    "plasma_curvy_solar_wind_wet",
]

# ── SSS 8종 ──
PLASMA_SSS = [
    "plasma_amazon_solar_wind_train",
    "plasma_plus_size_corona_loop_goddess",
    "plasma_petite_prominence_pillar",
    "plasma_curvy_granulation_skin",
    "plasma_petite_heliosphere_emergence",
    "plasma_curvy_magnetic_reconnection",
    "plasma_amazon_magnetosphere_armor",
    "plasma_plus_size_solar_flare_crown",
]


def read_file(path):
    raw = path.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]
    return raw.decode("utf-8")


def write_file(path, content):
    path.write_text(content, encoding="utf-8")


def validate(content, label):
    try:
        ast.parse(content)
        print(f"[OK] {label} 문법 정상")
        return True
    except SyntaxError as e:
        print(f"[ERROR] {label} 문법 오류: line {e.lineno} — {e.msg}")
        return False


def patch_presets_meta():
    content = read_file(TARGET)

    # 이미 존재하면 스킵
    if '"☀️ Plasma & Solar Flare Glamour"' in content:
        print("[SKIP] Plasma 카테고리 이미 존재")
        return

    # 카테고리 블록 생성
    preset_lines = ",\n        ".join([f'"{p}"' for p in PLASMA_PRESETS])
    cat_block = f'\n    "☀️ Plasma & Solar Flare Glamour": [\n        {preset_lines},\n    ],\n'

    # anchor: from core.hof_tier import HOF_TIER 바로 앞 } 찾기
    anchor = "from core.hof_tier import HOF_TIER"
    if anchor not in content:
        print(f"[ERROR] anchor 없음: {anchor}")
        sys.exit(1)

    anchor_idx = content.index(anchor)
    # anchor 앞에서 마지막 } 찾기
    close_pos = content.rfind("}", 0, anchor_idx)
    if close_pos == -1:
        print("[ERROR] PRESET_CATEGORIES 닫힘 } 없음")
        sys.exit(1)

    # } 앞에 카테고리 삽입
    content = content[:close_pos] + cat_block + content[close_pos:]

    if not validate(content, "presets_meta.py"):
        sys.exit(1)

    write_file(TARGET, content)
    print(f"[OK] Plasma 카테고리 {len(PLASMA_PRESETS)}종 추가 완료")


def patch_hof():
    content = read_file(HOF_TARGET)
    new_hof = [k for k in PLASMA_HOF if f'"{k}"' not in content]

    if not new_hof:
        print("[SKIP] HOF 이미 모두 존재")
        return

    close_pos = content.rfind("}")
    if close_pos == -1:
        print("[ERROR] HOF_TIER 닫힘 } 없음")
        sys.exit(1)

    insert = "\n    # 2026-07-11 Plasma & Solar Flare HOF 5종\n"
    for k in new_hof:
        insert += f'    "{k}",\n'

    content = content[:close_pos] + insert + content[close_pos:]
    write_file(HOF_TARGET, content)
    print(f"[OK] HOF {len(new_hof)}종 추가: {new_hof}")


def patch_sss():
    content = read_file(TARGET)
    new_sss = [k for k in PLASMA_SSS if f'"{k}"' not in content]

    if not new_sss:
        print("[SKIP] SSS 이미 모두 존재")
        return

    # SSS_TIER = { 블록에 삽입
    anchor = "# SSS tier"
    if anchor not in content:
        print(f"[ERROR] SSS anchor 없음")
        sys.exit(1)

    # SSS_TIER = { 다음 첫 줄 찾기
    sss_open = content.index("SSS_TIER = {")
    first_entry = content.index("\n", sss_open) + 1

    insert = "    # 2026-07-11 Plasma & Solar Flare SSS 8종\n"
    for k in new_sss:
        insert += f'    "{k}",\n'

    content = content[:first_entry] + insert + content[first_entry:]

    if not validate(content, "presets_meta.py (SSS)"):
        sys.exit(1)

    write_file(TARGET, content)
    print(f"[OK] SSS {len(new_sss)}종 추가: {new_sss}")

    # SS_TIER에도 SSS 포함
    new_ss = [k for k in PLASMA_SSS + PLASMA_HOF if f'"{k}"' not in content or True]
    content = read_file(TARGET)
    ss_anchor = "SS_TIER = {"
    if ss_anchor not in content:
        print("[ERROR] SS_TIER anchor 없음")
        sys.exit(1)

    all_plasma = PLASMA_HOF + PLASMA_SSS
    new_ss = [k for k in all_plasma if content.count(f'"{k}"') < 2]

    if new_ss:
        ss_open = content.index(ss_anchor)
        ss_first = content.index("\n", ss_open) + 1
        ss_insert = "    # 2026-07-11 Plasma SS_TIER 포함\n"
        for k in new_ss:
            ss_insert += f'    "{k}",\n'
        content = content[:ss_first] + ss_insert + content[ss_first:]

        if not validate(content, "presets_meta.py (SS)"):
            sys.exit(1)

        write_file(TARGET, content)
        print(f"[OK] SS_TIER {len(new_ss)}종 추가")


def verify():
    content = read_file(TARGET)
    hof_content = read_file(HOF_TARGET)

    print("\n── 검증 ──────────────────────────")
    cat_ok = '"☀️ Plasma & Solar Flare Glamour"' in content
    print(f"  카테고리: {'[OK]' if cat_ok else '[MISSING]'}")

    for k in PLASMA_HOF:
        ok = f'"{k}"' in hof_content
        print(f"  HOF {'[OK]' if ok else '[MISSING]'}: {k}")

    for k in PLASMA_SSS:
        ok = f'"{k}"' in content
        print(f"  SSS {'[OK]' if ok else '[MISSING]'}: {k}")
    print("───────────────────────────────────")


if __name__ == "__main__":
    print("=== Plasma & Solar Flare 패치 시작 ===")
    patch_presets_meta()
    patch_hof()
    patch_sss()
    verify()
    print("\n=== 완료 ===")
    print("다음 단계:")
    print("  git add core/presets_meta.py core/hof_tier.py")
    print('  git commit -m "feat: Plasma & Solar Flare Glamour 13종 + HOF 5 + SSS 8"')
    print("  git push")
