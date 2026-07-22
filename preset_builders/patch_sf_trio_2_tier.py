import ast
from pathlib import Path

BASE = Path("C:/Dev/LumineX")

HOF_KEYS = [
    "silverfox_trio_black_koi_lotus_gold_void",
    "silverfox_trio_black_haetae_dragon_crimson_capetown",
]

SSS_KEYS = [
    "silverfox_trio_black_koi_lotus_gold_bali",
    "silverfox_trio_black_haetae_phoenix_crimson_cairo",
    "silverfox_trio_black_dragon_dancheong_gold_shanghai",
    "silverfox_trio_black_tiger_crane_crimson_aurora",
    "silverfox_trio_black_phoenix_haetae_gold_angkor",
    "silverfox_trio_black_dragon_minhwa_crimson_istanbul",
    "silverfox_trio_black_phoenix_crane_gold_machu_picchu",
    "silverfox_trio_black_tiger_minhwa_crimson_void",
    "silverfox_trio_black_dragon_lotus_gold_petra",
    "silverfox_trio_black_haetae_phoenix_crimson_paris",
    "silverfox_trio_black_tiger_celadon_gold_kyoto",
    "silverfox_trio_black_dragon_haetae_crimson_rio",
    "silverfox_trio_black_phoenix_lotus_gold_void",
]

ALL_KEYS = HOF_KEYS + SSS_KEYS

# HOF tier 패치
HOF_PATH = BASE / "core/hof_tier.py"
content = HOF_PATH.read_text(encoding="utf-8-sig")
for key in HOF_KEYS:
    if f'"{key}"' not in content:
        last = content.rfind("}")
        content = content[:last] + f'    "{key}",\n' + content[last:]
HOF_PATH.write_text(content, encoding="utf-8")
print(f"✅ hof_tier.py 패치 완료 ({len(HOF_KEYS)}종)")

# SSS tier 패치
SSS_PATH = BASE / "core/sss_tier.py"
content = SSS_PATH.read_text(encoding="utf-8-sig")
for key in SSS_KEYS:
    if f'"{key}"' not in content:
        last = content.rfind("}")
        content = content[:last] + f'    "{key}",\n' + content[last:]
SSS_PATH.write_text(content, encoding="utf-8")
print(f"✅ sss_tier.py 패치 완료 ({len(SSS_KEYS)}종)")

# presets_meta.py 카테고리 추가
META_PATH = BASE / "core/presets_meta.py"
content = META_PATH.read_text(encoding="utf-8-sig")
target = '"🦊 Silver Fox TRIO":'
if target not in content:
    print("⚠️ Silver Fox TRIO 카테고리 없음 — 수동 추가 필요")
else:
    idx = content.find(target)
    end = content.find(']', idx)
    for key in ALL_KEYS:
        if f'"{key}"' not in content:
            content = content[:end] + f'        "{key}",\n' + content[end:]
            end = content.find(']', idx)
    META_PATH.write_text(content, encoding="utf-8")
    print("✅ presets_meta.py 패치 완료")

# AST 검증
for path in [HOF_PATH, SSS_PATH, META_PATH]:
    ast.parse(path.read_text(encoding="utf-8"))
    print(f"✅ AST OK: {path.name}")

print(f"\n🎉 완료! HOF {len(HOF_KEYS)}종 / SSS {len(SSS_KEYS)}종")
print("\n다음:")
print("git add -A")
print('git commit -m "feat: Silver Fox TRIO SF-86~100 패치 (HOF 2 / SSS 13)"')
print("git push")
