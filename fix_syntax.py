with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '    "hanbok_wet_editorial", "joseon_boudoir",\n\n\n\n    "\U0001f3a4 K-Idol \ud55c\uad6d\uc778"'
new = '    "hanbok_wet_editorial", "joseon_boudoir",\n\n],\n\n    "\U0001f3a4 K-Idol \ud55c\uad6d\uc778"'

if old in content:
    content = content.replace(old, new)
    with open('core/presets_meta.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('수정 완료!')
else:
    print('패턴 못 찾음')
