with open('core/hof_tier.py', 'r', encoding='utf-8') as f:
    content = f.read()

old = '    "young_korean_debut_red_carpet",\n\ndef add_hof'
new = '    "young_korean_debut_red_carpet",\n}\n\ndef add_hof'

if old in content:
    content = content.replace(old, new)
    with open('core/hof_tier.py', 'w', encoding='utf-8') as f:
        f.write(content)
    print('수정 완료!')
else:
    print('패턴 못 찾음')
