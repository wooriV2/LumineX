"""
delete_elite_motion.py
======================
elite_motion 완전 삭제
1. presets/elite_motion.json 삭제
2. dashboard.py에서 참조 제거

실행: python delete_elite_motion.py
"""

from pathlib import Path

DASHBOARD = Path("dashboard.py")
PRESET = Path("presets/elite_motion.json")

# 1. JSON 삭제
if PRESET.exists():
    PRESET.unlink()
    print("✅ elite_motion.json 삭제 완료")
else:
    print("⚠️  elite_motion.json 없음 (이미 삭제됨)")

# 2. dashboard.py 참조 제거
content = DASHBOARD.read_text(encoding="utf-8")

if '"elite_motion"' in content:
    content = content.replace('"elite_motion",\n', '')
    content = content.replace('"elite_motion",', '')
    content = content.replace('"elite_motion"', '')
    DASHBOARD.write_text(content, encoding="utf-8")
    print("✅ dashboard.py 참조 제거 완료")
else:
    print("ℹ️  dashboard.py에 elite_motion 참조 없음")

# 3. 검증
print("\n[ 검증 ]")
print(f"  elite_motion.json 존재: {PRESET.exists()}")
verify = DASHBOARD.read_text(encoding="utf-8")
print(f"  dashboard.py 잔존 여부: {'elite_motion' in verify}")

print("\n완료! 커밋:")
print('  git add -A')
print('  git commit -m "fix: elite_motion 삭제"')
print('  git push')
