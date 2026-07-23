import ast
from pathlib import Path

BASE = Path("C:/Dev/LumineX")

HOF_KEYS = [
    "silverfox_trio_korean_crimson_lightning_dragon_peony_bioluminescent_void",
    "silverfox_trio_korean_violet_nebula_phoenix_wisteria_aurora_void",
    "silverfox_trio_korean_cyan_circuit_tiger_lotus_orange_solar_void",
    "silverfox_trio_korean_ferrofluid_phoenix_sakura_violet_nebula_void",
    "silverfox_trio_korean_aurora_crystal_koi_sakura_crimson_lightning_void",
    "silverfox_trio_korean_murmuration_phoenix_wisteria_aurora_crystal_void",
    "silverfox_trio_orange_solar_tiger_maple_bioluminescent_void",
    "silverfox_trio_latina_plasma_pink_phoenix_sakura_gold_cymatics_void",
    "silverfox_trio_aurora_crystal_dragon_peony_murmuration_void",
    "silverfox_trio_latina_crimson_lightning_koi_sakura_holographic_void",
    "silverfox_trio_bioluminescent_snake_chrysanthemum_crimson_lightning_void",
    "silverfox_trio_plasma_pink_crane_wave_holographic_void",
    "silverfox_trio_murmuration_tiger_lotus_gold_cymatics_void",
    "silverfox_trio_violet_nebula_dragon_wisteria_aurora_crystal_void",
    "silverfox_trio_crimson_lightning_dragon_peony_violet_nebula_blackbrazilian_void",
    "silverfox_trio_gold_cymatics_tiger_lotus_bioluminescent_blackscandinavian_void",
]

SSS_KEYS = [
    "silverfox_trio_korean_crimson_lightning_dragon_peony_bioluminescent_void",  # KSF-003
    "silverfox_trio_korean_gold_cymatics_crane_wave_mycelium_void",
    "silverfox_trio_korean_holographic_snake_chrysanthemum_gold_cymatics_void",
    "silverfox_trio_violet_nebula_crane_wave_ferrofluid_void",
    "silverfox_trio_ferrofluid_koi_maple_orange_solar_void",
]

# HOF tier 패치
HOF_PATH = BASE / "core/hof_tier.py"
content = HOF_PATH.read_text(encoding="utf-8-sig")
added = 0
for key in HOF_KEYS:
    if f'"{key}"' not in content:
        last = content.rfind("}")
        content = content[:last] + f'    "{key}",\n' + content[last:]
        added += 1
HOF_PATH.write_text(content, encoding="utf-8")
print(f"✅ hof_tier.py 패치 완료 ({added}종 추가)")

# SSS tier 패치
SSS_PATH = BASE / "core/sss_tier.py"
content = SSS_PATH.read_text(encoding="utf-8-sig")
added = 0
for key in SSS_KEYS:
    if f'"{key}"' not in content:
        last = content.rfind("}")
        content = content[:last] + f'    "{key}",\n' + content[last:]
        added += 1
SSS_PATH.write_text(content, encoding="utf-8")
print(f"✅ sss_tier.py 패치 완료 ({added}종 추가)")

# presets_meta.py 카테고리 추가
META_PATH = BASE / "core/presets_meta.py"
content = META_PATH.read_text(encoding="utf-8-sig")

ALL_KEYS = HOF_KEYS + [k for k in SSS_KEYS if k not in HOF_KEYS]

# 🦊 Silver Fox TRIO 카테고리 찾아서 추가
target = '"🦊 Silver Fox TRIO":'
if target not in content:
    # 없으면 새로 생성
    keys_str = "\n".join([f'        "{k}",' for k in ALL_KEYS])
    new_cat = f'\n    "🦊 Silver Fox TRIO": [\n{keys_str}\n    ],\n'
    insert_pos = content.rfind("}")
    content = content[:insert_pos] + new_cat + content[insert_pos:]
    print("✅ presets_meta.py 🦊 Silver Fox TRIO 카테고리 신규 생성")
else:
    idx = content.find(target)
    end = content.find(']', idx)
    for key in ALL_KEYS:
        if f'"{key}"' not in content:
            content = content[:end] + f'        "{key}",\n' + content[end:]
            end = content.find(']', idx)
    print("✅ presets_meta.py 🦊 Silver Fox TRIO 카테고리 업데이트")

META_PATH.write_text(content, encoding="utf-8")

# AST 검증
for path in [HOF_PATH, SSS_PATH, META_PATH]:
    ast.parse(path.read_text(encoding="utf-8"))
    print(f"✅ AST OK: {path.name}")

print(f"\n🎉 완료! HOF {len(HOF_KEYS)}종 / SSS {len(SSS_KEYS)}종")
print("\n다음:")
print("git add -A")
print('git commit -m "feat: Silver Fox TRIO KSF-001~020 + TEST-A/C 패치 (HOF 16 / SSS 5)"')
print("git push")
