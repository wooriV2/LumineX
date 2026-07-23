# -*- coding: utf-8 -*-
import ast, re

HOF_KEYS = [
    "sf_duo_persian_jade",
    "sf_duo_berber_flame",
    "sf_duo_babylon_goddess",
    "sf_duo_phoenician_cedar",
    "sf_duo_sheba_queen",
    "sf_duo_carthage_queen",
    "sf_duo_magyar_rose",
    "sf_duo_dacian_wolf",
    "sf_duo_thracian_rose",
    "sf_duo_serbian_orthodox",
    "sf_duo_mayan_jaguar",
    "sf_duo_polish_amber",
    "sf_duo_mesopotamian_fire",
    "sf_duo_carthage_fire",
    "sf_duo_lebanese_rose",
    "sf_duo_amazon_thunder",
]

SSS_KEYS = [
    "sf_duo_dragon_lotus",
    "sf_duo_nabataean_rose",
    "sf_duo_arabian_nights",
    "sf_duo_bohemian_crystal",
    "sf_duo_dalmatian_queen",
    "sf_duo_finnish_aurora",
    "sf_duo_scottish_highland",
    "sf_duo_polynesian_storm",
    "sf_duo_byzantine_queen",
    "sf_duo_anatolian_goddess",
    "sf_duo_roman_goddess",
]

META_KEYS = HOF_KEYS + SSS_KEYS

# ── 1. hof_tier.py 패치 ──────────────────────────────────────────
HOF_PATH = r"C:\Dev\LumineX\core\hof_tier.py"
with open(HOF_PATH, encoding="utf-8-sig") as f:
    hof_src = f.read()

hof_insert = "\n" + "\n".join(f'    "{k}",' for k in HOF_KEYS) + "\n"
hof_src = hof_src.rstrip()
hof_src = re.sub(r'(\})\s*$', hof_insert + r'\1', hof_src)

with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof_src)

ast.parse(open(HOF_PATH, encoding="utf-8").read())
print("✅ hof_tier.py 패치 및 AST 검증 완료")

# ── 2. sss_tier.py 패치 ──────────────────────────────────────────
SSS_PATH = r"C:\Dev\LumineX\core\sss_tier.py"
with open(SSS_PATH, encoding="utf-8-sig") as f:
    sss_src = f.read()

sss_insert = "\n" + "\n".join(f'    "{k}",' for k in SSS_KEYS) + "\n"
sss_src = sss_src.rstrip()
sss_src = re.sub(r'(\})\s*$', sss_insert + r'\1', sss_src)

with open(SSS_PATH, "w", encoding="utf-8") as f:
    f.write(sss_src)

ast.parse(open(SSS_PATH, encoding="utf-8").read())
print("✅ sss_tier.py 패치 및 AST 검증 완료")

# ── 3. presets_meta.py 패치 ──────────────────────────────────────
META_PATH = r"C:\Dev\LumineX\core\presets_meta.py"
with open(META_PATH, encoding="utf-8-sig") as f:
    meta_src = f.read()

meta_insert = "\n" + "\n".join(f'    "{k}": {{"key": "{k}", "category": "🦁 Silver Fox DUO"}},' for k in META_KEYS) + "\n"
meta_src = meta_src.rstrip()
meta_src = re.sub(r'(\})\s*$', meta_insert + r'\1', meta_src)

with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta_src)

ast.parse(open(META_PATH, encoding="utf-8").read())
print("✅ presets_meta.py 패치 및 AST 검증 완료")

print(f"\n🎉 전체 패치 완료! HOF {len(HOF_KEYS)}개 / SSS {len(SSS_KEYS)}개")
