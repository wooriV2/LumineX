# -*- coding: utf-8 -*-
"""
Runway Slim 한국인 20종 패치 스크립트
대상 파일: core/presets_meta.py
실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_runway_korean_slim_20.py
"""

import re

TARGET_FILE = "core/presets_meta.py"

NEW_PRESETS = {
    "runway_korean_slim_void_studio":           ("런웨이 슬림 보이드 스튜디오",    "SS",  ["korean","runway","slim","void","studio"]),
    "runway_korean_slim_paris_window":          ("런웨이 슬림 파리 창가",          "SS",  ["korean","runway","slim","paris","window"]),
    "runway_korean_slim_milan_catwalk":         ("런웨이 슬림 밀라노 캣워크",      "SSS", ["korean","runway","slim","milan","catwalk"]),
    "runway_korean_slim_tokyo_shibuya_rain":    ("런웨이 슬림 시부야 빗속",        "SSS", ["korean","runway","slim","tokyo","rain"]),
    "runway_korean_slim_dubai_penthouse":       ("런웨이 슬림 두바이 펜트하우스",  "SS",  ["korean","runway","slim","dubai","penthouse"]),
    "runway_korean_slim_nyc_rooftop":           ("런웨이 슬림 NYC 루프탑",         "SS",  ["korean","runway","slim","nyc","rooftop"]),
    "runway_korean_slim_seoulforest_spring":    ("런웨이 슬림 서울숲 봄",          "SS",  ["korean","runway","slim","seoul","spring"]),
    "runway_korean_slim_icelandic_glacier":     ("런웨이 슬림 아이슬란드 빙하",    "SSS", ["korean","runway","slim","iceland","glacier"]),
    "runway_korean_slim_moroccan_riad":         ("런웨이 슬림 모로코 리아드",      "SS",  ["korean","runway","slim","morocco","riad"]),
    "runway_korean_slim_amalfi_cliff":          ("런웨이 슬림 아말피 해안",        "SS",  ["korean","runway","slim","amalfi","cliff"]),
    "runway_korean_slim_berlin_underground":    ("런웨이 슬림 베를린 언더그라운드","SS",  ["korean","runway","slim","berlin","techno"]),
    "runway_korean_slim_bali_temple_gold":      ("런웨이 슬림 발리 사원 골드",     "SS",  ["korean","runway","slim","bali","temple"]),
    "runway_korean_slim_kyoto_autumn":          ("런웨이 슬림 교토 단풍",          "SS",  ["korean","runway","slim","kyoto","autumn"]),
    "runway_korean_slim_palawan_karst":         ("런웨이 슬림 팔라완 카르스트",    "SS",  ["korean","runway","slim","palawan","karst"]),
    "runway_korean_slim_aurora_finland":        ("런웨이 슬림 핀란드 오로라",      "SSS", ["korean","runway","slim","finland","aurora"]),
    "runway_korean_slim_sahara_wind":           ("런웨이 슬림 사하라 바람",        "SS",  ["korean","runway","slim","sahara","desert"]),
    "runway_korean_slim_seychelles_granite":    ("런웨이 슬림 세이셸 화강암",      "SS",  ["korean","runway","slim","seychelles","granite"]),
    "runway_korean_slim_tattoo_collarbone_void":("런웨이 슬림 쇄골타투 보이드",   "SSS", ["korean","runway","slim","tattoo","collarbone"]),
    "runway_korean_slim_newyork_snowstorm":     ("런웨이 슬림 NYC 눈보라",         "SS",  ["korean","runway","slim","nyc","blizzard"]),
    "runway_korean_slim_crystal_gala":          ("런웨이 슬림 크리스탈 갈라",      "SSS", ["korean","runway","slim","crystal","gala"]),
}

SSS_KEYS = [k for k,(l,t,g) in NEW_PRESETS.items() if t == "SSS"]
SS_KEYS  = [k for k,(l,t,g) in NEW_PRESETS.items() if t == "SS"]

with open(TARGET_FILE, "r", encoding="utf-8-sig") as f:
    src = f.read()

# ── PRESET_CATEGORIES에 korean_runway_slim 블록 추가 ──────────────
BLOCK_KEY = "korean_runway_slim"
ANCHOR = '"korean_fitness": {'   # korean_fitness 블록 바로 뒤에 삽입

if BLOCK_KEY in src:
    print(f"[SKIP] {BLOCK_KEY} 블록 이미 존재.")
else:
    entries = ""
    for key, (label, tier, tags) in NEW_PRESETS.items():
        tags_str = ", ".join(f'"{t}"' for t in tags)
        entries += f'''        "{key}": {{
            "label": "{label}",
            "tier": "{tier}",
            "tags": [{tags_str}],
        }},
'''

    new_block = f'''
    "{BLOCK_KEY}": {{
{entries}    }},'''

    # korean_fitness 블록 닫힘 }}, 뒤에 삽입
    pattern = r'("korean_fitness":\s*\{.*?\n    \},)'
    match = re.search(pattern, src, re.DOTALL)
    if match:
        src = src[:match.end()] + new_block + src[match.end():]
        print(f"[OK] {BLOCK_KEY} 블록 추가됨 (20종).")
    else:
        print("[ERROR] korean_fitness 블록 끝 패턴을 찾지 못했습니다. 수동 확인 필요.")
        exit(1)

# ── SSS_TIER 추가 ──────────────────────────────────────────────
SSS_ANCHOR = "SSS_TIER = ["
for key in SSS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SSS_TIER: {key}")
    else:
        src = src.replace(SSS_ANCHOR, SSS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SSS_TIER: {key}")

# ── SS_TIER 추가 ───────────────────────────────────────────────
SS_ANCHOR = "SS_TIER = ["
for key in SS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SS_TIER: {key}")
    else:
        src = src.replace(SS_ANCHOR, SS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SS_TIER: {key}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(src)

print(f"\n✅ patch_runway_korean_slim_20.py 완료!")
print(f"   SSS: {SSS_KEYS}")
print(f"   SS : {SS_KEYS}")
