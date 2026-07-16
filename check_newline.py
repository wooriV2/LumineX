with open('core/presets_meta.py', 'rb') as f:
    content = f.read()
cr = content.count(b'\r')
lf = content.count(b'\n')
crlf = content.count(b'\r\n')
print(f"CR: {cr}, LF: {lf}, CRLF: {crlf}")
