# -*- coding: utf-8 -*-
"""
DeepBlack Trio 완전 수정 패치 v3
- hof_tier.py: dict 항목 제거 → 키만 추가
- sss_tier.py: dict 항목 제거 → 키만 추가
- presets/deepblack_trio.json 생성 (프롬프트 저장)

실행: $env:PYTHONUTF8="1"; python preset_builders/patch_deepblack_trio_v3.py
"""

import re, json, ast, os

# ============================================================
# 공통 데이터
# ============================================================

HOF_KEYS = [
    "deepblack_trio_dragon_phoenix_tiger_void",
    "deepblack_trio_koi_dragon_phoenix_aurora",
    "deepblack_trio_uvneon_dragon_phoenix_tiger_void",
]

SSS_KEYS = [
    "deepblack_trio_dragon_celadon_phoenix_void",
    "deepblack_trio_koi_crane_phoenix_aurora",
    "deepblack_trio_dragon_goldleaf_phoenix_void",
    "deepblack_trio_tiger_uvneon_koi_void",
]

PROMPTS = {
    "deepblack_trio_dragon_phoenix_tiger_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, long floor-length silver box braids gold serpent cuffs — full body irezumi dragon and wisteria covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, 24k gold dragon violet wisteria cascading. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, voluminous silver afro gold diadem crown — full body irezumi phoenix and flame covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, crimson gold phoenix orange inferno. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, impossibly thick powerful thighs, wide commanding hips, full bust, silver micro locs sculptural updo obsidian pins — full body irezumi tiger and maple covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, blazing orange tiger crimson maple. LEFT: gold crystal rhinestone platform thigh-high boots 8 inch, extra long stiletto nails black gold dragon tips. CENTER: crimson extreme platform heels 8 inch, extra long coffin nails crimson gold flame ombre. RIGHT: black spike platform boots 8 inch, extra long stiletto nails orange black tiger stripe. All: extreme high-gloss oil. Pure black void backdrop. Triple chiaroscuro — dragon gold-violet left, phoenix crimson-gold center, tiger orange-black right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_koi_dragon_phoenix_aurora": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, massive round bubble butt commanding every inch, snatched waist, full high bust, floor-length silver goddess locs jade gold ornaments — full body irezumi koi and maple covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, blazing orange koi crimson maple. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, wild silver-tipped natural afro supreme — full body irezumi dragon and peony covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, 24k gold dragon scarlet peony. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, sleek silver-streaked long waves diamond pins — full body irezumi phoenix and wisteria covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, crimson gold phoenix violet wisteria. LEFT: jade extreme platform thigh-high boots 8 inch, extra long stiletto nails orange black koi tips. CENTER: black crystal platform heels 8 inch, extra long coffin nails black 24k gold tips. RIGHT: crimson extreme thigh-high boots 8 inch, extra long almond nails crimson violet phoenix ombre. All: extreme high-gloss oil. Iceland glacier aurora borealis green violet purple, massive ice formations perfect dark water reflection. Triple irezumi aurora — koi orange left, dragon gold center, phoenix crimson right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_uvneon_dragon_phoenix_tiger_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, wild voluminous silver-tipped afro — body fully covered in UV reactive neon bodypaint from neck to ankle, electric magenta and gold sacred geometry mandala patterns covering entire body, black light UV glow making neon patterns float above dark skin void, skin disappearing into darkness while magenta-gold geometry hovers in space. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, sleek silver-streaked updo diamond pins — body fully covered in UV reactive neon bodypaint from neck to ankle, electric cyan and green serpent dragon spiral patterns covering entire body, black light UV making cyan-green dragon float above void skin, intricate scales and coils glowing electric against disappearing black skin. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, massive round bubble butt commanding every inch, snatched waist, full high bust, floor-length silver goddess locs — body fully covered in UV reactive neon bodypaint from neck to ankle, electric crimson and orange phoenix flame patterns covering entire body, black light UV making crimson-orange phoenix float above void skin. LEFT: UV glowing magenta platform thigh-high boots 8 inch, extra long stiletto nails UV reactive neon hot pink same family as magenta body. CENTER: UV glowing cyan extreme platform heels 8 inch, extra long coffin nails UV reactive ice mint same family as cyan body. RIGHT: UV glowing crimson extreme platform boots 8 inch, extra long almond nails UV reactive neon orange same family as crimson body. All: extreme high-gloss oil, UV blacklight. Pure black void backdrop UV blacklight. Triple UV — magenta mandala left, cyan dragon center, crimson phoenix right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_dragon_celadon_phoenix_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, long floor-length silver box braids gold serpent cuffs — full body irezumi dragon and wisteria covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, 24k gold dragon violet wisteria cascading. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, voluminous silver afro gold diadem crown — body fully covered in semi-transparent Korean Goryeo celadon crane bodypaint from neck to ankle, translucent jade-green celadon glaze with white cranes soaring THROUGH which dark skin glows underneath, skin visible beneath paint creating living jade effect. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, massive round bubble butt commanding every inch, snatched waist, full high bust, silver micro locs sculptural updo obsidian pins — full body irezumi phoenix and flame covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, crimson gold phoenix orange inferno. LEFT: gold crystal rhinestone platform thigh-high boots 8 inch, extra long stiletto nails black gold dragon tips. CENTER: jade transparent extreme platform heels 8 inch, extra long coffin nails jade green black tips. RIGHT: crimson extreme platform boots 8 inch, extra long almond nails crimson gold phoenix ombre. All: extreme high-gloss oil. Pure black void backdrop. Triple chiaroscuro — dragon gold-violet left, celadon jade gleaming center, phoenix crimson-gold right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_koi_crane_phoenix_aurora": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, impossibly thick powerful thighs, wide commanding hips, full bust, floor-length silver goddess locs jade gold ornaments — full body irezumi koi and maple covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, blazing orange koi crimson maple. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, wild silver-tipped natural afro supreme — body fully covered in semi-transparent Japanese ink wash crane and wave bodypaint from neck to ankle, translucent monochrome grey-white cranes soaring THROUGH which dark skin glows underneath, skin visible beneath creating living shadow effect. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, sleek silver-streaked long waves diamond pins — full body irezumi phoenix and wisteria covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, crimson gold phoenix violet wisteria. LEFT: jade extreme platform thigh-high boots 8 inch, extra long stiletto nails orange black koi tips. CENTER: silver transparent extreme platform heels 8 inch, extra long coffin nails white silver crane tips. RIGHT: crimson extreme thigh-high boots 8 inch, extra long almond nails crimson violet phoenix ombre. All: extreme high-gloss oil. Iceland glacier aurora borealis green violet purple, massive ice formations perfect dark water reflection. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_dragon_goldleaf_phoenix_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, BBW bombshell physique — massive full-figure curves, extremely wide heavy hips, enormous full bust, long floor-length silver box braids gold serpent cuffs — full body irezumi dragon and wisteria covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, 24k gold dragon violet wisteria cascading. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, voluminous silver afro gold diadem crown — body fully covered in semi-transparent gold leaf bodypaint from neck to ankle, ultra-thin translucent 24k gold leaf sheets layered across entire body, dark skin glowing through gold gaps and tears creating living gold skin effect, scattered gold leaf fragments revealing black void beneath. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, massive round bubble butt commanding every inch, snatched waist, full high bust, silver micro locs sculptural updo obsidian pins — full body irezumi phoenix and flame covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, crimson gold phoenix orange inferno. LEFT: gold crystal rhinestone platform thigh-high boots 8 inch, extra long stiletto nails black gold tips. CENTER: gold extreme platform heels 8 inch, extra long coffin nails 24k gold tips. RIGHT: crimson extreme platform boots 8 inch, extra long almond nails crimson gold ombre. All: extreme high-gloss oil. Pure black void backdrop. Triple chiaroscuro — dragon gold-violet left, gold leaf gleaming center, phoenix crimson-gold right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
    "deepblack_trio_tiger_uvneon_koi_void": {
        "prompt": "Professional fashion photograph, full body shot. THREE women standing side by side. LEFT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, 50s silver fox glamour physique — ageless bombshell curves, impossibly thick powerful thighs, wide commanding hips, full bust, floor-length silver goddess locs jade ornaments — full body irezumi tiger and maple covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, blazing orange tiger crimson maple. CENTER: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 20s, hourglass queen physique — impossibly tiny waist, explosively wide round hips, full high bust, wild voluminous silver-tipped afro — body fully covered in UV reactive neon bodypaint glowing electric from neck to ankle, translucent electric neon geometric patterns and sacred geometry lines in cyan magenta yellow green, black light UV glow making patterns float above dark skin void, skin itself disappearing into darkness while neon lines hover in space. RIGHT: THE ABSOLUTE DARKEST BLACK SKIN ON EARTH blue-black void complexion, early 30s MILF glamour physique — mature voluptuous curves, extremely wide heavy hips, enormous full bust, sleek silver-streaked waves diamond pins — full body irezumi koi and peony covering EVERY inch neck to ankle WITHOUT EXCEPTION both legs fully tattooed to ankles NO bare skin visible below neck, blazing orange koi scarlet peony. LEFT: black extreme platform thigh-high boots 8 inch, extra long stiletto nails deep orange black tips. CENTER: transparent UV platform heels 8 inch glowing cyan, extra long coffin nails UV reactive ice mint same family as neon body. RIGHT: black extreme platform boots 8 inch, extra long almond nails orange scarlet tips. All: extreme high-gloss oil, UV blacklight. Pure black void backdrop UV blacklight. Triple — tiger orange-black left, UV neon geometric floating center, koi orange-scarlet right. 8K portrait 3:4 vertical.",
        "aspect_ratio": "3:4",
        "num_images": 2,
    },
}

