with open('core/presets_meta.py', 'rb') as f:
    content = f.read()
print(repr(content[-100:]))
