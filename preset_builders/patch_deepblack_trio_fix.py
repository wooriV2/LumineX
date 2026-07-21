# -*- coding: utf-8 -*-
"""
DeepBlack Trio 수정 패치
1. hof_tier.py 중복 } 제거
2. sss_tier.py 중복 } 제거
3. presets_meta.py 카테고리 추가

실행: $env:PYTHONUTF8="1"; python preset_builders/patch_deepblack_trio_fix.py
"""

import re

# ============================================================
# 1. hof_tier.py 중복 } 제거
# ============================================================

HOF_PATH = "core/hof_tier.py"

with open(HOF_PATH, encoding="utf-8-sig") as f:
    hof = f.read()

# },\n} 패턴 → 마지막 } 하나만 남기기
# 현재: ...\n    },\n}\n} 
# 목표: ...\n    },\n}
hof_fixed = re.sub(r'\}\s*\n\}(\s*)$', '}\n', hof)

with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof_fixed)

print("✅ hof_tier.py 중복 } 제거 완료")

# ============================================================
# 2. sss_tier.py 중복 } 제거
# ============================================================

SSS_PATH = "core/sss_tier.py"

with open(SSS_PATH, encoding="utf-8-sig") as f:
    sss = f.read()

sss_fixed = re.sub(r'\}\s*\n\}(\s*)$', '}\n', sss)

with open(SSS_PATH, "w", encoding="utf-8") as f:
    f.write(sss_fixed)

print("✅ sss_tier.py 중복 } 제거 완료")

# ============================================================
# 3. presets_meta.py 카테고리 추가
# presets_meta.py:730 마지막 } 앞에 삽입
# ============================================================

META_PATH = "core/presets_meta.py"

with open(META_PATH, encoding="utf-8-sig") as f:
    meta = f.read()

# 이미 추가됐는지 확인
if "DeepBlack Trio" in meta:
    print("⚠️ presets_meta.py 이미 DeepBlack Trio 존재 — 스킵")
else:
    NEW_CATEGORY = '''    "\U0001f5a4 DeepBlack Trio": [
        "deepblack_trio_dragon_phoenix_tiger_void",
        "deepblack_trio_koi_dragon_phoenix_aurora",
        "deepblack_trio_dragon_celadon_phoenix_void",
        "deepblack_trio_koi_crane_phoenix_aurora",
        "deepblack_trio_dragon_goldleaf_phoenix_void",
        "deepblack_trio_tiger_uvneon_koi_void",
        "deepblack_trio_uvneon_dragon_phoenix_tiger_void",
    ],\n'''

    # 마지막 } 앞에 삽입
    meta_fixed = re.sub(r'\n\}(\s*)$', '\n' + NEW_CATEGORY + '}\n', meta)

    with open(META_PATH, "w", encoding="utf-8") as f:
        f.write(meta_fixed)

    print("✅ presets_meta.py DeepBlack Trio 카테고리 추가 완료")

print("\n🎉 수정 패치 완료! AST 검증을 실행하세요.")