# ============================================================
# 1. hof_tier.py — dict 항목 제거 후 키만 추가
# ============================================================

HOF_PATH = "core/hof_tier.py"

with open(HOF_PATH, encoding="utf-8-sig") as f:
    hof = f.read()

# dict 블록 제거: "deepblack_trio_xxx": { ... }, 패턴
hof = re.sub(
    r'\s*# DeepBlack Trio HOF\s*"deepblack_trio_[^"]+": \{[^}]+\},?\s*' * 10,
    '',
    hof,
    flags=re.DOTALL
)

# 더 안전한 방법: DeepBlack Trio 주석부터 마지막 } 전까지 제거
hof = re.sub(
    r'\s*# DeepBlack Trio HOF.*?(?=\n\})',
    '',
    hof,
    flags=re.DOTALL
)

# 키만 추가 (마지막 } 앞에)
hof_addition = '\n    # 🖤 DeepBlack Trio HOF\n'
for k in HOF_KEYS:
    hof_addition += f'    "{k}",\n'

hof = re.sub(r'\n\}(\s*)$', '\n' + hof_addition + '}\n', hof.rstrip())

with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof)

print("✅ hof_tier.py 수정 완료")

# ============================================================
# 2. sss_tier.py — dict 항목 제거 후 키만 추가
# ============================================================

