# -*- coding: utf-8 -*-
"""
LumineX 3개 카테고리 패치
- 🌙 나이트 글래머 4종 (전종 HOF)
- 👗 슬립드레스 글래머 3종 (전종 HOF)
- 🐆 애니멀프린트 글래머 4종 (전종 HOF)

실행: python preset_builders\patch_night_slip_animal.py
위치: C:\Dev\LumineX\ 에서 실행
"""

import json
from pathlib import Path

PRESETS_DIR = Path("presets")
META        = Path("core/presets_meta.py")

assert PRESETS_DIR.exists(), "presets/ 없음"
assert META.exists(), "core/presets_meta.py 없음"

PRESETS = {

    # ── 🌙 나이트 글래머 4종 ──────────────────────────────
    "club_vip_neon_goddess": {
        "tag": "Club VIP Neon Goddess",
        "subject": "a stunning Korean female model in ultra-luxury nightclub VIP section",
        "body": "fierce confident Korean model, neon-lit skin, VIP energy",
        "outfit": "wearing micro-length silver sequin bandage dress, all-over mirror sequins, completely backless, deep plunge, strappy silver heels",
        "material": "silver micro sequin stretch fabric, mirror-finish, backless",
        "environment": "ultra-luxury nightclub VIP booth, neon pink and blue lighting, champagne tower, velvet ropes, crystal bottle service, smoke machine atmosphere",
        "lighting": "neon club lighting pink and blue mixed, bottle sparklers glow, electric atmosphere",
        "style": "ultra-luxury VIP club editorial",
        "quality": "shot on Sony A7R V, neon club grade, portrait 2:3 vertical"
    },
    "club_rooftop_citylight": {
        "tag": "Club Rooftop Citylight",
        "subject": "a stunning Korean female model at luxury rooftop bar overlooking city skyline at night",
        "body": "sophisticated Korean model, windswept hair, city lights reflected in eyes",
        "outfit": "wearing backless black crepe mini dress, plunging front neckline, completely backless, diamond drop earrings, black strappy heels",
        "material": "black silk crepe, completely backless, mini length",
        "environment": "luxury rooftop bar overlooking Seoul skyline at night, infinity pool edge, Namsan Tower visible, city lights carpet below, warm string lights overhead",
        "lighting": "city skyline ambient glow, warm string light backlight, cool blue night sky contrast",
        "style": "Helmut Newton rooftop night editorial",
        "quality": "shot on Leica SL2, Seoul city night grade, portrait 2:3 vertical"
    },
    "micro_sequin_club": {
        "tag": "Micro Sequin Club",
        "subject": "a stunning Korean female model dancing in high-energy nightclub",
        "body": "dynamic dancing Korean model, hair in motion, fierce club energy",
        "outfit": "wearing micro gold sequin mini dress, plunging neckline, completely backless, every sequin catching light, gold heels",
        "material": "gold micro sequin stretch, fluid moving sequins, micro length",
        "environment": "high-energy nightclub dance floor, laser beams, disco ball scatter reflections, fog machine, crowd silhouettes, towering speakers",
        "lighting": "disco ball scatter light, gold laser beams, sequin reflections creating light explosion, dark club",
        "style": "Studio 54 disco revival editorial",
        "quality": "shot on Canon EOS R5, disco gold grade, portrait 2:3 vertical"
    },
    "rooftop_micro_night": {
        "tag": "Rooftop Micro Night",
        "subject": "a stunning Korean female model on luxury penthouse rooftop at night",
        "body": "sleek minimal Korean model, sharp features, urban night energy",
        "outfit": "wearing black micro-length bodycon dress, barely covering, thin shoulder straps, completely backless, black pointed-toe heels",
        "material": "matte black scuba fabric, body-hugging, micro length",
        "environment": "penthouse rooftop terrace in Hong Kong, city light grid below, infinity pool edge, modern glass architecture, dark sky, neon signs below",
        "lighting": "city light ambient glow from below, cool blue hour sky, neon sign color cast",
        "style": "Tom Ford minimal night editorial",
        "quality": "shot on Sony A7R V, Hong Kong night grade, portrait 2:3 vertical"
    },

    # ── 👗 슬립드레스 글래머 3종 ──────────────────────────
    "silk_slip_dawn_hotel": {
        "tag": "Silk Slip Dawn Hotel",
        "subject": "a stunning Korean female model in luxury Paris hotel suite at dawn",
        "body": "languid sensual Korean model, disheveled morning beauty, golden skin glow",
        "outfit": "wearing ivory silk charmeuse slip dress, thin spaghetti straps, bias-cut floor-length, completely backless, naturally draping",
        "material": "ivory silk charmeuse slip, ultra-lightweight, backless",
        "environment": "luxury Paris hotel suite at dawn, unmade ivory silk sheets, floor-to-ceiling windows, Eiffel Tower silhouette in golden dawn light, champagne flute on nightstand",
        "lighting": "dawn golden hour through sheer curtains, soft warm diffused light, Rembrandt-style gentle side lighting",
        "style": "Sofia Coppola luxury morning editorial",
        "quality": "shot on Leica M11, Paris dawn hotel grade, portrait 2:3 vertical"
    },
    "satin_slip_vanity_noir": {
        "tag": "Satin Slip Vanity Noir",
        "subject": "a stunning Korean female model at vintage vanity mirror in noir boudoir",
        "body": "classic femme fatale Korean model, red lips, dark sultry expression",
        "outfit": "wearing black silk satin slip dress, thin straps, mid-thigh length, side split, completely backless, black mules",
        "material": "black silk satin slip, ultra-smooth, backless",
        "environment": "noir Hollywood boudoir, vintage vanity mirror with warm bulb lights, scattered crystal perfume bottles, black and white film stills, velvet chaise longue",
        "lighting": "vanity bulb warm glow, classic noir shadow play, Hollywood glamour side lighting",
        "style": "Herb Ritts noir boudoir editorial",
        "quality": "shot on Hasselblad H6D, noir boudoir grade, portrait 2:3 vertical"
    },
    "satin_slip_micro": {
        "tag": "Satin Slip Micro",
        "subject": "a stunning Korean female model in micro satin slip dress in minimal studio",
        "body": "ultra-slim Korean editorial model, impossibly long legs, minimal makeup",
        "outfit": "wearing champagne silk satin micro slip dress, barely hip-length, thin straps, completely backless, delicate lace trim hem",
        "material": "champagne silk satin, micro-length, lace trim, backless",
        "environment": "minimal white photo studio, single warm floor lamp, polished wooden floor, architectural clean shadow lines",
        "lighting": "single side lamp warm light, minimal clean studio, precise shadow",
        "style": "Carine Roitfeld minimal editorial",
        "quality": "shot on Canon EOS R5, minimal studio grade, portrait 2:3 vertical"
    },

    # ── 🐆 애니멀프린트 글래머 4종 ────────────────────────
    "leopard_power_editorial": {
        "tag": "Leopard Power Editorial",
        "subject": "a stunning female model in head-to-toe leopard print power suit in art gallery",
        "body": "fierce powerful model, predator energy, commanding gaze",
        "outfit": "wearing head-to-toe leopard print power suit, fitted structured blazer and wide-leg tailored trousers, leopard print ankle boots, chunky gold jewelry",
        "material": "leopard print jacquard suiting, tailored",
        "environment": "luxury contemporary art gallery, white walls, dramatic architectural spotlighting, polished marble floor, large abstract art pieces",
        "lighting": "dramatic gallery spotlighting, high contrast, sharp defined shadows",
        "style": "Saint Laurent animal print power editorial",
        "quality": "shot on Hasselblad H6D, gallery editorial grade, portrait 2:3 vertical"
    },
    "leopard_micro_studio": {
        "tag": "Leopard Micro Studio",
        "subject": "a stunning female model in micro leopard print dress in professional studio",
        "body": "sleek long-limbed editorial model, fierce energy, sharp gaze",
        "outfit": "wearing micro leopard print bodycon dress, barely hip-length, skin-tight stretch fabric, completely backless, leopard print stiletto heels",
        "material": "leopard print stretch jersey, skin-tight, micro-length, backless",
        "environment": "minimalist photo studio, white seamless paper background, professional studio setup, reflective floor",
        "lighting": "professional studio lighting, clean defined shadows, high fashion editorial precision",
        "style": "Helmut Newton studio editorial",
        "quality": "shot on Phase One XF, studio editorial grade, portrait 2:3 vertical"
    },
    "snake_micro_marble": {
        "tag": "Snake Micro Marble",
        "subject": "a stunning female model in snakeskin micro dress in luxury marble interior",
        "body": "sleek dangerous model, reptilian cold energy, intense unblinking gaze",
        "outfit": "wearing python snakeskin print micro dress, skin-tight, barely covering, completely backless, pointed snake-print stiletto heels",
        "material": "python snakeskin print leather, micro-length, backless",
        "environment": "luxury Carrara white marble interior, floor-to-ceiling marble walls, architectural marble columns, cold minimal luxury space",
        "lighting": "architectural ceiling spot lighting, cold marble reflections, clean luxury light",
        "style": "Bottega Veneta marble editorial",
        "quality": "shot on Leica SL2, marble luxury grade, portrait 2:3 vertical"
    },
    "snakeskin_latex_glam": {
        "tag": "Snakeskin Latex Glam",
        "subject": "a stunning female model in snakeskin latex catsuit in dark jungle studio",
        "body": "powerful dangerous model, latex-shined skin, predator beauty",
        "outfit": "wearing snakeskin-print latex full bodysuit, green-gold python scale pattern covering entire body, matching latex gloves, python-print platform heels",
        "material": "snakeskin print latex, full bodysuit",
        "environment": "dark editorial studio with jungle aesthetic, atmospheric fog, reptile terrarium setting, jungle shadow background",
        "lighting": "dramatic hard side lighting, latex surface highlights, moody dark atmosphere",
        "style": "Alexander McQueen reptile editorial",
        "quality": "shot on Canon EOS R5, dark editorial grade, portrait 2:3 vertical"
    },
}

