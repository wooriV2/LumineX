with open('core/presets_meta.py', 'r', encoding='utf-8-sig') as f:
    content = f.read()
with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("BOM 제거 완료")
