with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    content = f.read()

# ],만 있는 줄 찾기
lines = content.split('\n')
for i, line in enumerate(lines):
    if line.strip() == '],':
        print(f'Line {i+1}: prev={repr(lines[i-1][:50])}')
        print(f'Line {i+1}: this={repr(line)}')
        print(f'Line {i+1}: next={repr(lines[i+1][:50])}')
        print()