# ─────────────────────────────────────────────────────────
# 1. JSON 파일 생성
# ─────────────────────────────────────────────────────────
created = []
skipped = []
for name, data in PRESETS.items():
    p = PRESETS_DIR / f"{name}.json"
    if p.exists():
        skipped.append(name)
    else:
        p.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        created.append(name)

print(f"✅ JSON 생성: {len(created)}개")
if skipped:
    print(f"⚠️  이미 존재 (스킵): {skipped}")

# ─────────────────────────────────────────────────────────
# 2. presets_meta.py 패치
# ─────────────────────────────────────────────────────────
text = META.read_text(encoding="utf-8")

NIGHT    = ["club_vip_neon_goddess", "club_rooftop_citylight", "micro_sequin_club", "rooftop_micro_night"]
SLIP     = ["silk_slip_dawn_hotel", "satin_slip_vanity_noir", "satin_slip_micro"]
ANIMAL   = ["leopard_power_editorial", "leopard_micro_studio", "snake_micro_marble", "snakeskin_latex_glam"]
ALL_NEW  = NIGHT + SLIP + ANIMAL
HOF_ALL  = ALL_NEW  # snakeskin_latex_glam도 HOF 확정

CATS = {
    "🌙 나이트 글래머": NIGHT,
    "👗 슬립드레스 글래머": SLIP,
    "🐆 애니멀프린트 글래머": ANIMAL,
}