SSS_PATH = "core/sss_tier.py"

with open(SSS_PATH, encoding="utf-8-sig") as f:
    sss = f.read()

# DeepBlack Trio SSS dict 블록 제거
sss = re.sub(
    r'\s*# DeepBlack Trio SSS.*?(?=\n\})',
    '',
    sss,
    flags=re.DOTALL
)

# SSS_TIER set 끝 } 앞에 키만 추가
# SS_TIER 시작 전 SSS_TIER 닫는 } 찾기
sss_addition = '\n    # 🖤 DeepBlack Trio SSS\n'
for k in SSS_KEYS:
    sss_addition += f'    "{k}",\n'

# SSS_TIER = { ... } 블록의 닫는 } 앞에 삽입
sss = re.sub(
    r'(\n\}\s*\nSS_TIER)',
    '\n' + sss_addition + '}\nSS_TIER',
    sss
)

with open(SSS_PATH, "w", encoding="utf-8") as f:
    f.write(sss)

print("✅ sss_tier.py 수정 완료")

# ============================================================
# 3. presets/deepblack_trio.json 생성
# ============================================================

JSON_PATH = "presets/deepblack_trio.json"

with open(JSON_PATH, "w", encoding="utf-8") as f:
    json.dump(PROMPTS, f, ensure_ascii=False, indent=2)

print(f"✅ {JSON_PATH} 생성 완료 ({len(PROMPTS)}종)")

# ============================================================
# 4. presets_meta.py 카테고리 — 중복 체크 후 추가
# ============================================================

META_PATH = "core/presets_meta.py"

with open(META_PATH, encoding="utf-8-sig") as f:
    meta = f.read()

if "DeepBlack Trio" in meta:
    print("⚠️ presets_meta.py DeepBlack Trio 이미 존재 — 스킵")
else:
    all_keys = HOF_KEYS + SSS_KEYS
    new_cat = '    "\U0001f5a4 DeepBlack Trio": [\n'
    for k in all_keys:
        new_cat += f'        "{k}",\n'
    new_cat += '    ],\n'

    meta = re.sub(r'\n\}(\s*)$', '\n' + new_cat + '}\n', meta.rstrip())

    with open(META_PATH, "w", encoding="utf-8") as f:
        f.write(meta)
    print("✅ presets_meta.py DeepBlack Trio 카테고리 추가 완료")

# ============================================================
# 5. AST 검증
# ============================================================

print("\n🔍 AST 검증 중...")
errors = []
for path in [HOF_PATH, SSS_PATH, META_PATH]:
    try:
        with open(path, encoding="utf-8") as f:
            ast.parse(f.read())
        print(f"  ✅ {path} OK")
    except SyntaxError as e:
        print(f"  ❌ {path} SyntaxError: {e}")
        errors.append(path)

if not errors:
    print("\n🎉 모든 파일 검증 통과!")
    print("다음 명령어로 커밋하세요:")
    print('git add -A && git commit -m "fix: DeepBlack Trio 키만 등록 + JSON 분리" && git push')
else:
    print(f"\n❌ {len(errors)}개 파일 오류 — 커밋 전 수정 필요")
