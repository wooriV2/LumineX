# -*- coding: utf-8 -*-
"""
patch_phenomenal5_hof10.py
==========================
Phenomenal 5 카테고리 신규 추가 + HOF 10종 패치

대상 파일:
  - C:\Dev\LumineX\core\presets_meta.py  (PRESET_CATEGORIES + HOF_TIER)

추가 카테고리 5개 (각 12종):
  🧲 Ferrofluid Glamour
  🐦 Murmuration Glamour
  🎵 Cymatics Glamour
  🔬 Micro Scale Glamour
  🫧 Mycelium Glamour

HOF 확정 10종 (재검토 기준):
  Ferrofluid  2종: amazon_couture_train, petite_ballgown_spikes
  Murmuration 2종: petite_wedding, amazon_sequin_gown
  Cymatics    2종: plus_size_couture_gown, athletic_sand_body_overlay
  Micro Scale 2종: petite_butterfly_scale, plus_size_crystal_cave_lattice
  Mycelium    2종: plus_size_haute_couture_mushroom, petite_lace_communion

실행:
  cd C:\Dev\LumineX
  python preset_builders\patch_phenomenal5_hof10.py
"""

import re
import sys
from pathlib import Path

TARGET = Path(__file__).parent.parent / "core" / "presets_meta.py"


# ── 1. 추가할 카테고리 프리셋 정의 ──────────────────────────────────
NEW_CATEGORIES = {
    "🧲 Ferrofluid Glamour": [
        # 기존 7종 (이전 라운드)
        "ferrofluid_crown_spikes",
        "ferrofluid_latex_emergence",
        "ferrofluid_gown_river",
        "ferrofluid_spiderweb_silk",
        "ferrofluid_sheer_column",
        "ferrofluid_couture_armor",
        "ferrofluid_mirror_pool",
        # 강화 5종 (이번 라운드)
        "ferrofluid_plus_size_latex_column_goddess",
        "ferrofluid_amazon_couture_train_goddess",
        "ferrofluid_athletic_full_armor_goddess",
        "ferrofluid_petite_ballgown_spikes_goddess",
        "ferrofluid_curvy_wet_look_emergence_goddess",
    ],
    "🐦 Murmuration Glamour": [
        # 기존 7종 (이전 라운드)
        "murmuration_silk_gown",
        "murmuration_latex_cliff",
        "murmuration_sheer_field",
        "murmuration_couture_atrium",
        "murmuration_bodypaint_goddess",
        "murmuration_ruins_editorial",
        "murmuration_desert_goddess",
        # 강화 5종 (이번 라운드)
        "murmuration_plus_size_fur_coat_goddess",
        "murmuration_athletic_latex_goddess",
        "murmuration_amazon_sequin_gown_goddess",
        "murmuration_petite_wedding_goddess",
        "murmuration_curvy_trench_boots_goddess",
    ],
    "🎵 Cymatics Glamour": [
        # 기존 7종 (이전 라운드)
        "cymatics_water_column",
        "cymatics_sand_goddess",
        "cymatics_silk_frequency",
        "cymatics_latex_resonance",
        "cymatics_couture_wave",
        "cymatics_neon_pool",
        "cymatics_crystal_chamber",
        # 강화 5종 (이번 라운드)
        "cymatics_amazon_metallic_bodysuit_goddess",
        "cymatics_plus_size_couture_gown_frequency_goddess",
        "cymatics_petite_wetsuit_deep_frequency_goddess",
        "cymatics_curvy_mirror_dress_goddess",
        "cymatics_athletic_sand_body_overlay_goddess",
    ],
    "🔬 Micro Scale Glamour": [
        # 기존 7종 (이전 라운드)
        "micro_spiderweb_dew_goddess",
        "micro_pollen_goddess",
        "micro_salt_crystal_goddess",
        "micro_feather_barb_goddess",
        "micro_snowflake_goddess",
        "micro_sand_grain_goddess",
        "micro_silk_fiber_goddess",
        # 강화 5종 (이번 라운드)
        "micro_amazon_space_suit_vessel_goddess",
        "micro_plus_size_crystal_cave_lattice_goddess",
        "micro_petite_butterfly_scale_goddess",
        "micro_curvy_soap_film_goddess",
        "micro_athletic_tardigrade_goddess",
    ],
    "🫧 Mycelium Glamour": [
        # 기존 7종 (이전 라운드)
        "mycelium_forest_goddess",
        "mycelium_silk_network",
        "mycelium_latex_roots",
        "mycelium_couture_spores",
        "mycelium_bodypaint_threads",
        "mycelium_ruins_colonized",
        "mycelium_glow_editorial",
        # 강화 5종 (이번 라운드)
        "mycelium_amazon_leather_armor_goddess",
        "mycelium_plus_size_haute_couture_mushroom_goddess",
        "mycelium_curvy_velvet_coat_goddess",
        "mycelium_petite_lace_communion_goddess",
        "mycelium_athletic_neon_bodysuit_network_goddess",
    ],
}

