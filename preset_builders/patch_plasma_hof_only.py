"""
patch_plasma_hof_only.py
=========================
plasma_plus_size_solar_flare_crown HOF_TIER 삽입

저장: C:\\Dev\\LumineX\\preset_builders\\patch_plasma_hof_only.py
실행: python preset_builders/patch_plasma_hof_only.py
"""

from pathlib import Path

HOF_PATH = Path("C:/Dev/LumineX/core/hof_tier.py")
TARGET   = '"plasma_plus_size_solar_flare_crown"'
ANCHOR   = '"plasma_curvy_solar_wind_wet",'

def patch():
    content = HOF_PATH.read_text(encoding="utf-8")

    if TARGET in content:
        print("✅ 이미 존재 — SKIP")
        return

    if ANCHOR not in content:
        print(f"❌ 앵커 없음: {ANCHOR}")
        return

    new_content = content.replace(
        ANCHOR,
        ANCHOR + f'\n    {TARGET},'
    )

    HOF_PATH.write_text(new_content, encoding="utf-8")

    ok = TARGET in HOF_PATH.read_text(encoding="utf-8")
    print(f"{'✅' if ok else '❌'} plasma_plus_size_solar_flare_crown")

    if ok:
        print("\n다음 단계:")
        print("  git add core/presets_meta.py core/hof_tier.py")
        print('  git commit -m "feat: Acoustic Levitation Glamour 12종 추가 HOF 4종 + plasma HOF 승격"')
        print("  git push")

if __name__ == "__main__":
    patch()
