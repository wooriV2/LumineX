# fix_sss_tier.py
# 실행: python preset_builders/fix_sss_tier.py

FILE = "core/sss_tier.py"

with open(FILE, encoding="utf-8-sig") as f:
    content = f.read()

# } 닫힌 후 바깥에 붙은 trio 항목들 추출
trio_lines = []
remaining = []
after_close = False

lines = content.split("\n")
new_lines = []

for line in lines:
    if line.strip() == "}":
        after_close = True
        # } 는 일단 보류
        continue
    if after_close:
        stripped = line.strip()
        if stripped.startswith('"trio_bae'):
            # } 안으로 넣을 항목
            trio_lines.append(f'    {stripped}')
        else:
            # 예상치 못한 줄 — 그냥 유지
            remaining.append(line)
    else:
        new_lines.append(line)

# trio_lines를 } 앞에 삽입 후 } 닫기
for t in trio_lines:
    new_lines.append(t)
new_lines.append("}")

# remaining 있으면 뒤에 추가
for r in remaining:
    if r.strip():
        new_lines.append(r)

fixed = "\n".join(new_lines)

with open(FILE, "w", encoding="utf-8") as f:
    f.write(fixed)

# 검증
import ast
ast.parse(open(FILE, encoding="utf-8").read())
print("✅ sss_tier.py 수정 완료")

# 마지막 15줄 확인
lines_check = fixed.split("\n")
print("\n[마지막 15줄]")
for l in lines_check[-15:]:
    print(l)