# ── 2. HOF 확정 10종 (재검토 기준) ──────────────────────────────────
NEW_HOF = [
    # 🧲 Ferrofluid (2종)
    "ferrofluid_amazon_couture_train_goddess",      # 페로플루이드 = 스커트 자체 / 브레이크스루
    "ferrofluid_petite_ballgown_spikes_goddess",    # 스파이크 구형 스커트 > figure 신장 / 역전 구도

    # 🐦 Murmuration (2종)
    "murmuration_petite_wedding_goddess",           # 새 베일 = 독립 예술 컨셉
    "murmuration_amazon_sequin_gown_goddess",       # 시퀸 빛 → 새 반응 / 3요소 맞물림

    # 🎵 Cymatics (2종)
    "cymatics_plus_size_couture_gown_frequency_goddess",  # 가운 자체가 cymatics 악기 / 의상=현상
    "cymatics_athletic_sand_body_overlay_goddess",        # 오버헤드 앵글 독점 / body=plate 합체

    # 🔬 Micro Scale (2종)
    "micro_petite_butterfly_scale_goddess",              # 스케일 관계 최강 드라마 / 날개 위 보행
    "micro_plus_size_crystal_cave_lattice_goddess",      # 에메랄드×프리즘×퀸 에너지 완성

    # 🫧 Mycelium (2종)
    "mycelium_plus_size_haute_couture_mushroom_goddess", # 드레스=발광 버섯 / 외부 광원 없음
    "mycelium_petite_lace_communion_goddess",            # 대성당 빔 + 뒤돌아보기 / 영상미 최상
]


def patch_file():
    if not TARGET.exists():
        print(f"[ERROR] 파일 없음: {TARGET}")
        sys.exit(1)

    content = TARGET.read_text(encoding="utf-8")

    # ── Step 1: PRESET_CATEGORIES에 카테고리 추가 ──
    # 마지막 카테고리 닫히는 }\ 바로 앞에 삽입
    # anchor: "}\n}" 패턴 (PRESET_CATEGORIES 닫힘)
    cat_block = "\n"
    for cat_name, presets in NEW_CATEGORIES.items():
        already_in = f'"{cat_name}"' in content
        if already_in:
            print(f"[SKIP] 카테고리 이미 존재: {cat_name}")
            continue
        preset_lines = ",\n        ".join([f'"{p}"' for p in presets])
        cat_block += f'    "{cat_name}": [\n        {preset_lines},\n    ],\n'

    if cat_block.strip():
        # PRESET_CATEGORIES = { ... } 끝 찾기
        # anchor: 'from core.hof_tier import HOF_TIER' 바로 위의 닫힘 }
        anchor = "from core.hof_tier import HOF_TIER"
        if anchor not in content:
            print(f"[ERROR] anchor 없음: '{anchor}'")
            sys.exit(1)
        insert_pos = content.index(anchor)
        # 그 앞의 } 찾기 (PRESET_CATEGORIES 닫힘)
        close_pos = content.rfind("}", 0, insert_pos)
        if close_pos == -1:
            print("[ERROR] PRESET_CATEGORIES 닫힘 } 를 찾을 수 없음")
            sys.exit(1)
        content = content[:close_pos + 1] + "\n" + cat_block + "\n" + content[close_pos + 1:]
        print(f"[OK] PRESET_CATEGORIES에 {len(NEW_CATEGORIES)}개 카테고리 추가")
    else:
        print("[SKIP] 추가할 카테고리 없음 (이미 모두 존재)")

    # ── Step 2: HOF_TIER에 추가 ──
    # core/hof_tier.py를 직접 수정
    hof_target = TARGET.parent / "hof_tier.py"
    if not hof_target.exists():
        print(f"[ERROR] hof_tier.py 없음: {hof_target}")
        sys.exit(1)

    hof_content = hof_target.read_text(encoding="utf-8")
    new_hof_added = []
    for hof_key in NEW_HOF:
        if f'"{hof_key}"' in hof_content:
            print(f"[SKIP] HOF 이미 존재: {hof_key}")
        else:
            new_hof_added.append(hof_key)

    if new_hof_added:
        # HOF_TIER = { ... } 닫힘 } 바로 앞에 삽입
        hof_close = hof_content.rfind("}")
        if hof_close == -1:
            print("[ERROR] HOF_TIER 닫힘 } 없음")
            sys.exit(1)
        hof_insert = "\n    # 2026-07-10 Phenomenal 5 HOF 10종 (재검토 확정)\n"
        for k in new_hof_added:
            hof_insert += f'    "{k}",\n'
        hof_content = hof_content[:hof_close] + hof_insert + hof_content[hof_close:]
        hof_target.write_text(hof_content, encoding="utf-8")
        print(f"[OK] HOF_TIER에 {len(new_hof_added)}종 추가: {new_hof_added}")
    else:
        print("[SKIP] 추가할 HOF 없음")

    # presets_meta.py 저장
    TARGET.write_text(content, encoding="utf-8")
    print(f"[OK] presets_meta.py 저장 완료")


def verify():
    """패치 결과 검증"""
    content = TARGET.read_text(encoding="utf-8")
    hof_content = (TARGET.parent / "hof_tier.py").read_text(encoding="utf-8")

    print("\n── 검증 결과 ──────────────────────────")
    for cat_name in NEW_CATEGORIES:
        exists = f'"{cat_name}"' in content
        print(f"  카테고리 {'[OK]' if exists else '[MISSING]'}: {cat_name}")

    print()
    for hof_key in NEW_HOF:
        exists = f'"{hof_key}"' in hof_content
        print(f"  HOF {'[OK]' if exists else '[MISSING]'}: {hof_key}")

    # 총 프리셋 수 계산 (간이)
    preset_count = content.count('"ferrofluid_') + content.count('"murmuration_') + \
                   content.count('"cymatics_') + content.count('"micro_') + \
                   content.count('"mycelium_')
    print(f"\n  Phenomenal 5 프리셋 등장 횟수 (중복 포함): {preset_count}")
    print("────────────────────────────────────────")


if __name__ == "__main__":
    print("=== Phenomenal 5 + HOF 10 패치 시작 ===")
    patch_file()
    verify()
    print("\n=== 완료 ===")
    print("다음 단계:")
    print("  git add core/presets_meta.py core/hof_tier.py")
    print('  git commit -m "feat: Phenomenal5 5cats 60presets + HOF 10 (재검토 확정)"')
    print("  git push")
