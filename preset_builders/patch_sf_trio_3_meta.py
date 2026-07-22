import ast
from pathlib import Path

BASE = Path("C:/Dev/LumineX")
META_PATH = BASE / "core/presets_meta.py"

KEYS = [
    "silverfox_trio_black_koi_lotus_gold_void",
    "silverfox_trio_black_haetae_dragon_crimson_capetown",
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

keys_str = "\n".join([f'        "{k}",' for k in KEYS])
new_category = f'\n    "\U0001f98a Silver Fox TRIO": [\n{keys_str}\n    ],\n'

content = META_PATH.read_text(encoding="utf-8-sig")

# PRESET_CATEGORIES 딕셔너리의 마지막 } 앞에 삽입
insert_pos = content.rfind("}")
content = content[:insert_pos] + new_category + content[insert_pos:]

META_PATH.write_text(content, encoding="utf-8")
print("✅ presets_meta.py 🦊 Silver Fox TRIO 카테고리 추가 완료")

ast.parse(content)
print("✅ AST OK: presets_meta.py")
print("\n다음:")
print("git add -A")
print('git commit -m "feat: Silver Fox TRIO SF-86~100 패치 (HOF 2 / SSS 13)"')
print("git push")
