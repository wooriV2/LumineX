"""
patch_wet_presets.py
wet_white_shirt / rain_bodysuit 프리셋 수정

문제:
- wet_white_shirt: 하의가 청바지로 나옴, 투명도 부족
- rain_bodysuit: 운동복+재킷으로 나옴, 시스루 안됨

실행: python preset_builders/patch_wet_presets.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")

# ── wet_white_shirt 수정 ──────────────────────────────────
wet_white_shirt = {
    "tag": "Wet White Shirt",
    "subject": "a soaking wet white shirt only female model",
    "body": "VS Angel body, toned slim figure, every curve visible through soaked translucent fabric",
    "outfit": "oversized white dress shirt ONLY, completely soaked and translucent, clinging to bare skin, shirt barely covers hips, nothing underneath, wet fabric see-through, buttons undone at top",
    "material": "soaked white cotton shirt, fully translucent when wet, second-skin wet clinging, bare legs visible below shirt hem",
    "environment": "rain-soaked alley at night, neon reflections in puddles, steam rising from grates",
    "lighting": "dramatic backlit neon light, wet fabric glow, rain streak illumination, translucent fabric backlight",
    "style": "wet shirt editorial, rain-soaked glamour photography, provocative fashion, shirt-only minimal",
    "quality": "shot on Sony A7R V, dramatic rain grade, portrait 2:3 vertical"
}

# ── rain_bodysuit 수정 ────────────────────────────────────
rain_bodysuit = {
    "tag": "Rain Bodysuit",
    "subject": "a rain-soaked sheer bodysuit female model",
    "body": "athletic fitness model, sleek wet body, every curve defined by skin-tight wet sheer suit",
    "outfit": "ultra-sheer bodysuit completely soaked in rain, skin-tight transparent second skin, body fully visible through wet sheer fabric, high-cut legs, no layering, no jacket",
    "material": "soaked sheer mesh bodysuit, fully transparent when wet, bare skin visible through fabric, wet second-skin effect",
    "environment": "heavy rain rooftop at night, dramatic storm, city lights blurred behind rain curtain",
    "lighting": "dramatic stormy backlight, rain streak illumination, wet sheer fabric backlit glow, skin visible through fabric",
    "style": "storm sheer bodysuit editorial, rain-drenched glamour photography, transparent wet fashion",
    "quality": "shot on Canon EOS R5, stormy dramatic grade, portrait 2:3 vertical"
}

for filename, data in [("wet_white_shirt", wet_white_shirt), ("rain_bodysuit", rain_bodysuit)]:
    path = PRESETS_DIR / f"{filename}.json"
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"✅ {filename}.json 수정 완료")

print("\n검증:")
print('  Get-Content C:\\Dev\\LumineX\\presets\\wet_white_shirt.json')
