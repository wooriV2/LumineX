with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i, line in enumerate(lines[3465:3490], start=3466):
    print(f"{i}: {repr(line)}")
