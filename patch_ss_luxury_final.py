"""
patch_ss_luxury_final.py
=========================
럭셔리 글래머 나머지 SS 12종 등록
champagne_mist, couture_heat, casino_royale, black_tie_gala,
champagne_tower, plunge_gown, slit_maxi, cutout_bodysuit,
jeweled_bikini_top, golden_drape_goddess, penthouse_glam, serpentine_dress

실행: python patch_ss_luxury_final.py
"""

import re
from pathlib import Path

DASHBOARD = Path("dashboard.py")

NEW_SS = [
    "champagne_mist",
    "couture_heat",
    "casino_royale",
    "black_tie_gala",
    "champagne_tower",
    "plunge_gown",
    "slit_maxi",
    "cutout_bodysuit",
    "jeweled_bikini_top",
    "golden_drape_goddess",
    "penthouse_glam",
    "serpentine_dress",
]

print("=" * 50)
print("patch_ss_luxury_final.py 시작")
print("=" * 50)

content = DASHBOARD.read_text(encoding="utf-8")

# SS_TIER 블록 추출
ss_match = re.search(r'(SS_TIER\s*=\s*\{)([^}]+)(\})', content, re.DOTALL)
if not ss_match:
    print("❌ SS_TIER 블록 찾기 실패 — 수동 확인 필요")
    exit(1)

ss_block = ss_match.group(2)

# 이미 등록된 것 필터링
already = [p for p in NEW_SS if p in ss_block]
to_add  = [p for p in NEW_SS if p not in ss_block]

if already:
    print(f"이미 SS_TIER에 있음 (스킵): {already}")

if not to_add:
    print("추가할 항목 없음 — 이미 모두 등록됨")
    exit(0)

# 새 항목 추가
new_entries = "\n" + "\n".join(f'    "{p}",' for p in to_add)
new_content = content.replace(
    ss_match.group(0),
    ss_match.group(1) + ss_block.rstrip() + new_entries + "\n" + ss_match.group(3)
)

if new_content == content:
    print("❌ 교체 실패 — 수동 확인 필요")
    exit(1)

DASHBOARD.write_text(new_content, encoding="utf-8")
print(f"✅ SS_TIER 추가 완료: {to_add}")

# 검증
print("\n[ 검증 ]")
verify = DASHBOARD.read_text(encoding="utf-8")
ss_match2 = re.search(r'SS_TIER\s*=\s*\{([^}]+)\}', verify, re.DOTALL)
ss_block2 = ss_match2.group(1) if ss_match2 else ""

for p in NEW_SS:
    status = "✅" if p in ss_block2 else "❌"
    print(f"  {status} {p}")

ss_count = len(re.findall(r'"[\w_]+"', ss_block2))
print(f"\n  SS_TIER 총 항목 수: {ss_count}개")
print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "v33: 럭셔리 글래머 SS 12종 추가 확정"')
print('  git push')
