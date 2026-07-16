with open('core/presets_meta.py', 'rb') as f:
    content = f.read()
print(f'파일 크기: {len(content)} bytes')
# 첫 10바이트 확인
print(f'첫 10바이트: {content[:10]}')
# 마지막 10바이트 확인  
print(f'마지막 10바이트: {content[-10:]}')
