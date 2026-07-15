"""
patch_acoustic_levitation.py
=============================
작업 내용:
  1. presets_meta.py — 🔊 Acoustic Levitation Glamour 카테고리 12종 추가
  2. hof_tier.py     — HOF 4종 추가
                       (mercury_drop_curtain / fire_ember_levitation /
                        flower_petal_vortex / ice_shard_armor)
  3. hof_tier.py     — plasma_plus_size_solar_flare_crown SSS → HOF 승격

저장 위치: C:\\Dev\\LumineX\\preset_builders\\patch_acoustic_levitation.py
실행: python preset_builders/patch_acoustic_levitation.py
"""

import re
from pathlib import Path

BASE = Path("C:/Dev/LumineX")
META_PATH = BASE / "core/presets_meta.py"
HOF_PATH  = BASE / "core/hof_tier.py"

# ── 1. 신규 프리셋 데이터 ──────────────────────────────────────────────────

ACOUSTIC_CATEGORY = '    "🔊 Acoustic Levitation Glamour"'

ACOUSTIC_PRESETS = '''\
    "🔊 Acoustic Levitation Glamour": [
        {
            "id": "acoustic_amazon_glass_shard_levitation",
            "name": "Glass Shard Levitation",
            "prompt": "Professional fashion photograph, full body shot. Model: towering amazon goddess, hundreds of razor-sharp glass shards levitating in acoustic nodes around her powerful figure — glass suspended mid-air in precise sound field architecture. Body: 183cm powerful physique, copper skin, natural afro halo, fierce warrior expression. Wearing: minimal silver metallic micro bikini — glass shards of varying sizes suspended 2-30cm from skin creating living glass armor without touching her, clear platform stiletto thigh-high boots 6-inch heel visible through glass constellation, silver cuff bracelets. Environment: dark industrial studio, glass shards catching studio lights as scattered crystal prisms, acoustic transducer array visible at frame edges. Lighting: hard directional silver light, each glass shard creating prismatic rainbow, copper skin reflecting glass light. Style: amazon acoustic glass editorial, sound as weapon. Shot on Phase One XF IQ4, acoustic glass grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_plus_size_water_sphere_cloud",
            "name": "Water Sphere Cloud",
            "prompt": "Professional fashion photograph, full body shot. Model: magnificent plus-size goddess surrounded by acoustic water sphere cloud — thousands of perfect water spheres 1-5cm diameter levitating in acoustic nodes creating total water atmosphere. Body: full magnificent curves, deep ebony skin, voluminous natural locs, serene expression commanding the water. Wearing: ultra-minimal black micro bodysuit — water spheres surrounding every curve highlighting silhouette, spheres refracting body into thousands of tiny reflections, black patent thigh-high platform boots 5-inch heel with water spheres orbiting at ankle and knee nodes, no jewelry — water is everything. Environment: dark studio, water spheres filling entire frame as living cloud, figure at center of sphere density, light refracting through water creating rainbow halos. Lighting: single overhead white beam, water spheres acting as lenses creating caustic patterns on skin and floor. Style: plus-size acoustic water sphere editorial, sound holding water in air. Shot on Hasselblad X2D, acoustic water grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_petite_salt_crystal_formation",
            "name": "Salt Crystal Formation",
            "prompt": "Professional fashion photograph, full body shot. Model: petite goddess at center of acoustic salt crystal formation — salt crystals growing and levitating in acoustic nodes around tiny figure, white cubic crystals in perfect geometric formation. Body: 151cm compact figure, golden-olive skin creating warmth contrast with white salt crystals, dark hair in sleek low bun away from crystal field. Wearing: white micro bikini — salt crystals suspended in acoustic nodes 1-20cm from skin forming geometric white armor, white patent platform stiletto ankle boots 4-inch heel with salt crystal clusters at acoustic boot nodes, silver crystal drop earrings matching levitating crystals. Environment: stark white studio, salt crystal formation extending full frame, petite figure as dark warm center of white crystal universe, cubic crystals catching directional light in geometric sparkle. Lighting: hard side lighting, salt crystals creating geometric specular patterns, golden skin warm against cold white crystal field. Style: petite acoustic salt crystal editorial, sound growing crystals. Shot on Hasselblad X2D, acoustic crystal grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_curvy_rose_petal_orbit",
            "name": "Rose Petal Orbit",
            "prompt": "Professional fashion photograph, full body shot. Model: voluptuous curvy goddess, thousands of red rose petals levitating in acoustic orbital paths around her full figure — petals tracing figure-8 orbital loops in 3D sound field. Body: spectacular full hourglass figure, warm caramel oiled skin, loose waves catching petal-wind, lips red matching petals. Wearing: deep red ultra-sheer silk slip dress soaked in acoustic petal-wind — fabric barely there, rose petals landing and sliding off curves, red stiletto thigh-high platform boots 5-inch heel, petals orbiting boot heels like tiny satellites. Environment: dark romantic studio, rose petals tracing luminous orbital paths in long-exposure light trails, remaining petals suspended at acoustic nodes. Lighting: warm amber key, rose petals backlit catching golden edges, skin warm in amber between petal orbits. Style: curvy acoustic rose petal orbit editorial, sound as romance. Shot on Hasselblad X2D, acoustic rose grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_athletic_steel_ball_precision",
            "name": "Steel Ball Precision",
            "prompt": "Professional fashion photograph, full body shot. Model: elite athletic goddess, hundreds of chrome steel balls levitating in perfect military-precision acoustic grid around her athletic figure — geometric perfection mirroring body discipline. Body: competition-level athletic physique, every muscle defined, bronze oiled skin, severe high bun, expression fierce-focused. Wearing: minimal black latex micro sports bra and micro shorts — athletic minimal, chrome steel balls 2cm diameter suspended in perfect cubic acoustic lattice surrounding figure from floor to crown, matte black thigh-high platform stiletto boots 5-inch heel, steel balls reflecting distorted black figure in each sphere. Environment: dark precision studio, steel ball grid creating perfect geometric architecture around figure, acoustic transducer array visible at corners. Lighting: hard directional light, steel balls creating perfect specular highlights, figure in dramatic chiaroscuro between ball grid. Style: athletic acoustic steel precision editorial, discipline made visible. Shot on Phase One XF IQ4, acoustic steel grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_amazon_mercury_drop_curtain",
            "name": "Mercury Drop Curtain",
            "prompt": "Professional fashion photograph, full body shot. Model: 183cm amazon goddess standing behind acoustic mercury drop curtain — liquid mercury suspended in vertical acoustic plane creates mirror curtain she emerges through, legs visible below. Body: tall powerful physique, long legs fully visible below mercury curtain, copper skin, natural afro halo above curtain edge. Wearing: mercury itself draping torso — liquid metal suspended in acoustic field conforming to curves as living mercury bodysuit, deep plunge, thigh-high silver chrome platform stiletto boots 6-inch heel below mercury plane, silver torque collar. Environment: dark studio, mercury drop curtain spanning full frame width, figure emerging through it, drops suspended in perfect acoustic node positions. Lighting: silver side lighting, mercury drops acting as infinite tiny mirrors, figure multiply reflected in mercury curtain. Style: amazon acoustic mercury curtain editorial, liquid metal as couture veil. Shot on Hasselblad X2D, acoustic mercury grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_plus_size_golden_dust_suspension",
            "name": "Golden Dust Suspension",
            "prompt": "Professional fashion photograph, full body shot. Model: magnificent plus-size goddess at center of acoustic gold dust suspension — millions of 24k gold particles levitating in acoustic field creating total gold atmosphere, figure the dark goddess at golden universe center. Body: full magnificent figure, deep ebony skin creating maximum contrast with gold particle cloud, voluminous natural locs adorned with gold dust caught in hair. Wearing: minimal black micro dress — pure black against gold particle cloud for maximum contrast, gold particles settling on skin as living gold paint, thigh-high black patent platform boots 5-inch heel catching gold reflections, single black choker. Environment: gold particle suspension filling entire studio atmosphere, figure at density center where particles thickest, cloud thinning toward edges. Lighting: single overhead gold-filtered beam, gold particles creating total warm luminous atmosphere, figure silhouetted against own gold cloud. Style: plus-size acoustic gold dust goddess editorial, sound making gold float. Shot on Phase One XF IQ4, acoustic gold grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_petite_ink_drop_suspension",
            "name": "Ink Drop Suspension",
            "prompt": "Professional fashion photograph, full body shot. Model: petite goddess at moment of acoustic ink drop suspension — dozens of ink drops caught mid-fall in acoustic nodes, black ink suspended as frozen explosion around tiny figure. Body: 151cm compact figure, ivory skin creating stark contrast with black ink drops, platinum hair in tight bun away from ink. Wearing: pure white micro bikini — white canvas for ink drop shadow play, black ink drops suspended 1-30cm from skin in acoustic nodes creating ink corona around white figure, white platform stiletto ankle boots 4-inch, no jewelry — just ink and white. Environment: white infinity studio, ink drops suspended in perfect acoustic positions creating complex black constellation around figure, ink trails showing acoustic node paths. Lighting: flat white studio, ink drops casting tiny shadows on white floor, figure as white goddess in black ink cosmos. Style: petite acoustic ink suspension editorial, sound freezing chaos. Shot on Hasselblad X2D, acoustic ink grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_curvy_champagne_bubble_levitation",
            "name": "Champagne Bubble Levitation",
            "prompt": "Professional fashion photograph, full body shot. Model: curvy goddess surrounded by acoustic champagne bubble levitation — thousands of champagne bubbles suspended in acoustic nodes rather than rising, creating permanent effervescent cloud around full figure. Body: voluptuous full hourglass figure, warm honey skin catching bubble light, waist-length blonde waves catching bubbles. Wearing: ultra-sheer champagne silk slip dress — fabric colour-matched to champagne bubbles making dress and bubbles merge visually, bubbles suspended at every curve highlighting silhouette, champagne gold stiletto thigh-high platform boots 5-inch heel with bubbles orbiting heels, gold pearl drop earrings. Environment: luxury penthouse setting, champagne flutes on surfaces, bubble cloud dense around figure, thinning to reveal penthouse view. Lighting: warm champagne gold ambient, bubbles catching light as thousands of tiny golden spheres, skin warm in bubble-diffused light. Style: curvy acoustic champagne bubble goddess editorial, celebration suspended in time. Shot on Phase One XF IQ4, acoustic champagne grade, portrait 2:3 vertical.",
            "tier": "SSS"
        },
        {
            "id": "acoustic_athletic_fire_ember_levitation",
            "name": "Fire Ember Levitation",
            "prompt": "Professional fashion photograph, full body shot. Model: athletic goddess at center of acoustic fire ember levitation — hundreds of glowing fire embers suspended in acoustic nodes around athletic figure, embers frozen mid-flight in 3D sound grid. Body: elite athletic physique, bronze oiled skin glowing in ember light, fierce expression, tight warrior braid. Wearing: minimal black micro sports bra and micro shorts — dark base to contrast ember glow, embers suspended around body at acoustic nodes ranging from ankle to crown creating living fire constellation, thigh-high matte black platform combat boots 4-inch with embers orbiting at boot tops, no jewelry — fire is the accessory. Environment: dark forge-like space, embers suspended in perfect acoustic architecture around figure, smoke wisps below ember nodes. Lighting: ember warm amber-orange from all acoustic node positions, figure lit entirely by own ember constellation, bronze skin catching every ember. Style: athletic acoustic ember levitation editorial, sound taming fire. Shot on Hasselblad X2D, acoustic ember grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_amazon_flower_petal_vortex",
            "name": "Flower Petal Vortex",
            "prompt": "Professional fashion photograph, full body shot. Model: towering amazon goddess at axis of acoustic petal vortex — thousands of white magnolia petals levitating in upward spiral acoustic field around her tall figure, petals forming tornado-goddess architecture. Body: 183cm powerful physique, deep brown skin, severe geometric updo with single magnolia, long legs visible through petal vortex gaps. Wearing: white micro bandeau and white micro thong — white petals and white fabric creating seamless skin-reveal throughout vortex, petal vortex forming natural strapless gown silhouette in air, white platform stiletto mules 6-inch heel at vortex base, single gold armband. Environment: dark studio, petal vortex rising full frame height around figure, long-exposure showing spiral petal trails as luminous white lines. Lighting: single overhead white beam, petals catching edge light in white arcs, skin visible through petal architecture. Style: amazon acoustic petal vortex editorial, sound building a gown from flowers. Shot on Phase One XF IQ4, acoustic petal grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
        {
            "id": "acoustic_plus_size_ice_shard_armor",
            "name": "Ice Shard Armor",
            "prompt": "Professional fashion photograph, full body shot. Model: supreme plus-size goddess armored in acoustic ice shard levitation — large ice crystal shards suspended in precise acoustic nodes forming fitted ice armor around full magnificent figure. Body: 5XL commanding figure, deep brown skin dramatically contrasting with translucent ice armor panels, natural locs with ice crystal accessories. Wearing: ultra-minimal skin-tone bodysuit beneath ice armor — ice shards 5-30cm suspended in acoustic nodes forming chest plate, shoulder guards, hip panels, shin shields as living ice armor, transparent ice heels 5-inch platform showing bare foot above, diamond choker the only non-ice element. Environment: arctic dark, ice armor glowing blue-white from within, acoustic transducer array creating the field, breath visible in cold air. Lighting: cold blue from ice shard interior luminescence, no external source — armor is the light, deep ebony skin edge-lit by own ice armor. Style: plus-size acoustic ice armor goddess editorial, sound as protection. Shot on Hasselblad X2D, acoustic ice grade, portrait 2:3 vertical.",
            "tier": "HOF"
        },
    ],\
'''

