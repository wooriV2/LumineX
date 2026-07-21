# -*- coding: utf-8 -*-
"""
DeepBlack Trio — Tier A (이레즈미×3) + Tier B (UV×UV×UV)
HOF / SSS 패치 스크립트

저장 위치: C:\Dev\LumineX\preset_builders\patch_deepblack_trio_tierAB.py
"""

import ast
import shutil
from pathlib import Path

BASE = Path("C:/Dev/LumineX/core")
HOF_FILE = BASE / "hof_tier.py"
SSS_FILE = BASE / "sss_tier.py"

# ═══════════════════════════════════════════════════
# HOF 추가 목록 (총 15종)
# ═══════════════════════════════════════════════════
NEW_HOF = [
    # 🔴 이레즈미×이레즈미×이레즈미 HOF 6종
    "deepblack_trio_dragon_koi_phoenix_goldvoid",
    "deepblack_trio_dragon_wisteria_phoenix_peony_koi_sakura_voidbl",
    "deepblack_trio_phoenix_peony_koi_sakura_dragon_wisteria_nightsky",
    "deepblack_trio_dragon_peony_phoenix_maple_koi_wisteria_crimsonvoid",
    "deepblack_trio_phoenix_wisteria_dragon_sakura_koi_peony_purplevoid",
    "deepblack_trio_phoenix_peony_koi_wisteria_dragon_lotus_midnightvoid",
    # 🔵 UV×UV×UV HOF 9종
    "deepblack_trio_uv_crimson_phoenix_gold_serpent_violet_lotus_voidbl",
    "deepblack_trio_uv_green_circuit_orange_tiger_blue_wave_voidbl",
    "deepblack_trio_uv_red_tribal_yellow_sun_purple_moon_voidbl",
    "deepblack_trio_uv_violet_nebula_cyan_galaxy_gold_stardust_voidbl",
    "deepblack_trio_uv_magenta_sakura_rain_cyan_thunder_white_lightning_voidbl",
    "deepblack_trio_uv_gold_arabesque_crimson_calligraphy_violet_fractal_voidbl",
    "deepblack_trio_uv_cyan_jellyfish_magenta_coral_gold_deep_voidbl",
    "deepblack_trio_uv_pink_floral_explosion_teal_wave_gold_sun_voidbl",
    "deepblack_trio_uv_neon_rainbow_psychedelic_acid_plasma_burst_voidbl",
]

# ═══════════════════════════════════════════════════
# SSS 추가 목록 (총 13종)
# ═══════════════════════════════════════════════════
NEW_SSS = [
    # 🔴 이레즈미×이레즈미×이레즈미 SSS 4종
    "deepblack_trio_tiger_dragon_snake_bamboovoid",
    "deepblack_trio_koi_sakura_dragon_lotus_phoenix_peony_goldvoid",
    "deepblack_trio_dragon_sakura_phoenix_lotus_koi_maple_rosevoid",
    "deepblack_trio_dragon_chrysanthemum_tiger_maple_koi_wave_lacquervoid",
    # 🔵 UV×UV×UV SSS 9종
    "deepblack_trio_uv_magenta_mandala_cyan_dragon_white_constellation_voidbl",
    "deepblack_trio_uv_white_geometric_cyan_koi_magenta_flame_voidbl",
    "deepblack_trio_uv_orange_lava_blue_ice_green_acid_voidbl",
    "deepblack_trio_uv_blue_mandala_pink_butterfly_green_vine_voidbl",
    "deepblack_trio_uv_teal_mermaid_orange_sunset_white_moon_voidbl",
    "deepblack_trio_uv_violet_spiderweb_green_toxic_pink_acid_voidbl",
    "deepblack_trio_uv_gold_circuit_blue_data_crimson_glitch_voidbl",
    "deepblack_trio_uv_white_crystal_violet_aurora_cyan_ice_voidbl",
    "deepblack_trio_uv_red_lava_crack_orange_ember_yellow_fire_voidbl",
]


def patch_file(filepath, new_keys, label):
    content = filepath.read_text(encoding="utf-8-sig")
    added = []
    skipped = []

    for key in new_keys:
        if f'"{key}"' in content:
            skipped.append(key)
            continue
        # 마지막 } 앞에 삽입
        last_brace = content.rfind("}")
        insert_line = f'    "{key}",\n'
        content = content[:last_brace] + insert_line + content[last_brace:]
        added.append(key)

    filepath.write_text(content, encoding="utf-8")

    print(f"\n{'='*55}")
    print(f"✅ {label} 패치 완료 → {filepath.name}")
    print(f"   추가: {len(added)}종 / 스킵(중복): {len(skipped)}종")
    if added:
        for k in added:
            print(f"   + {k}")
    return added


def validate(filepath):
    try:
        ast.parse(filepath.read_text(encoding="utf-8"))
        print(f"  ✅ AST OK: {filepath.name}")
        return True
    except SyntaxError as e:
        print(f"  ❌ AST 오류: {filepath.name} → {e}")
        return False


if __name__ == "__main__":
    print("🖤 DeepBlack Trio Tier A/B 패치 시작")

    # 백업
    shutil.copy(HOF_FILE, HOF_FILE.with_suffix(".py.bak"))
    shutil.copy(SSS_FILE, SSS_FILE.with_suffix(".py.bak"))
    print("📦 백업 완료 (.bak)")

    # 패치
    patch_file(HOF_FILE, NEW_HOF, "HOF_TIER (Tier A+B)")
    patch_file(SSS_FILE, NEW_SSS, "SSS_TIER (Tier A+B)")

    # AST 검증
    print(f"\n{'='*55}")
    print("🔍 AST 검증 중...")
    hof_ok = validate(HOF_FILE)
    sss_ok = validate(SSS_FILE)

    if hof_ok and sss_ok:
        print("\n🎉 모든 검증 통과! 아래 명령어로 커밋하세요:")
        print("""
git add -A
git commit -m "feat: DeepBlack Trio Tier A(이레즈미×3) + Tier B(UV×3) HOF/SSS 패치"
git push
""")
    else:
        print("\n⚠️ 검증 실패 — 백업(.bak)으로 복구 후 확인하세요.")
