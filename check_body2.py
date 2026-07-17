with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 체형 섹션 찾기
idx = content.find('체형')
print(repr(content[idx-100:idx+500]))