# ── 2. HOF 4종 ────────────────────────────────────────────────────────────

NEW_HOF = [
    "acoustic_amazon_mercury_drop_curtain",
    "acoustic_athletic_fire_ember_levitation",
    "acoustic_amazon_flower_petal_vortex",
    "acoustic_plus_size_ice_shard_armor",
]

# ── 3. plasma HOF 승격 ────────────────────────────────────────────────────

PLASMA_SSS_ID = "plasma_plus_size_solar_flare_crown"

# ══════════════════════════════════════════════════════════════════════════
# STEP 1: presets_meta.py — 카테고리 추가
# ══════════════════════════════════════════════════════════════════════════

def patch_presets_meta():
    print("\n[ STEP 1 ] presets_meta.py 패치 중...")
    content = META_PATH.read_text(encoding="utf-8")

    if "acoustic_amazon_glass_shard_levitation" in content:
        print("  ⚠️  이미 패치됨 — SKIP")
        return

    # Mycelium Glamour 카테고리 뒤에 삽입
    anchor = '    "🫧 Mycelium Glamour"'
    if anchor not in content:
        print("  ❌ 앵커 찾기 실패 — presets_meta.py 수동 확인 필요")
        return

    # Mycelium 블록 끝 찾기 (닫는 ],)
    idx = content.find(anchor)
    # 해당 블록의 ], 찾기
    block_end = content.find("],", idx)
    if block_end == -1:
        print("  ❌ Mycelium 블록 끝 찾기 실패")
        return

    insert_pos = block_end + 2  # ], 다음
    new_content = (
        content[:insert_pos]
        + "\n"
        + ACOUSTIC_PRESETS
        + content[insert_pos:]
    )

    META_PATH.write_text(new_content, encoding="utf-8")
    print("  ✅ Acoustic Levitation Glamour 12종 추가 완료")

    # 검증
    verify = META_PATH.read_text(encoding="utf-8")
    ids = [
        "acoustic_amazon_glass_shard_levitation",
        "acoustic_plus_size_water_sphere_cloud",
        "acoustic_petite_salt_crystal_formation",
        "acoustic_curvy_rose_petal_orbit",
        "acoustic_athletic_steel_ball_precision",
        "acoustic_amazon_mercury_drop_curtain",
        "acoustic_plus_size_golden_dust_suspension",
        "acoustic_petite_ink_drop_suspension",
        "acoustic_curvy_champagne_bubble_levitation",
        "acoustic_athletic_fire_ember_levitation",
        "acoustic_amazon_flower_petal_vortex",
        "acoustic_plus_size_ice_shard_armor",
    ]
    all_ok = True
    for pid in ids:
        ok = pid in verify
        print(f"  {'✅' if ok else '❌'} {pid}")
        if not ok:
            all_ok = False
    print(f"\n  {'✅ 전체 검증 통과' if all_ok else '❌ 일부 누락 — 수동 확인 필요'}")


