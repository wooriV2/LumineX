# -*- coding: utf-8 -*-
import ast, shutil
from pathlib import Path

BASE = Path("C:/Dev/LumineX/core")
HOF_FILE = BASE / "hof_tier.py"
SSS_FILE = BASE / "sss_tier.py"

NEW_HOF = [
    "deepblack_trio_crossover_plum_chrysanthemum_bamboo_irezumi_biopunk_uvneon_voidbl",
    "deepblack_trio_crossover_chrysanthemum_plum_crane_irezumi_crystal_uvneon_voidbl",
    "deepblack_trio_crossover_tiger_wisteria_irezumi_plasma_uvneon_voidbl",
    "deepblack_trio_crossover_snake_crane_irezumi_bioluminescent_uvneon_voidbl",
    "deepblack_trio_crossover_peony_bamboo_irezumi_aurora_crystal_uvneon_voidbl",
    "deepblack_trio_crossover_phoenix_maple_irezumi_murmuration_uvneon_voidbl",
    "deepblack_trio_crossover_koi_plum_irezumi_cymatics_uvneon_voidbl",
    "deepblack_trio_crossover_tiger_lotus_irezumi_mycelium_uvneon_voidbl",
]

NEW_SSS = [
    "deepblack_trio_crossover_dragon_phoenix_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_koi_tiger_uvneon_voidbl",
    "deepblack_trio_crossover_snake_lotus_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_crane_wave_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_peony_maple_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_dragon_wisteria_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_koi_sakura_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_phoenix_peony_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_wave_fuji_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_tiger_maple_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_dragon_phoenix_koi_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_koi_wave_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_tiger_snake_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_crane_dragon_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_phoenix_tiger_irezumi_uvneon_voidbl",
    "deepblack_trio_crossover_wisteria_crane_peony_irezumi_galaxy_uvneon_voidbl",
    "deepblack_trio_crossover_lotus_sakura_maple_irezumi_aurora_uvneon_voidbl",
    "deepblack_trio_crossover_wave_peony_wisteria_irezumi_cosmos_uvneon_voidbl",
    "deepblack_trio_crossover_dragon_lotus_irezumi_holographic_uvneon_voidbl",
    "deepblack_trio_crossover_koi_phoenix_irezumi_nebula_uvneon_voidbl",
    "deepblack_trio_crossover_dragon_chrysanthemum_irezumi_ferrofluid_uvneon_voidbl",
    "deepblack_trio_crossover_crane_peony_irezumi_micro_scale_uvneon_voidbl",
]

def patch_file(filepath, new_keys, label):
    content = filepath.read_text(encoding="utf-8-sig")
    added, skipped = [], []
    for key in new_keys:
        if f'"{key}"' in content:
            skipped.append(key)
            continue
        last_brace = content.rfind("}")
        insert_line = f'    "{key}",\n'
        content = content[:last_brace] + insert_line + content[last_brace:]
        added.append(key)
    filepath.write_text(content, encoding="utf-8")
    print(f"✅ {label}: 추가 {len(added)}종 / 스킵 {len(skipped)}종")
    if skipped:
        for s in skipped:
            print(f"   ⚠️ 스킵: {s}")
    return added

def validate(filepath):
    try:
        ast.parse(filepath.read_text(encoding="utf-8"))
        print(f"✅ AST OK: {filepath.name}")
        return True
    except SyntaxError as e:
        print(f"❌ AST 오류: {filepath.name} → {e}")
        return False

if __name__ == "__main__":
    shutil.copy(HOF_FILE, HOF_FILE.with_suffix(".py.bak"))
    shutil.copy(SSS_FILE, SSS_FILE.with_suffix(".py.bak"))
    print("=== HOF 패치 ===")
    patch_file(HOF_FILE, NEW_HOF, "HOF_TIER")
    print("\n=== SSS 패치 ===")
    patch_file(SSS_FILE, NEW_SSS, "SSS_TIER")
    print("\n=== AST 검증 ===")
    validate(HOF_FILE)
    validate(SSS_FILE)
    print("\n완료! 커밋 전 AST OK 확인 후 진행하세요.")
