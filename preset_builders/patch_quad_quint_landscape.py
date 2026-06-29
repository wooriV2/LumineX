"""
patch_quad_quint_landscape.py
quad 5종 + quint 4종 프리셋에 가로 16:9 추가
실행: python preset_builders/patch_quad_quint_landscape.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")

TARGETS = [
    "quad_four_seasons_bodypaint",
    "quad_four_elements_bodypaint",
    "quad_four_directions_bodypaint",
    "quad_four_seasons_klimt_bodypaint",
    "quad_rgba_spectrum_bodypaint",
    "quint_five_continents_bodypaint",
    "quint_five_elements_asia_bodypaint",
    "quint_rainbow_five_bodypaint",
    "quint_five_oceans_bodypaint",
]

LANDSCAPE_SUFFIX = ", Wide landscape 16:9 horizontal format, panoramic composition showing all models clearly side by side"

def patch():
    patched = []
    for name in TARGETS:
        path = PRESETS_DIR / f"{name}.json"
        if not path.exists():
            print(f"  ❌ 없음: {name}.json")
            continue

        with open(path, encoding="utf-8") as f:
            preset = json.load(f)

        # environment에 가로 suffix 추가 (중복 방지)
        env = preset.get("environment", "")
        if "16:9" not in env:
            preset["environment"] = env + LANDSCAPE_SUFFIX

        # quality에도 추가
        quality = preset.get("quality", "")
        if "16:9" not in quality:
            preset["quality"] = quality + ", wide 16:9 panoramic format"

        with open(path, "w", encoding="utf-8") as f:
            json.dump(preset, f, ensure_ascii=False, indent=2)

        print(f"  ✅ {name}.json")
        patched.append(name)

    print(f"\n총 {len(patched)}종 패치 완료")

if __name__ == "__main__":
    print("🎨 quad/quint 가로 16:9 패치\n")
    patch()
