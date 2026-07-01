"""
미생성 2종 제거 패치
- duo_storm_and_calm_bodypaint  (658, 854, 1879번 줄)
- trio_angel_human_demon_bodypaint (해당 줄)
dashboard.py에서 해당 줄 완전 삭제
"""

from pathlib import Path

DASHBOARD = Path("C:/Dev/LumineX/dashboard.py")

TARGETS = [
    '"duo_storm_and_calm_bodypaint"',
    '"trio_angel_human_demon_bodypaint"',
]

content = DASHBOARD.read_text(encoding='utf-8')
lines = content.splitlines(keepends=True)

removed = []
kept = []
for i, line in enumerate(lines, 1):
    stripped = line.strip().rstrip(',')
    if any(t in line for t in TARGETS):
        removed.append((i, line.rstrip()))
    else:
        kept.append(line)

print(f"제거된 줄 ({len(removed)}개):")
for lineno, text in removed:
    print(f"  [{lineno}] {text.strip()}")

result = ''.join(kept)
DASHBOARD.write_text(result, encoding='utf-8')
print(f"\n✅ 저장 완료: {DASHBOARD}")

# 검증
check = result.count('"duo_storm_and_calm_bodypaint"')
check2 = result.count('"trio_angel_human_demon_bodypaint"')
print(f"\n검증:")
print(f"  duo_storm_and_calm_bodypaint 남은 수: {check} {'✅' if check==0 else '❌'}")
print(f"  trio_angel_human_demon_bodypaint 남은 수: {check2} {'✅' if check2==0 else '❌'}")
