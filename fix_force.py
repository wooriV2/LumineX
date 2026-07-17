import re

with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()

pattern = re.compile(r'^    "[a-zA-Z0-9_]+",\s*$')
new_lines = [l for l in lines if not pattern.match(l)]

print(f"제거: {len(lines) - len(new_lines)}개")

with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)
print("저장 완료")
