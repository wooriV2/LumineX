# fix_sss_tier2.py
FILE = "core/sss_tier.py"

with open(FILE, encoding="utf-8-sig") as f:
    content = f.read()

# 마지막 항목에 , 가 있고 } 가 없는 상태 → } 추가
# 마지막 줄이 "zhangjiajie_avatar", 로 끝남
content = content.rstrip()
if not content.endswith("}"):
    content += "\n}"

with open(FILE, "w", encoding="utf-8") as f:
    f.write(content)

# 검증
import ast
ast.parse(open(FILE, encoding="utf-8").read())
print("✅ sss_tier.py 수정 완료")

with open(FILE, encoding="utf-8") as f:
    lines = f.readlines()
print(f"총 줄 수: {len(lines)}")
print("\n[마지막 5줄]")
for l in lines[-5:]:
    print(repr(l))
