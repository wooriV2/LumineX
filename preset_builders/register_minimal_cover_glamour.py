"""
register_minimal_cover_glamour.py
신규 프리셋 7종 JSON 생성 + dashboard.py 등록
카테고리: 🎀 미니멀 커버 글래머
"""
import json
from pathlib import Path

PRESETS_DIR = Path("C:/Dev/LumineX/presets")
DASHBOARD   = Path("C:/Dev/LumineX/dashboard.py")

# ══════════════════════════════════════════════════════════
# 프리셋 JSON 데이터
# ══════════════════════════════════════════════════════════
PRESETS = {
    "body_chain_only_glam": {
        "tag": "Body Chain Only Glam",
        "subject": "a stunning female model adorned only in elaborate gold body chain jewelry, no clothing",
        "body": "luxury glamour model, defined waist, wide round hips, sophisticated voluptuous elegance",
        "outfit": "elaborate gold body chain jewelry draped across bare skin, layered chains covering chest and hips, no fabric clothing whatsoever, luxury body jewelry editorial, coin medallions and draped chains as the only covering",
        "material": "gold chain mail, coin pendants, layered metallic chains, no fabric",
        "environment": "dark baroque opulent chamber, velvet and gold interior, candlelit ambiance",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights, gold chains catching warm light",
        "style": "Versace campaign bold luxury glamour, Harper's Bazaar sensual fashion editorial",
        "quality": "shot on Hasselblad H6D, cinematic gold grade, portrait 2:3 vertical"
    },
    "flower_body_only": {
        "tag": "Flower Body Only",
        "subject": "a stunning female model wearing only fresh flowers and petals arranged on bare skin",
        "body": "soft glamour model, polished feminine curves, graceful elegant figure",
        "outfit": "fresh flowers and petals arranged directly on bare skin covering intimate areas only, botanical body art editorial, roses orchids and peonies draped across chest and hips, floral haute couture, no fabric only flowers and greenery",
        "material": "fresh roses, white orchids, pink peonies, trailing green vines, botanical",
        "environment": "luxury infinity pool edge, tropical resort, palm trees, golden hour Bali",
        "lighting": "golden hour warm backlight, skin luminosity, glowing botanical light",
        "style": "Vogue Italia high-fashion editorial, Sports Illustrated botanical glamour",
        "quality": "shot on Canon EOS R5, golden botanical grade, portrait 2:3 vertical"
    },
    "rope_art_editorial": {
        "tag": "Rope Art Editorial",
        "subject": "a stunning athletic female model wrapped in decorative white rope as sculptural fashion",
        "body": "slim toned model, lean athletic build, flat stomach, defined muscles",
        "outfit": "decorative white macrame rope artistically wrapped around entire body in geometric patterns, shibari-inspired fashion art, intricate knots forming structural garment, rope as haute couture sculpture, from neck to ankles",
        "material": "thick white cotton rope, macrame knots, geometric rope weaving",
        "environment": "pure white minimalist studio, seamless backdrop, concrete floor",
        "lighting": "professional octabox strobe, high-contrast glamour lighting, clean white light",
        "style": "Alexander McQueen dramatic fashion editorial, avant-garde conceptual runway",
        "quality": "shot on Phase One XF IQ4, crisp editorial grade, portrait 2:3 vertical"
    },
    "ribbon_wrap_glam": {
        "tag": "Ribbon Wrap Glam",
        "subject": "a stunning female model wrapped in wide satin ribbons as a living gift, gift-wrapped human concept",
        "body": "hot glamour model, dramatically cinched narrow waist, red carpet curves",
        "outfit": "wide satin ribbons in crimson red and gold wrapped strategically around body, large bows at chest and hips, ribbon as the only garment, gift-wrapped goddess concept, silk ribbon draping and trailing",
        "material": "wide silk satin ribbon, crimson red and gold, large decorative bows",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, marble floors",
        "lighting": "golden hour warm backlight, chandeliers reflecting off satin ribbon",
        "style": "Valentino red carpet luxury editorial, Vogue Paris haute couture",
        "quality": "shot on Canon EOS R5, warm golden grade, portrait 2:3 vertical"
    },
    "crystal_body_cover": {
        "tag": "Crystal Body Cover",
        "subject": "a stunning female model covered in Swarovski crystals and gemstones adhered directly to skin",
        "body": "luxury glamour model, slim elegant figure, sophisticated voluptuous elegance",
        "outfit": "thousands of Swarovski crystals sapphires and diamonds adhered directly to skin covering body, crystal body art as wearable sculpture, rhinestone body coverage editorial, gemstones arranged in baroque scrollwork patterns on bare skin, no fabric only crystals",
        "material": "Swarovski crystals, sapphires, rhinestones, diamonds, direct skin application",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor below",
        "lighting": "multi-colored neon edge glow, crystals refracting and scattering light, night glamour",
        "style": "Versace campaign bold luxury glamour, Monaco red carpet editorial",
        "quality": "shot on Hasselblad H6D, night luxury grade, portrait 2:3 vertical"
    },
    "maldives_bikini_editorial": {
        "tag": "Maldives Bikini Editorial",
        "subject": "a stunning female model in a luxury designer bikini on a Maldives overwater jetty",
        "body": "VS Angel body, toned flat abs, model-perfect proportions, legs over 90cm long",
        "outfit": "luxury designer string bikini with intricate blue and gold baroque floral print, tie-side bottoms, halter neck top, high-end swimwear editorial",
        "material": "premium swimwear fabric, baroque floral print, gold trim detail",
        "environment": "Maldives overwater villa jetty, crystal turquoise sea, water villas in background, golden hour",
        "lighting": "golden hour warm backlight, skin luminosity, tropical glow",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "quality": "shot on Canon EOS R5, golden tropical grade, portrait 2:3 vertical"
    },
    "seaweed_coral_body": {
        "tag": "Seaweed Coral Body",
        "subject": "a stunning female model underwater wearing only seaweed and coral as a natural garment",
        "body": "athletic fitness model, defined abs, lean graceful figure",
        "outfit": "fresh seaweed kelp and coral reef elements draped across body as natural ocean garment, sea kelp forming draped skirt, coral clusters covering chest, underwater goddess aesthetic, ocean botanical body coverage only",
        "material": "golden kelp seaweed, red and purple coral, sea fans, shells, ocean botanical",
        "environment": "underwater Maldives overwater villa pool, crystal blue water, rippling light from above, white sand below",
        "lighting": "underwater pool light reflection, rippling aqua caustic light patterns, turquoise glow",
        "style": "Vogue Italia high-fashion editorial, underwater goddess campaign",
        "quality": "shot on Canon EOS R5, underwater turquoise grade, portrait 2:3 vertical"
    },
}