# ══════════════════════════════════════════════════════════════════════════
# STEP 2: hof_tier.py — HOF 4종 추가
# ══════════════════════════════════════════════════════════════════════════

def patch_hof_new():
    print("\n[ STEP 2 ] hof_tier.py — Acoustic HOF 4종 추가 중...")
    content = HOF_PATH.read_text(encoding="utf-8")

    to_add = [pid for pid in NEW_HOF if pid not in content]
    if not to_add:
        print("  ⚠️  이미 모두 패치됨 — SKIP")
        return

    # HOF_TIER 리스트 닫는 ] 바로 앞에 삽입
    # 마지막 항목 뒤 찾기
    anchor = "HOF_TIER = ["
    if anchor not in content:
        print("  ❌ HOF_TIER 앵커 찾기 실패")
        return

    # 리스트 닫는 ] 찾기 (마지막)
    hof_start = content.find(anchor)
    close_bracket = content.rfind("]", hof_start)
    if close_bracket == -1:
        print("  ❌ HOF_TIER 닫는 ] 찾기 실패")
        return

    new_entries = "\n"
    for pid in to_add:
        new_entries += f'    "{pid}",\n'

    new_content = (
        content[:close_bracket]
        + new_entries
        + content[close_bracket:]
    )

    HOF_PATH.write_text(new_content, encoding="utf-8")
    print(f"  ✅ {len(to_add)}종 추가 완료")

    # 검증
    verify = HOF_PATH.read_text(encoding="utf-8")
    for pid in NEW_HOF:
        ok = pid in verify
        print(f"  {'✅' if ok else '❌'} {pid}")