CAT_MARKER = '"🎭 극장적 글래머":'

for cat_name, preset_list in CATS.items():
    if cat_name in text:
        print(f"⚠️  {cat_name} 이미 존재 — 스킵")
        continue
    insert = f'    "{cat_name}": {repr(preset_list)},\n    {CAT_MARKER}'
    assert CAT_MARKER in text, f"카테고리 마커 없음"
    text = text.replace(CAT_MARKER, insert, 1)
    print(f"✅ {cat_name} 카테고리 추가")

# HOF 추가
HOF_MARKER = "# 2026-07-07 극장적 글래머 30종 HOF"
HOF_NEW = "# 2026-07-07 나이트/슬립드레스/애니멀프린트 11종 HOF\n"
HOF_NEW += "\n".join([f'    "{n}",' for n in HOF_ALL]) + "\n    "

if "나이트/슬립드레스/애니멀프린트 11종 HOF" in text:
    print("⚠️  HOF 이미 존재 — 스킵")
else:
    text = text.replace(HOF_MARKER, HOF_NEW + HOF_MARKER, 1)
    print("✅ HOF_TIER 11종 추가")

# SSS 추가
SSS_MARKER = "# 2026-07-07 극장적 글래머 30종 SSS"
SSS_NEW = "# 2026-07-07 나이트/슬립드레스/애니멀프린트 11종 SSS\n"
SSS_NEW += "\n".join([f'    "{n}",' for n in HOF_ALL]) + "\n    "

if "나이트/슬립드레스/애니멀프린트 11종 SSS" in text:
    print("⚠️  SSS 이미 존재 — 스킵")
else:
    text = text.replace(SSS_MARKER, SSS_NEW + SSS_MARKER, 1)
    print("✅ SSS_TIER 11종 추가")

# SS 추가
SS_MARKER = "# 2026-07-07 극장적 글래머 30종 SS"
SS_NEW = "# 2026-07-07 나이트/슬립드레스/애니멀프린트 11종 SS\n"
SS_NEW += "\n".join([f'    "{n}",' for n in HOF_ALL]) + "\n    "

if "나이트/슬립드레스/애니멀프린트 11종 SS" in text:
    print("⚠️  SS 이미 존재 — 스킵")
else:
    text = text.replace(SS_MARKER, SS_NEW + SS_MARKER, 1)
    print("✅ SS_TIER 11종 추가")

META.write_text(text, encoding="utf-8")
print("✅ core/presets_meta.py 저장 완료")

# ─────────────────────────────────────────────────────────
# 3. 검증
# ─────────────────────────────────────────────────────────
verify = META.read_text(encoding="utf-8")
ok = True
for n in ALL_NEW:
    if n not in verify:
        print(f"❌ {n} 누락")
        ok = False
    if not (PRESETS_DIR / f"{n}.json").exists():
        print(f"❌ {n}.json 없음")
        ok = False

if ok:
    total = sum(1 for _ in PRESETS_DIR.glob("*.json"))
    print(f"\n🎉 패치 완료!")
    print(f"   총 JSON: {total}개")
    print(f"   신규: {len(created)}종 (전종 HOF)")
    print(f"\n다음: git add . && git commit -m '...' && git push")
