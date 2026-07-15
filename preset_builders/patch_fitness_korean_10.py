# -*- coding: utf-8 -*-
"""
Fitness 한국인 10종 패치 스크립트
대상 파일: core/presets_meta.py
실행: $env:PYTHONUTF8 = "1"; python preset_builders/patch_fitness_korean_10.py
"""

import re

TARGET_FILE = "core/presets_meta.py"

# ── 1. PRESET_CATEGORIES 블록에 추가 (korean_fitness 카테고리가 이미 있으면 건너뜀)
# 기존 커밋(e325d38)에서 추가된 korean_fitness 블록에 10종 append

NEW_PRESETS = {
    "fitness_korean_tattoo_rio_carnival": {
        "label": "피트니스 타투 리우 카니발",
        "tier": "SS",
        "tags": ["korean", "fitness", "tattoo", "rio", "carnival"],
    },
    "fitness_korean_silver_hair_cliff": {
        "label": "피트니스 실버헤어 제주 절벽",
        "tier": "SS",
        "tags": ["korean", "fitness", "silver_hair", "jeju", "cliff"],
    },
    "fitness_korean_abs_neon_void": {
        "label": "피트니스 복근 네온 보이드",
        "tier": "SS",
        "tags": ["korean", "fitness", "abs", "neon", "void"],
    },
    "fitness_korean_tattoo_thigh_monaco": {
        "label": "피트니스 허벅지타투 모나코",
        "tier": "SS",
        "tags": ["korean", "fitness", "tattoo", "thigh", "monaco"],
    },
    "fitness_korean_mature_40_seoul_penthouse": {
        "label": "피트니스 40세 서울 펜트하우스",
        "tier": "SS",
        "tags": ["korean", "fitness", "mature", "40", "seoul"],
    },
    "fitness_korean_glutes_ibiza_sunset": {
        "label": "피트니스 글루트 이비자 선셋",
        "tier": "SS",
        "tags": ["korean", "fitness", "glutes", "ibiza", "sunset"],
    },
    "fitness_korean_tattoo_sleeve_aurora": {
        "label": "피트니스 슬리브타투 오로라",
        "tier": "SSS",
        "tags": ["korean", "fitness", "tattoo", "sleeve", "aurora"],
    },
    "fitness_korean_abs_seychelles_granite": {
        "label": "피트니스 복근글루트 세이셸",
        "tier": "SS",
        "tags": ["korean", "fitness", "abs", "seychelles", "granite"],
    },
    "fitness_korean_cyber_muscle_ddp": {
        "label": "피트니스 사이버 DDP 서울",
        "tier": "SS",
        "tags": ["korean", "fitness", "cyber", "ddp", "seoul"],
    },
    "fitness_korean_tattoo_full_maldives_void": {
        "label": "피트니스 풀타투 몰디브 나이트",
        "tier": "SSS",
        "tags": ["korean", "fitness", "tattoo", "full", "maldives"],
    },
}

SSS_KEYS = [k for k, v in NEW_PRESETS.items() if v["tier"] == "SSS"]
SS_KEYS  = [k for k, v in NEW_PRESETS.items() if v["tier"] == "SS"]

# ── 앵커 방식 패치 ──────────────────────────────────────────────
with open(TARGET_FILE, "r", encoding="utf-8-sig") as f:
    src = f.read()

# (A) PRESET_CATEGORIES — korean_fitness 블록 끝부분에 삽입
# 기존 블록 마지막 항목 뒤에 추가 (anchor: 마지막으로 커밋된 fitness 키 기준)
# e325d38 커밋 기준 마지막 fitness 키: fitness_korean_elder_40_hanok (또는 유사)
# 안전하게: "korean_fitness" 섹션 CATEGORY 블록의 닫힘 `}` 바로 앞에 삽입

CATEGORIES_ANCHOR = '"korean_fitness": {'

if CATEGORIES_ANCHOR not in src:
    print(f"[ERROR] 앵커를 찾을 수 없습니다: {CATEGORIES_ANCHOR}")
    print("presets_meta.py에 korean_fitness 카테고리 블록이 있는지 확인하세요.")
    exit(1)

# 새 프리셋 카테고리 엔트리 생성
new_entries_block = ""
for key, meta in NEW_PRESETS.items():
    tags_str = ", ".join(f'"{t}"' for t in meta["tags"])
    new_entries_block += f'''        "{key}": {{
            "label": "{meta['label']}",
            "tier": "{meta['tier']}",
            "tags": [{tags_str}],
        }},
'''

# korean_fitness 블록 내 마지막 } 앞에 삽입
# 패턴: "korean_fitness": { ... } 전체에서 마지막 엔트리 뒤 삽입
pattern = r'("korean_fitness":\s*\{)(.*?)(\n    \})'
match = re.search(pattern, src, re.DOTALL)

if not match:
    print("[ERROR] korean_fitness 블록 파싱 실패. 수동으로 확인하세요.")
    exit(1)

# 이미 패치됐는지 확인
if "fitness_korean_tattoo_rio_carnival" in src:
    print("[SKIP] 이미 패치되어 있습니다 (fitness_korean_tattoo_rio_carnival 존재).")
else:
    prefix = match.group(1) + match.group(2)
    suffix = match.group(3)
    patched = src[:match.start()] + prefix + "\n" + new_entries_block + "    " + suffix.lstrip() + src[match.end():]
    src = patched
    print("[OK] PRESET_CATEGORIES korean_fitness 블록에 10종 추가됨.")

# (B) SSS_TIER 리스트에 추가
SSS_ANCHOR = "SSS_TIER = ["
if SSS_ANCHOR not in src:
    print("[ERROR] SSS_TIER 앵커 없음.")
    exit(1)

for key in SSS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SSS_TIER 이미 존재: {key}")
    else:
        src = src.replace(SSS_ANCHOR, SSS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SSS_TIER 추가: {key}")

# (C) SS_TIER 리스트에 추가
SS_ANCHOR = "SS_TIER = ["
if SS_ANCHOR not in src:
    print("[ERROR] SS_TIER 앵커 없음.")
    exit(1)

for key in SS_KEYS:
    if f'"{key}"' in src:
        print(f"[SKIP] SS_TIER 이미 존재: {key}")
    else:
        src = src.replace(SS_ANCHOR, SS_ANCHOR + f'\n    "{key}",')
        print(f"[OK] SS_TIER 추가: {key}")

# ── 파일 저장 ──────────────────────────────────────────────────
with open(TARGET_FILE, "w", encoding="utf-8") as f:
    f.write(src)

print("\n✅ patch_fitness_korean_10.py 완료!")
print(f"   SSS 추가: {SSS_KEYS}")
print(f"   SS  추가: {SS_KEYS}")
