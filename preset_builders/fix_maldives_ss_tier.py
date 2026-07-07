"""
fix_maldives_ss_tier.py
SS_TIER의 깨진 maldives_bikini_editorial 항목 수정
"""
from pathlib import Path

TARGET = Path("C:/Dev/LumineX/dashboard.py")
content = TARGET.read_text(encoding="utf-8")

# 깨진 항목 찾아서 교체
# 가능한 패턴들 모두 처리
bad_patterns = [
    '    " maldives_bikini_editorial\\,\n',
    '    " maldives_bikini_editorial\,\n',
    '    "maldives_bikini_editorial\\,\n',
    ' "maldives_bikini_editorial\\,\n',
]

fixed = False
for bad in bad_patterns:
    if bad in content:
        content = content.replace(bad, '    "maldives_bikini_editorial",\n', 1)
        print(f"✅ 수정 완료: {repr(bad)} → 정상")
        fixed = True
        break

if not fixed:
    # 정규식으로 찾기
    import re
    pattern = r'[ ]*"[ ]*maldives_bikini_editorial[\\,"]+'
    match = re.search(pattern, content)
    if match:
        content = content[:match.start()] + '    "maldives_bikini_editorial",' + content[match.end():]
        print(f"✅ 정규식으로 수정 완료")
        fixed = True

if not fixed:
    print("❌ 깨진 항목을 찾지 못했습니다")
    # 현재 상태 출력
    for i, line in enumerate(content.splitlines()):
        if "maldives" in line:
            print(f"  line {i+1}: {repr(line)}")
else:
    TARGET.write_text(content, encoding="utf-8")
    print("✅ dashboard.py 저장 완료")

# 최종 확인
for i, line in enumerate(content.splitlines()):
    if "maldives" in line:
        print(f"  확인 line {i+1}: {repr(line)}")
