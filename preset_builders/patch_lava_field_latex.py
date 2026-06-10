"""
preset_builders/patch_lava_field_latex.py
==========================================
lava_field_latex 글래머/섹시 강화
- subject: 글래머 goddess + 노출 암시 강화
- body: barely-there, skin-baring 명시
- style: 럭셔리 글래머 방향 강화

실행: python preset_builders/patch_lava_field_latex.py
"""

import json
from pathlib import Path

PRESET_PATH = Path("presets/lava_field_latex.json")

NEW_DATA = {
    "tag": "Lava Field Latex",
    "subject": "a fearless volcanic goddess woman, barely-there glossy outfit melting into lava glow, skin glistening from extreme heat",
    "body": "barely-there coverage, skin-baring second-skin silhouette, lava-kissed glistening skin, powerful commanding stance, full body shot",
    "outfit": "",
    "material": "",
    "environment": "active Hawaiian lava field at night, glowing red orange lava flows surrounding her, volcanic rock, intense heat shimmer, steam vents erupting, molten rivers of lava",
    "lighting": "intense red orange lava glow on bare skin, dramatic upward lava light, deep volcanic shadows, heat shimmer distortion around silhouette",
    "style": "volcanic goddess glamour editorial, lava glow luxury fashion photography, infernal sensual beauty, barely-there lava glam",
    "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"
}

PRESET_PATH.write_text(json.dumps(NEW_DATA, ensure_ascii=False, indent=2), encoding="utf-8")
print("✅ lava_field_latex.json 수정 완료")
print(f"\nsubject: {NEW_DATA['subject']}")
print(f"body: {NEW_DATA['body']}")
print(f"style: {NEW_DATA['style']}")

print("\n커밋:")
print('  git add -A')
print('  git commit -m "fix: lava_field_latex 글래머 강화"')
print('  git push')
