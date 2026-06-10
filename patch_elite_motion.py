"""
patch_elite_motion.py
======================
elite_motion.json 근본 수정
- athletic/performance/training 키워드 완전 제거
- 럭셔리 패션 에디토리얼 + 역동적 실루엣으로 재정의

실행: python patch_elite_motion.py
"""

import json
from pathlib import Path

PRESET_PATH = Path("presets/elite_motion.json")

NEW_DATA = {
    "tag": "Elite Motion",
    "subject": "a powerful glamorous woman in motion",
    "body": "tall commanding figure, fierce confident stride, full body shot",
    "outfit": "sculptural cutout mini dress, architectural fabric panels, bold geometric cutouts",
    "material": "matte stretch scuba fabric, structured bonded panels, razor-sharp seams",
    "environment": "high-fashion studio, polished concrete floor, dramatic shadow play",
    "lighting": "high-contrast editorial strobe, strong directional light, sharp shadows",
    "style": "avant-garde fashion editorial, high-fashion magazine, architectural fashion photography",
    "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
}

# 백업
backup_path = Path("presets/_bak_elite_motion.json")
if PRESET_PATH.exists():
    old_data = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
    backup_path.write_text(json.dumps(old_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"✅ 백업 저장: {backup_path}")
else:
    print("⚠️  elite_motion.json 없음 — 경로 확인 필요")

# 수정
PRESET_PATH.write_text(json.dumps(NEW_DATA, ensure_ascii=False, indent=2), encoding="utf-8")
print("✅ elite_motion.json 수정 완료")

# 검증 출력
print("\n[ 수정 후 내용 ]")
verify = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
for k, v in verify.items():
    print(f"  {k}: {v}")

# 위험 키워드 잔존 체크
danger_words = ["athletic", "performance", "training", "sport", "fitness", "aerodynamic"]
content_str = json.dumps(verify).lower()
found = [w for w in danger_words if w in content_str]
if found:
    print(f"\n⚠️  위험 키워드 잔존: {found}")
else:
    print("\n✅ 위험 키워드 없음 — 안전")
