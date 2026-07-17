with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# 3471~3485번 라인 직접 제거 (0-indexed: 3470~3484)
remove_range = set(range(3470, 3485))
new_lines = [line for i, line in enumerate(lines) if i not in remove_range]

import ast
content = ''.join(new_lines)
try:
    ast.parse(content)
    print("문법 OK")
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print("저장 완료!")
except SyntaxError as e:
    print(f"오류: {e}")
    err_lines = content.split('\n')
    for i, l in enumerate(err_lines[max(0,e.lineno-4):e.lineno+3], start=max(1,e.lineno-3)):
        print(f"  {i}: {l}")
