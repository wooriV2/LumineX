"""
add_new_presets_v27.py
🔥 핫 & 섹시 신규 프리셋 17개 추가

실행: python preset_builders/add_new_presets_v27.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")

presets = [
    # ── 💦 웻 & 바디 계열 ──────────────────────────────────
    ("wet_white_shirt", {
        "tag": "Wet White Shirt",
        "subject": "a soaking wet white shirt female model",
        "body": "VS Angel body, toned slim figure, curves revealed through soaked fabric",
        "outfit": "soaking wet white dress shirt completely drenched, translucent and clinging to every curve, buttons partially undone, minimal underneath",
        "material": "soaked white cotton shirt, wet transparency revealing silhouette, water-drenched clinging fabric",
        "environment": "rain-soaked alley, dramatic wet street, neon reflections in puddles",
        "lighting": "dramatic backlit wet light, neon reflection, wet fabric glow, rain atmosphere",
        "style": "wet shirt editorial, rain-soaked glamour photography, provocative fashion",
        "quality": "shot on Sony A7R V, dramatic rain grade, portrait 2:3 vertical"
    }),
    ("rain_bodysuit", {
        "tag": "Rain Bodysuit",
        "subject": "a rain-soaked bodysuit female model",
        "body": "athletic fitness model, sleek wet body, every curve defined by clinging wet suit",
        "outfit": "sheer bodysuit completely soaked in heavy rain, clinging skin-tight, water streaming down body, minimal coverage",
        "material": "soaked sheer bodysuit, wet skin-tight transparency, water-drenched second skin",
        "environment": "heavy rain rooftop, dramatic storm atmosphere, city lights blurred behind rain",
        "lighting": "dramatic stormy backlight, rain streak illumination, wet skin gleam",
        "style": "storm bodysuit editorial, rain-drenched glamour photography",
        "quality": "shot on Canon EOS R5, stormy dramatic grade, portrait 2:3 vertical"
    }),
    ("pool_edge_wet", {
        "tag": "Pool Edge Wet",
        "subject": "a dripping wet pool goddess emerging from water",
        "body": "VS Angel body, glistening wet skin, toned curves, water streaming down",
        "outfit": "soaking wet minimal bikini, water streaming off body, hands on pool edge, climbing out dramatically",
        "material": "wet bikini clinging to skin, water-drenched body, maximum wet skin gleam",
        "environment": "luxury infinity pool edge, city skyline at dusk, pool water reflection",
        "lighting": "golden dusk light on wet skin, pool reflection shimmer, wet body glow",
        "style": "luxury pool wet editorial, water goddess photography",
        "quality": "shot on Hasselblad H6D, golden wet grade, portrait 2:3 vertical"
    }),
    ("ocean_wave_body", {
        "tag": "Ocean Wave Body",
        "subject": "a wave-soaked beach goddess female model",
        "body": "athletic sun-kissed body, toned curves, wet sand on skin, ocean goddess",
        "outfit": "barely-there wet string bikini, ocean wave washing over body, wet fabric clinging, salt water drenched",
        "material": "soaked micro bikini, wet translucent fabric, ocean water on bare skin",
        "environment": "dramatic ocean shore, powerful waves crashing, golden sunset beach",
        "lighting": "golden sunset backlight, ocean spray shimmer, wet skin glow",
        "style": "ocean wave editorial, Sports Illustrated beach photography",
        "quality": "shot on Canon EOS R5, golden beach grade, portrait 2:3 vertical"
    }),

    # ── 🛋️ 인테리어 섹시 ──────────────────────────────────
    ("penthouse_bath", {
        "tag": "Penthouse Bath",
        "subject": "a luxury penthouse bath goddess female model",
        "body": "slim elegant model, bare shoulders and arms, submerged in bubbles, ultimate luxury",
        "outfit": "submerged in deep bubble bath, bare shoulders visible, draped in silk robe slipping off, city skyline through floor-to-ceiling window",
        "material": "white silk robe barely covering, bubble bath foam, bare skin above waterline",
        "environment": "ultra-luxury penthouse master bath, floor-to-ceiling windows, city skyline night view, rose petals floating",
        "lighting": "warm candlelight bath glow, city lights through window, intimate warm shadows",
        "style": "luxury boudoir editorial, penthouse lifestyle photography, intimate glamour",
        "quality": "shot on Hasselblad H6D, warm intimate grade, portrait 2:3 vertical"
    }),
    ("dressing_room_mirror", {
        "tag": "Dressing Room Mirror",
        "subject": "a luxury dressing room mirror goddess female model",
        "body": "VS Angel body, caught mid-change, intimate natural pose, full figure in mirror",
        "outfit": "luxury lingerie set partially on, silk robe fallen to floor, caught in mirror reflection, natural intimate moment",
        "material": "delicate lace lingerie, fallen silk robe, sheer stocking mid-pull",
        "environment": "luxury walk-in closet, floor-to-ceiling mirror, warm vanity lights, scattered designer clothing",
        "lighting": "warm vanity mirror lighting, soft shadow on curves, intimate dressing room glow",
        "style": "intimate boudoir editorial, luxury dressing room photography",
        "quality": "shot on Sony A7R V, warm vanity grade, portrait 2:3 vertical"
    }),
    ("silk_sheets_morning", {
        "tag": "Silk Sheets Morning",
        "subject": "a silk sheets morning goddess female model",
        "body": "slim elegant model, morning disheveled beauty, silk draped naturally over curves",
        "outfit": "barely covered by twisted silk sheets, natural morning pose, sheets sliding off one shoulder, intimate morning after",
        "material": "pure white silk sheets draped over curves, morning light on bare skin, minimal coverage",
        "environment": "luxury penthouse bedroom, morning golden light, white silk bedding, floor-to-ceiling windows",
        "lighting": "soft morning golden light, warm silk reflection, intimate bedroom glow",
        "style": "morning boudoir editorial, luxury bedroom lifestyle photography",
        "quality": "shot on Hasselblad H6D, soft morning grade, portrait 2:3 vertical"
    }),
    ("spa_private_steam", {
        "tag": "Spa Private Steam",
        "subject": "a luxury private spa steam goddess female model",
        "body": "slim toned model, dewy glowing skin, steamed skin texture, relaxed sensual pose",
        "outfit": "minimal white spa towel barely wrapped, steam rising from skin, wet dewy skin, luxury spa setting",
        "material": "white spa towel minimal wrap, steamed bare skin, water droplets on skin surface",
        "environment": "ultra-luxury private spa suite, marble walls, steam floating, warm ambient lighting",
        "lighting": "warm steam-filtered spa light, soft shadow through steam, dewy skin glow",
        "style": "luxury spa editorial, intimate wellness photography, steam glamour",
        "quality": "shot on Canon EOS R5, warm spa grade, portrait 2:3 vertical"
    }),

    # ── 🌙 나이트라이프 섹시 ──────────────────────────────
    ("bar_counter_glam", {
        "tag": "Bar Counter Glam",
        "subject": "a seductive bar counter glamour female model",
        "body": "hot glamour model, narrow waist, dramatic hourglass, leaning over bar counter provocatively",
        "outfit": "ultra-short sequined mini dress, deep plunge neckline, leaning over marble bar counter, cocktail glass in hand",
        "material": "metallic sequined micro dress, deep plunge sheer panel, stiletto heels",
        "environment": "upscale cocktail bar, marble counter, bottle-lined backlit shelf, moody amber lighting",
        "lighting": "warm amber bar light, backlit bottle glow, dramatic shadow play on curves",
        "style": "luxury bar editorial, nightlife glamour photography, cocktail fashion",
        "quality": "shot on Sony A7R V, warm amber nightlife grade, portrait 2:3 vertical"
    }),
    ("vip_booth_neon", {
        "tag": "VIP Booth Neon",
        "subject": "a neon VIP booth seductress female model",
        "body": "VS Angel body, long legs, dramatic curves, sprawled luxuriously in VIP booth",
        "outfit": "barely-there neon bodycon mini dress, deep cutouts, strappy stilettos, champagne bottle beside",
        "material": "ultra-tight neon bandage dress, deep cutout panels, metallic strappy heels",
        "environment": "ultra-exclusive VIP club booth, neon purple and pink lighting, velvet seating, crowd blurred below",
        "lighting": "dramatic neon purple-pink light, club strobe freeze, neon body highlight",
        "style": "VIP nightclub editorial, luxury party photography, neon glamour",
        "quality": "shot on Canon EOS R5, neon dramatic grade, portrait 2:3 vertical"
    }),
    ("after_party_suite", {
        "tag": "After Party Suite",
        "subject": "a glamorous after-party hotel suite female model",
        "body": "hot glamour model, disheveled party glamour, heels in hand, natural seductive ease",
        "outfit": "luxury evening gown slightly undone, one strap fallen, heels dangling from fingers, hair loosened from updo",
        "material": "silk evening gown slipping, fallen spaghetti strap, bare back revealed",
        "environment": "luxury hotel suite after party, scattered rose petals, champagne glasses, city skyline dawn",
        "lighting": "pre-dawn blue hour through window, warm lamp glow, dramatic shadow on bare back",
        "style": "after party boudoir editorial, luxury hotel suite photography",
        "quality": "shot on Hasselblad H6D, blue hour warm grade, portrait 2:3 vertical"
    }),

    # ── 💼 직업 섹시 ──────────────────────────────────────
    ("professor_after_class", {
        "tag": "Professor After Class",
        "subject": "a seductive professor after class female model",
        "body": "slim elegant model, intellectual glamour, glasses on, shirt unbuttoned",
        "outfit": "white dress shirt unbuttoned low, pencil skirt hiked up, glasses pushed up, sitting on desk edge",
        "material": "white cotton shirt open, tight pencil skirt, sheer stockings, heels",
        "environment": "empty lecture hall, chalkboard behind, late afternoon golden light through windows",
        "lighting": "warm late afternoon classroom light, golden window light on figure, intimate shadow",
        "style": "professor fantasy editorial, intellectual glamour photography",
        "quality": "shot on Sony A7R V, warm golden grade, portrait 2:3 vertical"
    }),
    ("bartender_closing", {
        "tag": "Bartender Closing",
        "subject": "a seductive closing-time bartender female model",
        "body": "hot glamour model, confident stance, leaning on bar, curves in uniform",
        "outfit": "bartender vest barely buttoned, tiny shorts, leaning on bar counter after last call, hair let down",
        "material": "tight bartender vest open, micro shorts, bare midriff, ankle boots",
        "environment": "empty bar after closing, dim amber lights, chairs on tables, lone spotlight",
        "lighting": "lone spotlight on figure, warm amber closing time light, dramatic bar shadows",
        "style": "closing time fantasy editorial, bar glamour photography",
        "quality": "shot on Canon EOS R5, warm amber grade, portrait 2:3 vertical"
    }),
    ("pilot_uniform_edit", {
        "tag": "Pilot Uniform Edit",
        "subject": "a seductive airline pilot uniform female model",
        "body": "slim elegant model, tall commanding presence, uniform worn provocatively",
        "outfit": "pilot uniform jacket open, shirt undone, captain hat tilted, uniform skirt short, in cockpit doorway",
        "material": "pilot uniform jacket open, white shirt undone, tight uniform mini skirt, stiletto heels",
        "environment": "private jet interior, cockpit doorway, tarmac sunset through window",
        "lighting": "warm sunset cockpit light, dramatic uniform shadow play, golden tarmac glow",
        "style": "airline fantasy editorial, luxury aviation glamour photography",
        "quality": "shot on Hasselblad H6D, warm aviation grade, portrait 2:3 vertical"
    }),

    # ── 🏋️ 스포츠 섹시 ──────────────────────────────────
    ("gym_mirror_pump", {
        "tag": "Gym Mirror Pump",
        "subject": "a post-workout gym mirror goddess female model",
        "body": "bikini competition model, extremely defined muscles, post-workout pump, glistening sweat",
        "outfit": "minimal sports bra and micro shorts, post-workout sweat glistening, gym mirror reflection, muscles pumped",
        "material": "tiny sports bra, micro biker shorts, sweat-drenched skin, bare midriff",
        "environment": "luxury gym mirror wall, professional equipment, warm gym lighting, empty after hours",
        "lighting": "warm gym spotlight, sweat-glistening highlight, mirror double reflection",
        "style": "fitness glamour editorial, gym mirror photography, post-workout glamour",
        "quality": "shot on Sony A7R V, warm fitness grade, portrait 2:3 vertical"
    }),
    ("yoga_stretch_sheer", {
        "tag": "Yoga Stretch Sheer",
        "subject": "a sheer yoga stretch goddess female model",
        "body": "ballerina physique, extreme flexibility, graceful stretch, toned curves",
        "outfit": "sheer see-through yoga pants, minimal crop top, deep backbend stretch pose, curves fully revealed through fabric",
        "material": "sheer transparent yoga leggings, minimal crop bra, translucent fabric revealing everything",
        "environment": "luxury yoga studio, floor-to-ceiling mirrors, morning golden light, wooden floor",
        "lighting": "soft morning golden studio light, backlight through sheer fabric, graceful shadow",
        "style": "yoga glamour editorial, flexible beauty photography, sheer sportswear",
        "quality": "shot on Canon EOS R5, soft golden grade, portrait 2:3 vertical"
    }),
    ("tennis_short_dress", {
        "tag": "Tennis Short Dress",
        "subject": "a seductive tennis short dress female model",
        "body": "VS Angel body, athletic toned legs, confident serve pose, tennis goddess",
        "outfit": "ultra-short white tennis dress, serve motion revealing underneath, racket in hand, hair flying",
        "material": "ultra-short white pleated tennis dress, minimal briefs underneath, bare toned legs",
        "environment": "luxury private tennis club, clay court, golden afternoon light, net in background",
        "lighting": "warm golden afternoon court light, dynamic serve shadow, athletic highlight",
        "style": "tennis glamour editorial, luxury sports photography, athletic fashion",
        "quality": "shot on Hasselblad H6D, warm clay court grade, portrait 2:3 vertical"
    }),
]

created = []
skipped = []

for filename, data in presets:
    path = PRESETS_DIR / f"{filename}.json"
    if path.exists():
        skipped.append(filename)
        continue
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    created.append(filename)

print("=" * 50)
print("LumineX v27 — 핫 & 섹시 신규 프리셋")
print("=" * 50)
print(f"\n✅ 생성 완료 ({len(created)}개):")
for c in created:
    print(f"  + {c}")
if skipped:
    print(f"\n⏭️  이미 존재 ({len(skipped)}개): {skipped}")
print(f"\n총 {len(created)}개 생성 완료!")
print("\n다음 단계: dashboard.py PRESET_CATEGORIES 및 SS_TIER 업데이트 필요")
