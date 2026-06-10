"""
patch_ss_power_edge.py
=======================
⚔️ 파워 & 엣지 SS 6종 등록
valkyrie_storm, shadow_play, power_suit,
shadow_queen, bioluminescent, punk_queen

실행: python patch_ss_power_edge.py
"""

import re
from pathlib import Path

DASHBOARD = Path("dashboard.py")

NEW_SS = [
    "valkyrie_storm",
    "shadow_play",
    "power_suit",
    "shadow_queen",
    "bioluminescent",
    "punk_queen",
]

print("=" * 50)
print("patch_ss_power_edge.py 시작")
print("=" * 50)

content = DASHBOARD.read_text(encoding="utf-8")

ss_match = re.search(r'(SS_TIER\s*=\s*\{)([^}]+)(\})', content, re.DOTALL)
if not ss_match:
    print("❌ SS_TIER 블록 찾기 실패")
    exit(1)

ss_block = ss_match.group(2)

already = [p for p in NEW_SS if p in ss_block]
to_add  = [p for p in NEW_SS if p not in ss_block]

if already:
    print(f"이미 등록됨 (스킵): {already}")

if not to_add:
    print("추가할 항목 없음")
    exit(0)

new_entries = "\n" + "\n".join(f'    "{p}",' for p in to_add)
new_content = content.replace(
    ss_match.group(0),
    ss_match.group(1) + ss_block.rstrip() + new_entries + "\n" + ss_match.group(3)
)

if new_content == content:
    print("❌ 교체 실패")
    exit(1)

DASHBOARD.write_text(new_content, encoding="utf-8")
print(f"✅ SS_TIER 추가: {to_add}")

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
print('  git commit -m "v34: ⚔️ 파워&엣지 SS 6종 등록"')
print('  git push')
