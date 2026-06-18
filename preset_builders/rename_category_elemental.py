"""
patch: 카테고리명 변경
저장위치: C:\Dev\LumineX\preset_builders\rename_category_elemental.py
실행: cd C:\Dev\LumineX && python preset_builders/rename_category_elemental.py
"""

filepath = "dashboard.py"

with open(filepath, encoding="utf-8") as f:
    content = f.read()

old = '"🌋 익스트림 글래머"'
new = '"🌋 엘리멘탈 갓데스"'

c2 = content.replace(old, new)
print("카테고리명 변경 OK" if c2 != content else "FAIL — anchor 못 찾음")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(c2)

print("패치 완료")