# ══════════════════════════════════════════════════════════════════════════
# STEP 3: hof_tier.py — plasma HOF 승격
# ══════════════════════════════════════════════════════════════════════════

def patch_plasma_hof():
    print("\n[ STEP 3 ] plasma_plus_size_solar_flare_crown HOF 승격 중...")
    content = HOF_PATH.read_text(encoding="utf-8")

    if PLASMA_SSS_ID in content:
        print("  ⚠️  이미 HOF_TIER에 존재 — SKIP")
        return

    # HOF_TIER 닫는 ] 앞에 삽입
    anchor = "HOF_TIER = ["
    hof_start = content.find(anchor)
    close_bracket = content.rfind("]", hof_start)

    new_content = (
        content[:close_bracket]
        + f'\n    "{PLASMA_SSS_ID}",\n'
        + content[close_bracket:]
    )

    HOF_PATH.write_text(new_content, encoding="utf-8")

    verify = HOF_PATH.read_text(encoding="utf-8")
    ok = PLASMA_SSS_ID in verify
    print(f"  {'✅' if ok else '❌'} {PLASMA_SSS_ID}")


# ══════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("patch_acoustic_levitation.py 시작")
    print("=" * 60)

    if not META_PATH.exists():
        print(f"❌ 파일 없음: {META_PATH}")
        exit(1)
    if not HOF_PATH.exists():
        print(f"❌ 파일 없음: {HOF_PATH}")
        exit(1)

    patch_presets_meta()
    patch_hof_new()
    patch_plasma_hof()

    print("\n" + "=" * 60)
    print("모든 패치 완료!")
    print("=" * 60)
    print("\n다음 단계:")
    print("  Select-String 'acoustic_amazon_mercury_drop_curtain' core\\hof_tier.py")
    print("  Select-String 'acoustic_plus_size_ice_shard_armor' core\\hof_tier.py")
    print("  Select-String 'plasma_plus_size_solar_flare_crown' core\\hof_tier.py")
    print("  git add core/presets_meta.py core/hof_tier.py")
    print('  git commit -m "feat: Acoustic Levitation Glamour 12종 추가 HOF 4종 + plasma HOF 승격"')
    print("  git push")
