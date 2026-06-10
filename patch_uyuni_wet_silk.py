"""
patch_uyuni_wet_silk.py
========================
uyuni_wet_silk 웨트룩 강화
- "walking out of water" 상황 명시
- 젖은 드레스 투명/밀착 직접 기술

실행: python patch_uyuni_wet_silk.py
"""

import json
from pathlib import Path

PRESET_PATH = Path("presets/uyuni_wet_silk.json")

NEW_DATA = {
    "tag": "Uyuni Wet Silk",
    "subject": "a sensual goddess woman walking out of shallow water, dress completely drenched and transparent, soaked white silk plastered to every curve of her body",
    "body": "soaking wet body, transparent wet dress clinging to skin revealing full silhouette, water dripping, full body shot",
    "outfit": "",
    "material": "",
    "environment": "Bolivia Uyuni salt flat, perfect mirror reflection of sky, shallow water layer, infinite horizon, golden hour sky reflection in water",
    "lighting": "golden hour light on wet transparent fabric, warm glow on glistening skin, breathtaking salt flat symmetry",
    "style": "wet editorial fashion photography, soaking wet luxury glamour, body-revealing wet silk",
    "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
}

# 백업
bak = Path("presets/_bak_uyuni_wet_silk.json")
old = json.loads(PRESET_PATH.read_text(encoding="utf-8"))
bak.write_text(json.dumps(old, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"✅ 백업: {bak}")

# 저장
PRESET_PATH.write_text(json.dumps(NEW_DATA, ensure_ascii=False, indent=2), encoding="utf-8")
print("✅ uyuni_wet_silk.json 수정 완료")

print("\n[ 수정 후 subject ]")
print(f"  {NEW_DATA['subject']}")
print(f"\n[ 수정 후 body ]")
print(f"  {NEW_DATA['body']}")

print("\n커밋:")
print('  git add -A')
print('  git commit -m "fix: uyuni_wet_silk 웨트룩 강화"')
print('  git push')
