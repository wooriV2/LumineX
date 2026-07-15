# -*- coding: utf-8 -*-
"""
presets_meta.py 끝부분 구조 진단
실행: $env:PYTHONUTF8 = "1"; python preset_builders/diagnose_meta.py
"""

META_FILE = "core/presets_meta.py"

with open(META_FILE, encoding="utf-8-sig") as f:
    content = f.read()

# PRESET_CATEGORIES 딕셔너리가 끝나는 위치 찾기
idx = content.find("PRESET_CATEGORIES")
print(f"PRESET_CATEGORIES 위치: {idx}")

# SSS_TIER 위치
idx_sss = content.find("SSS_TIER")
print(f"SSS_TIER 위치: {idx_sss}")

# from core.hof_tier 위치
idx_hof = content.find("from core.hof_tier")
print(f"from core.hof_tier 위치: {idx_hof}")

# PRESET_CATEGORIES 끝 ~ SSS_TIER 사이 내용 출력
if idx_sss > 0:
    # PRESET_CATEGORIES 닫힘 } 찾기 (SSS_TIER 직전)
    segment = content[idx_sss - 300 : idx_sss + 50]
    print("\n[SSS_TIER 앞 300자]")
    print(repr(segment))

# SSS_TIER = { 앞 50자
if idx_sss > 0:
    print("\n[SSS_TIER 라인 주변]")
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if "SSS_TIER" in line or "from core.hof_tier" in line:
            start = max(0, i-3)
            end = min(len(lines), i+4)
            for j in range(start, end):
                print(f"  {j+1:4d}: {repr(lines[j])}")
            print()
