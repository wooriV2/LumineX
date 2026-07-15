# -*- coding: utf-8 -*-
"""
Young Adult 한국인 20종 패치 스크립트
대상 파일: core/presets_meta.py
실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_young_korean_20.py
"""

import re

TARGET_FILE = "core/presets_meta.py"

NEW_PRESETS = {
    "young_korean_jeju_sunrise":           ("영어덜트 제주 일출",          "SS",  ["korean","young","jeju","sunrise"]),
    "young_korean_studio_black_minimal":   ("영어덜트 블랙 스튜디오",      "SS",  ["korean","young","studio","minimal"]),
    "young_korean_pool_pastel":            ("영어덜트 파스텔 풀",           "S",   ["korean","young","pool","pastel"]),
    "young_korean_cherry_blossom":         ("영어덜트 벚꽃",               "SS",  ["korean","young","cherry","blossom"]),
    "young_korean_neon_first_night":       ("영어덜트 홍대 네온",           "SS",  ["korean","young","hongdae","neon"]),
    "young_korean_maldives_first_trip":    ("영어덜트 몰디브 첫 여행",      "SS",  ["korean","young","maldives","first"]),
    "young_korean_tokyo_first_solo":       ("영어덜트 도쿄 하라주쿠",       "S",   ["korean","young","tokyo","harajuku"]),
    "young_korean_paris_first_europe":     ("영어덜트 파리 에펠탑",         "SSS", ["korean","young","paris","eiffel"]),
    "young_korean_tattoo_first_wrist":     ("영어덜트 손목타투 서울카페",   "SS",  ["korean","young","tattoo","wrist"]),
    "young_korean_bali_first_solo":        ("영어덜트 발리 첫 배낭",        "SS",  ["korean","young","bali","sunset"]),
    "young_korean_gym_first_gains":        ("영어덜트 홈짐 첫 근육",        "S",   ["korean","young","gym","gains"]),
    "young_korean_summer_busan":           ("영어덜트 부산 해운대",          "SS",  ["korean","young","busan","summer"]),
    "young_korean_tattoo_ankle_jeju":      ("영어덜트 발목타투 제주",        "SS",  ["korean","young","tattoo","ankle"]),
    "young_korean_midnight_rooftop_seoul": ("영어덜트 서울 새벽 루프탑",    "SSS", ["korean","young","seoul","midnight"]),
    "young_korean_nyc_first_american":     ("영어덜트 NYC 타임스퀘어",      "SSS", ["korean","young","nyc","times_square"]),
    "young_korean_campus_spring":          ("영어덜트 캠퍼스 봄",           "S",   ["korean","young","campus","spring"]),
    "young_korean_tattoo_shoulder_okinawa":("영어덜트 어깨타투 오키나와",   "SS",  ["korean","young","tattoo","shoulder"]),
    "young_korean_debut_red_carpet":       ("영어덜트 레드카펫 데뷔",       "SSS", ["korean","young","debut","red_carpet"]),
    "young_korean_first_snowfall_seoul":   ("영어덜트 서울 첫눈",           "SS",  ["korean","young","seoul","snow"]),
    "young_korean_21_birthday_gold":       ("영어덜트 21세 생일 골드",      "SSS", ["korean","young","birthday","gold"]),
}

SSS_KEYS = [k for k,(l,t,g) in NEW_PRESETS.items() if t == "SSS"]
SS_KEYS  = [k for k,(l,t,g) in NEW_PRESETS.items() if t == "SS"]
S_KEYS   = [k for k,(l,t,g) in NEW_PRESETS.items() if t == "S"]

with open(TARGET_FILE, "r", encoding="utf-8-sig") as f:
    src = f.read()

# ── PRESET_CATEGORIES에 korean_young_adult 블록 추가 ───────────
BLOCK_KEY = "korean_young_adult"

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

    # korean_runway_slim 블록 뒤에 삽입 (없으면 korean_fitness 뒤에)
    for anchor_key in ["korean_runway_slim", "korean_fitness"]:
        pattern = rf'("{anchor_key}":\s*\{{.*?\n    \}},)'
        match = re.search(pattern, src, re.DOTALL)
        if match:
            src = src[:match.end()] + new_block + src[match.end():]
            print(f"[OK] {BLOCK_KEY} 블록 추가됨 ({anchor_key} 뒤).")
            break
    else:
        print("[ERROR] 앵커 블록을 찾지 못했습니다.")
        exit(1)

# ── SSS_TIER ──────────────────────────────────────────────────
SSS_ANCHOR = "SSS_TIER = ["
for key in SSS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SSS_TIER: {key}")
    else:
        src = src.replace(SSS_ANCHOR, SSS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SSS_TIER: {key}")

# ── SS_TIER ───────────────────────────────────────────────────
SS_ANCHOR = "SS_TIER = ["
for key in SS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SS_TIER: {key}")
    else:
        src = src.replace(SS_ANCHOR, SS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SS_TIER: {key}")

# ── S_TIER ────────────────────────────────────────────────────
S_ANCHOR = "S_TIER = ["
if S_ANCHOR in src:
    for key in S_KEYS:
        if f'"{key}"' in src:
            print(f"[SKIP] S_TIER: {key}")
        else:
            src = src.replace(S_ANCHOR, S_ANCHOR + f'\n    "{key}",')
            print(f"[OK] S_TIER: {key}")
else:
    print(f"[WARN] S_TIER 앵커 없음. S 티어 항목은 수동 추가 필요: {S_KEYS}")

with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(src)

print(f"\n✅ patch_young_korean_20.py 완료!")
print(f"   SSS: {SSS_KEYS}")
print(f"   SS : {SS_KEYS}")
print(f"   S  : {S_KEYS}")
