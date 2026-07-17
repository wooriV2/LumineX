with open('core/presets_meta.py', 'r', encoding='utf-8') as f:
    lines = f.readlines()
# 3465~3480번 줄 확인
for i, line in enumerate(lines[3460:3485], start=3461):
    print(f"{i}: {line}", end="")