# ══════════════════════════════════════════════════════════
# 1. JSON 파일 생성
# ══════════════════════════════════════════════════════════
print("=" * 50)
print("[1/3] JSON 파일 생성")
for name, data in PRESETS.items():
    path = PRESETS_DIR / f"{name}.json"
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"  ✅ {name}.json")

# ══════════════════════════════════════════════════════════
# 2. dashboard.py — PRESET_CATEGORIES에 신규 카테고리 추가
# ══════════════════════════════════════════════════════════
print("\n[2/3] dashboard.py 카테고리 등록")
content = DASHBOARD.read_text(encoding="utf-8")

NEW_CATEGORY = '''
    "🎀 미니멀 커버 글래머": [
        "body_chain_only_glam",
        "flower_body_only",
        "rope_art_editorial",
        "ribbon_wrap_glam",
        "crystal_body_cover",
        "maldives_bikini_editorial",
        "seaweed_coral_body",
    ],
'''

# PRESET_CATEGORIES 딕셔너리 끝 (마지막 } 바로 앞)에 삽입
ANCHOR = '\n}\n\n\n# HOF tier'
if ANCHOR in content and "미니멀 커버 글래머" not in content:
    content = content.replace(ANCHOR, NEW_CATEGORY + "\n}\n\n\n# HOF tier", 1)
    print("  ✅ PRESET_CATEGORIES에 카테고리 추가")
elif "미니멀 커버 글래머" in content:
    print("  ⏭️  카테고리 이미 존재 — 건너뜀")
else:
    # fallback
    ANCHOR2 = "\n}\n\n# HOF tier"
    if ANCHOR2 in content and "미니멀 커버 글래머" not in content:
        content = content.replace(ANCHOR2, NEW_CATEGORY + "\n}\n\n# HOF tier", 1)
        print("  ✅ PRESET_CATEGORIES에 카테고리 추가 (fallback)")
    else:
        print("  ❌ 삽입 위치를 찾지 못했습니다 — 수동 삽입 필요")

# ══════════════════════════════════════════════════════════
# 3. HOF_TIER / SSS_TIER / SS_TIER 등록
# ══════════════════════════════════════════════════════════
print("\n[3/3] tier 등록")

HOF_ADD = '''    "body_chain_only_glam",
    "flower_body_only",
    "crystal_body_cover",
    "seaweed_coral_body",
'''

SSS_ADD = '''    "body_chain_only_glam",
    "flower_body_only",
    "rope_art_editorial",
    "ribbon_wrap_glam",
    "crystal_body_cover",
    "seaweed_coral_body",
'''

SS_ADD = '''    "body_chain_only_glam",
    "flower_body_only",
    "rope_art_editorial",
    "ribbon_wrap_glam",
    "crystal_body_cover",
    "maldives_bikini_editorial",
    "seaweed_coral_body",
'''

def add_to_tier(content, tier_name, entries):
    """tier set의 첫 번째 항목 앞에 신규 항목 삽입"""
    marker = f"{tier_name} = {{"
    pos = content.find(marker)
    if pos == -1:
        return content, False
    # { 다음 줄에 삽입
    eol = content.find("\n", pos) + 1
    # 이미 있는지 확인
    if "body_chain_only_glam" in content[pos:pos+500]:
        return content, None  # already exists
    content = content[:eol] + entries + content[eol:]
    return content, True

content, ok = add_to_tier(content, "HOF_TIER", HOF_ADD)
if ok is True:   print("  ✅ HOF_TIER 4종 추가")
elif ok is None: print("  ⏭️  HOF_TIER 이미 존재")
else:            print("  ❌ HOF_TIER 위치를 찾지 못했습니다")

content, ok = add_to_tier(content, "SSS_TIER", SSS_ADD)
if ok is True:   print("  ✅ SSS_TIER 6종 추가")
elif ok is None: print("  ⏭️  SSS_TIER 이미 존재")
else:            print("  ❌ SSS_TIER 위치를 찾지 못했습니다")

content, ok = add_to_tier(content, "SS_TIER", SS_ADD)
if ok is True:   print("  ✅ SS_TIER 7종 추가")
elif ok is None: print("  ⏭️  SS_TIER 이미 존재")
else:            print("  ❌ SS_TIER 위치를 찾지 못했습니다")

DASHBOARD.write_text(content, encoding="utf-8")
print("\n✅ dashboard.py 저장 완료")
print("=" * 50)
print("🎉 완료! streamlit run dashboard.py 로 확인하세요.")
print("   카테고리: 🎀 미니멀 커버 글래머 (7종)")
print("   HOF 4종 / SSS 6종 / SS 7종")
