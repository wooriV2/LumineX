import ast, re

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 고아 키 패턴: 4칸 들여쓰기 + "키", 로 끝나는 라인
pattern = re.compile(r'^    "[a-zA-Z0-9_]+",\s*$')

new_lines = []
removed = 0
for i, line in enumerate(lines, 1):
    if pattern.match(line):
        print(f"제거 {i}: {line.rstrip()}")
        removed += 1
    else:
        new_lines.append(line)

print(f"\n제거 {removed}개")
content = ''.join(new_lines)

try:
    ast.parse(content)
    print("문법 OK — 저장")
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("완료!")
except SyntaxError as e:
    print(f"오류: {e}")
    el = content.split('\n')
    for i, l in enumerate(el[max(0,e.lineno-4):e.lineno+3], start=max(1,e.lineno-3)):
        print(f"  {i}: {l}")
