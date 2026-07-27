# -*- coding: utf-8 -*-
"""
patch_bp_hof_4_tier.py
Bodypaint HOF 28종 - presets_meta.py 등록 + hof_tier.py 패치 + AST 검증

실행 순서:
    $env:PYTHONUTF8 = "1"
    cd C:\\Dev\\LumineX
    python preset_builders\\patch_bp_hof_1_solo.py
    python preset_builders\\patch_bp_hof_2_duo.py
    python preset_builders\\patch_bp_hof_3_trio.py
    python preset_builders\\patch_bp_hof_4_tier.py
"""
import ast
import os
import re

META_PATH = "core/presets_meta.py"
HOF_PATH = "core/hof_tier.py"

CATEGORY = "🎨 Bodypaint"

SOLO_KEYS = [
    "bp_solo_shibori_indigo_mature",
    "bp_solo_katazome_crane_pine_mature",
    "bp_solo_hwarot_phoenix_gold_elder",
    "bp_solo_adire_eleko_indigo_mature",
    "bp_solo_abrbandi_ikat_young",
    "bp_solo_andean_pallay_mature",
    "bp_solo_kente_adweneasa_mature",
    "bp_solo_miao_batik_silver_mature",
    "bp_solo_ndebele_geometric_mature",
    "bp_solo_kuba_raffia_mature",
    "bp_solo_paj_ntaub_hmong_mature",
    "bp_solo_termeh_boteh_mature",
    "bp_solo_ainu_moreu_mature",
]

DUO_KEYS = [
    "bp_duo_diatom_radiolaria_mature",
    "bp_duo_pollen_wingscale_mature",
    "bp_duo_stomata_rootsection_mature",
    "bp_duo_peristome_sporeridge_mature",
    "bp_duo_leafskeleton_ginkgovein_mature",
]

TRIO_KEYS = [
    "bp_trio_indigo_resist_mature",
    "bp_trio_mineral_section_mature",
    "bp_trio_islamic_geometry_mature",
    "bp_trio_ceramic_glaze_mature",
    "bp_trio_frost_crystal_mature",
    "bp_trio_interlace_manuscript_mature",
    "bp_trio_cartography_mature",
    "bp_trio_architectural_section_mature",
    "bp_trio_natural_history_plate_mature",
    "bp_trio_woodblock_line_mature",
]

ALL_KEYS = SOLO_KEYS + DUO_KEYS + TRIO_KEYS


def _read(path):
    with open(path, encoding="utf-8-sig") as f:
        return f.read()


def _write(path, src):
    with open(path, "w", encoding="utf-8") as f:
        f.write(src)


def _validate(path):
    ast.parse(_read(path))


def _insert_before_last_brace(src, block):
    """마지막 } 앞에 block 삽입. lambda 사용으로 백슬래시 이스케이프 문제 회피."""
    src = src.rstrip()
    new_src, n = re.subn(r'(\})\s*$', lambda m: block + m.group(1), src)
    if n != 1:
        raise RuntimeError("닫는 중괄호를 찾지 못했습니다 — 파일 구조 확인 필요")
    return new_src


def patch_hof(path, keys):
    src = _read(path)
    new_keys = [k for k in keys if f'"{k}"' not in src]
    if not new_keys:
        print("⏭ HOF: 전부 이미 등록됨")
        return 0

    block = "\n" + "\n".join(f'    "{k}",' for k in new_keys) + "\n"
    _write(path, _insert_before_last_brace(src, block))
    _validate(path)
    print(f"✅ HOF 패치 완료 ({len(new_keys)}개): {path}")
    return len(new_keys)


def patch_meta(path, keys, category):
    src = _read(path)
    new_keys = [k for k in keys if f'"{k}"' not in src]
    if not new_keys:
        print("⏭ META: 전부 이미 등록됨")
        return 0

    block = "\n" + "\n".join(
        f'    "{k}": {{"key": "{k}", "category": "{category}"}},'
        for k in new_keys
    ) + "\n"
    _write(path, _insert_before_last_brace(src, block))
    _validate(path)
    print(f"✅ META 패치 완료 ({len(new_keys)}개): {path}")
    return len(new_keys)


def verify_sync():
    missing = [k for k in ALL_KEYS if not os.path.exists(f"presets/{k}.json")]
    if missing:
        print(f"\n⚠ JSON 누락 (대시보드에 안 보임): {len(missing)}개")
        for k in missing:
            print(f"   - {k}")
        print("   → patch_bp_hof_1_solo.py / _2_duo.py / _3_trio.py 를 먼저 실행하세요")
        return False
    print(f"\n✅ JSON ↔ META 동기화 확인 완료 ({len(ALL_KEYS)}개)")
    return True


def main():
    print(f"대상: SOLO {len(SOLO_KEYS)} / DUO {len(DUO_KEYS)} / TRIO {len(TRIO_KEYS)} "
          f"= 총 {len(ALL_KEYS)}개\n")

    patch_meta(META_PATH, ALL_KEYS, CATEGORY)
    patch_hof(HOF_PATH, ALL_KEYS)

    for p, name in ((META_PATH, "META"), (HOF_PATH, "HOF")):
        _validate(p)
        print(f"🧪 {name} AST OK")

    verify_sync()


if __name__ == "__main__":
    main()
