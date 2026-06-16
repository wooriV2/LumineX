"""
patch_v26_tiers.py
dashboard.py의 SSS_TIER / SS_TIER set에 v26 월드 랜드마크 프리셋 추가

실행: python preset_builders/patch_v26_tiers.py
"""

from pathlib import Path
import re

DASHBOARD = Path(r"C:\Dev\LumineX\dashboard.py")

# ── 추가할 프리셋 ──────────────────────────────────────────
NEW_SSS = [
    "positano_cliff",
    "bruges_canal",
    "colosseum_dusk",
    "alhambra_palace",
    "mont_saint_michel",
    "sigiriya_rock",
    "angkor_thom_faces",
    "teotihuacan_pyramid",
    "palmyra_colonnade",
]

NEW_SS = [
    "cinque_terre_harbor",
    "karnak_temple",
    "chichen_itza_pyramid",
    "gobekli_tepe",
]

# ── SSS는 SS에도 포함시켜야 함 (기존 패턴) ────────────────
NEW_SS_FROM_SSS = NEW_SSS  # SSS_TIER도 SS_TIER에 중복 등록 (dashboard 로직)

src = DASHBOARD.read_text(encoding="utf-8")

# ── SSS_TIER에 추가 ────────────────────────────────────────
SSS_COMMENT = "    # 2026-06-13 v26 월드 랜드마크 SSS 확정\n"
SSS_LINES = SSS_COMMENT
for p in NEW_SSS:
    SSS_LINES += f'    "{p}",\n'

# SSS_TIER closing brace 바로 앞에 삽입
src = re.sub(
    r'(    "ellora_rock_temple",[^\n]*\n)(})',
    lambda m: m.group(1) + SSS_LINES + m.group(2),
    src,
    count=1
)

# ── SS_TIER에 추가 (SSS 포함 + 순수 SS) ───────────────────
SS_COMMENT = "    # 2026-06-13 v26 월드 랜드마크 SS/SSS 확정\n"
SS_LINES = SS_COMMENT
for p in NEW_SSS + NEW_SS:
    SS_LINES += f'    "{p}",\n'

# SS_TIER 마지막 항목("ellora_rock_temple" SS 중복 등록 라인) 뒤에 삽입
src = re.sub(
    r'("ellora_rock_temple",\n)(})',
    lambda m: m.group(1) + SS_LINES + m.group(2),
    src,
    count=1
)

DASHBOARD.write_text(src, encoding="utf-8")

print("=" * 50)
print("LumineX v26 Tier Patch — dashboard.py")
print("=" * 50)
print(f"\nSSS_TIER 추가 ({len(NEW_SSS)}개):")
for p in NEW_SSS:
    print(f"  + {p}")
print(f"\nSS_TIER 추가 ({len(NEW_SSS + NEW_SS)}개):")
for p in NEW_SSS + NEW_SS:
    print(f"  + {p}")
print("\n✅ 완료")
print("\n검증:")
print('  Select-String -Path dashboard.py -Pattern "positano_cliff|palmyra_colonnade" | Select-Object LineNumber, Line')
