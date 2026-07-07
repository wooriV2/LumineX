# -*- coding: utf-8 -*-
"""
공식E 오브제 커버 HOF 7종 JSON 생성
실행: python preset_builders/patch_formula_e_json.py (프로젝트 루트에서)
"""
import json
from pathlib import Path

PRESETS_DIR = Path("presets")

PRESETS = {
    "feather_body_cover": {
        "name": "Feather Body Cover",
        "category": "🌿 Minimal Object Cover",
        "background": "Ethereal white mist studio, soft feathers floating in air",
        "outfit": "Cascading white and gold feathers draped across body, NO clothing",
        "material": "Luxury ostrich and peacock feathers — soft, voluminous, iridescent",
        "lighting": "Soft diffused light, feathers glowing with rim light",
        "pose": "Standing, arms slightly raised, feathers cascading naturally",
        "style": "High fashion editorial, avant-garde couture, feather goddess",
        "negative": "no dress, no top, no clothing, no fabric underneath",
    },
    "mushroom_moss_cover": {
        "name": "Mushroom Moss Cover",
        "category": "🌿 Minimal Object Cover",
        "background": "Ancient forest floor, bioluminescent mushrooms, deep green moss",
        "outfit": "Giant luminous mushrooms and thick moss arranged across body, NO clothing",
        "material": "Glowing fungi caps, velvet moss, forest earth — organic textures",
        "lighting": "Bioluminescent blue-green glow from mushrooms, deep forest ambient",
        "pose": "Seated among mushrooms, body emerging from forest floor",
        "style": "Dark fantasy editorial, forest goddess, nature surrealism",
        "negative": "no dress, no clothing, no fabric, no costume",
    },
    "butterfly_swarm_cover": {
        "name": "Butterfly Swarm Cover",
        "category": "🌿 Minimal Object Cover",
        "background": "Sun-drenched meadow, golden bokeh, flowers in bloom",
        "outfit": "Swarm of colorful butterflies landing and covering body, NO clothing",
        "material": "Monarch, morpho, swallowtail butterflies — vivid wings, living mosaic",
        "lighting": "Golden afternoon sun, wings translucent with backlight",
        "pose": "Arms outstretched, face upward, butterflies in motion",
        "style": "Magical realism editorial, butterfly goddess, nature fantasy",
        "negative": "no dress, no clothing, no butterfly costume, no fabric",
    },
    "seashell_body_cover": {
        "name": "Seashell Body Cover",
        "category": "🌿 Minimal Object Cover",
        "background": "Pristine white sand beach, crystal turquoise water, sea foam",
        "outfit": "Arrangement of large iridescent seashells covering body, NO clothing",
        "material": "Giant clam shells, nautilus, conch — pearl iridescence, ocean-worn",
        "lighting": "Bright tropical sun, shells reflecting rainbow light",
        "pose": "Reclining on sand, shells arranged artfully across body",
        "style": "Mythological editorial, sea goddess, Venus rising concept",
        "negative": "no swimwear, no bikini, no clothing, no fabric",
    },
    "silver_chain_mirror_room": {
        "name": "Silver Chain Mirror Room",
        "category": "🌿 Minimal Object Cover",
        "background": "Infinite mirror room, silver reflections multiplying endlessly",
        "outfit": "Intricate silver chain draping across body, NO clothing",
        "material": "Fine sterling silver chains — layered, geometric, body jewelry aesthetic",
        "lighting": "Hard studio light, chains casting geometric shadows, mirror reflections",
        "pose": "Standing center of mirror room, chains catching every reflection",
        "style": "Avant-garde editorial, silver goddess, mirror world concept",
        "negative": "no dress, no clothing, no chain mail outfit, no fabric",
    },
    "desert_sand_sculpture": {
        "name": "Desert Sand Sculpture",
        "category": "🌿 Minimal Object Cover",
        "background": "Sahara desert at golden hour, massive sand dunes, heat shimmer",
        "outfit": "Wind-blown desert sand sculpted across body like liquid gold, NO clothing",
        "material": "Fine golden sand — flowing, sculptural, catching light like silk",
        "lighting": "Intense golden hour sun, sand particles glowing, long shadows",
        "pose": "Standing on dune crest, arms open, sand flowing in wind",
        "style": "Desert goddess editorial, elemental beauty, earth as couture",
        "negative": "no dress, no clothing, no fabric, no sand costume",
    },
    "ice_crystal_gown": {
        "name": "Ice Crystal Gown",
        "category": "🌿 Minimal Object Cover",
        "background": "Arctic ice cave, deep blue ice formations, frozen stalactites",
        "outfit": "Ice crystals and frost formations grown across body like a gown, NO clothing",
        "material": "Transparent ice crystals, frost patterns, frozen water — crystalline structure",
        "lighting": "Blue arctic ambient, ice refracting light into prisms",
        "pose": "Standing in ice cave, ice formations rising from ground around body",
        "style": "Ice queen editorial, elemental goddess, frozen couture",
        "negative": "no dress, no ice dress costume, no clothing, no fabric",
    },
}

def create_jsons():
    created, skipped = [], []
    for key, data in PRESETS.items():
        path = PRESETS_DIR / f"{key}.json"
        if path.exists():
            skipped.append(key)
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created.append(key)

    print(f"✅ JSON 생성: {len(created)}개 — {', '.join(created)}")
    if skipped:
        print(f"⚠️  이미 존재: {len(skipped)}개 — {', '.join(skipped)}")

if __name__ == "__main__":
    create_jsons()
