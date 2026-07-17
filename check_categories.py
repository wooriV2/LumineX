import re
with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

keys = re.findall(r'    "([^"]+)":\s*\[', content)
print(f'총 카테고리: {len(keys)}개')
for k in keys:
    print(k)
