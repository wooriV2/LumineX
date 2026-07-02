"""
LumineX 🌀 환경 일체 바디페인팅 (Environment Merge Bodypaint)
21종 프리셋 생성 스크립트

검증 결과:
G1 패턴/직물 6종 — 전원 SSS
G2 자연환경 5종 — SSS/SS (forest_bark 스킵)
G3 건축/소재 5종 — 전원 SSS (brick_wall 스킵)
G4 예술/회화 6종 — 전원 SSS

실행: python preset_builders/build_merge_bodypaint_presets.py
"""

import json
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")

PRESETS = {

    # ════════════════════════════════════════
    # G1 패턴/직물 6종 (전원 SSS)
    # ════════════════════════════════════════

    "merge_butterfly_fabric": {
        "tag": "Merge Butterfly Fabric",
        "subject": "a woman lying face down on a butterfly-patterned fabric",
        "body": "full body visible, back toward camera, hair in tight bun",
        "outfit": "Body fully painted with: the exact same butterfly pattern as the fabric beneath her — identical cream base color, identical golden yellow butterflies at the exact same scale, spacing and orientation, continuing seamlessly from the fabric surface across her body without any color shift or break. Her body is virtually invisible within the pattern. Only the subtle three-dimensional curve of her back and the shadow around her edges distinguish her from the surface.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large decorative fabric covered entirely in golden yellow butterfly patterns fills the entire frame from edge to edge — cream background with scattered golden monarch butterflies at various sizes",
        "lighting": "natural soft diffused studio light",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_floral_wallpaper": {
        "tag": "Merge Floral Wallpaper",
        "subject": "a woman lying face up on a floral wallpaper surface",
        "body": "full body visible, arms slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same dense floral wallpaper pattern as the surface beneath her — identical blooming roses, peonies and botanical motifs in the same scale, color and placement, continuing seamlessly from the wallpaper across her skin without any offset or break. Her body is virtually invisible within the pattern.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A vintage floral wallpaper fills the entire frame from edge to edge — dense repeating pattern of blooming roses and peonies in blush pink, cream and sage green",
        "lighting": "soft flat studio light, even diffused illumination",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_leopard_fabric": {
        "tag": "Merge Leopard Fabric",
        "subject": "a woman lying face down on a leopard-print fabric",
        "body": "full body visible, back toward camera, hair tied back",
        "outfit": "Body fully painted with: the exact same leopard print pattern as the fabric beneath her — identical tawny golden base, identical dark brown rosette spots at the exact same scale and distribution, continuing seamlessly from the fabric surface across her skin without any color shift or break. Her body is virtually invisible within the animal print.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large leopard-print fabric fills the entire frame from edge to edge — warm tawny golden background with irregular dark brown rosette spots distributed across the entire surface",
        "lighting": "natural soft diffused studio light",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_mandala_carpet": {
        "tag": "Merge Mandala Carpet",
        "subject": "a woman lying face up on a mandala carpet in meditation pose",
        "body": "full body visible, arms slightly away from sides, eyes closed, serene expression",
        "outfit": "Body fully painted with: the exact same mandala carpet pattern as the surface beneath her — identical geometric mandala motifs in deep burgundy, gold and ivory at the exact same scale and radial symmetry, continuing seamlessly from the carpet surface across her skin without any offset or break.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A richly patterned mandala carpet fills the entire frame from edge to edge — intricate geometric mandala in deep burgundy, gold and ivory with repeating radial symmetry",
        "lighting": "warm even gallery light",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_toile_pattern": {
        "tag": "Merge Toile Pattern",
        "subject": "a woman lying face up on a toile de Jouy fabric surface",
        "body": "full body visible, arms relaxed, eyes closed",
        "outfit": "Body fully painted with: the exact same toile de Jouy pastoral scene pattern as the surface beneath her — identical cream background with identical blue pastoral figures, trees and landscape motifs at the exact same scale, continuing seamlessly from the fabric across her skin without any offset or break. The toile scene passes straight through her body without interruption.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A toile de Jouy fabric fills the entire frame from edge to edge — cream background with repeating blue pastoral scenes of figures, trees and countryside landscapes",
        "lighting": "soft flat studio light",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_tartan_plaid": {
        "tag": "Merge Tartan Plaid",
        "subject": "a woman lying face down on a tartan plaid fabric",
        "body": "full body visible, back toward camera, arms at sides",
        "outfit": "Body fully painted with: the exact same tartan plaid pattern as the fabric beneath her — identical color stripes running at the exact same angles, spacing and width, the grid lines continuing seamlessly from the fabric across her body without any misalignment or color shift. The tartan stripes cross her body as if she were simply another fold of the fabric.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large tartan plaid fabric fills the entire frame from edge to edge — classic Scottish tartan in deep red, navy and forest green with intersecting stripe grid",
        "lighting": "flat even studio light",
        "style": "fine art camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    # ════════════════════════════════════════
    # G2 자연환경 5종 (forest_bark 스킵)
    # ════════════════════════════════════════

    "merge_salt_flat_sky": {
        "tag": "Merge Salt Flat Sky",
        "subject": "a woman standing barefoot on the Salar de Uyuni salt flat",
        "body": "full body visible, arms relaxed at sides, eyes closed, facing camera",
        "outfit": "A fine art optical illusion photograph. The landscape passes straight through her body — her legs and lower body painted with the exact same flat white salt surface as the ground, fine thin salt polygon seam lines, delicate shallow hairline cracks. Her torso transitions through pale blue-white gradient. Her upper body painted the exact same bright misty pale blue-white as the overcast sky. No visible outline, no silhouette edge. The boundary does not exist.",
        "material": "environmental camouflage body paint, trompe-l'oeil landscape projection",
        "environment": "Salar de Uyuni salt flat in Bolivia, flat overcast sky, bright pale misty white-blue atmosphere, cracked white salt crust ground",
        "lighting": "natural flat overcast light, no harsh shadows",
        "style": "fine art environmental camouflage photography, trompe-l'oeil optical illusion",
        "quality": "Eye-level camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic, fine art environmental camouflage photography"
    },

    "merge_autumn_leaves_floor": {
        "tag": "Merge Autumn Leaves Floor",
        "subject": "a woman lying face up on a forest floor covered in autumn leaves",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed, facing camera above",
        "outfit": "Body fully painted with: the exact same autumn leaf pattern as the ground beneath her — identical orange red yellow brown maple and oak leaf shapes at the exact same scale, overlap pattern and orientation, continuing seamlessly from the forest floor across her body without any color shift or break. As if the leaf carpet pattern passes straight through her body without interruption. Her body is virtually invisible within the leaf carpet.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A forest floor covered entirely in fallen autumn leaves fills the entire frame from edge to edge — dense overlapping maple and oak leaves in deep orange, burnt red, golden yellow and chocolate brown",
        "lighting": "soft diffused autumn forest light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_coral_reef_water": {
        "tag": "Merge Coral Reef Water",
        "subject": "a woman standing against a staghorn coral reef wall underwater",
        "body": "full body visible, arms relaxed at sides, eyes closed, facing camera",
        "outfit": "Body fully painted with: the exact same vivid orange-pink staghorn coral branching texture as the reef wall behind her — identical branch patterns at the exact same scale and density, identical warm coral color, continuing seamlessly from the coral wall across her skin without any color shift or break. Her body is virtually invisible against the coral wall.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A wall of staghorn coral fills the entire frame from edge to edge — dense branching coral in vivid orange-pink, every branch identical in color and texture, lit by filtered tropical sunlight from above",
        "lighting": "bright filtered tropical sunlight, vivid saturated underwater colors",
        "style": "fine art environmental camouflage photography, underwater eye-level camera",
        "quality": "Eye-level underwater camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_sand_dunes": {
        "tag": "Merge Sand Dunes",
        "subject": "a woman lying on her side along a Saharan sand dune ridge",
        "body": "full body visible, body curving naturally with the dune shape, arms relaxed, eyes closed",
        "outfit": "Body fully painted with: the exact same golden sand ripple texture as the dune beneath her — identical sinuous parallel ripple lines at the exact same spacing and diagonal angle, identical warm amber-to-shadow gradient, continuing seamlessly from the dune surface across her skin without any color shift or break. The curve of her body echoes the dune ridgeline. Her body is virtually invisible within the dune.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A Saharan sand dune fills the entire frame from edge to edge — smooth wind-sculpted ridges of fine golden sand, sinuous parallel ripple lines running diagonally, warm amber tones of late afternoon light",
        "lighting": "warm late afternoon desert side-light",
        "style": "fine art environmental camouflage photography, low side-light camera angle",
        "quality": "Low side-light camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_moss_stone_ground": {
        "tag": "Merge Moss Stone Ground",
        "subject": "a woman lying face up on ancient moss-covered stone paving",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same grey stone and green moss texture as the ground beneath her — identical cool grey granite base with identical vivid green moss patches at the exact same scale and placement, identical orange lichen and dark water stain markings, continuing seamlessly from the stone surface across her skin without any color shift or break. The stone paving pattern passes straight through her body without interruption.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "Ancient moss-covered stone paving fills the entire frame from edge to edge — irregular granite slabs in cool grey with deep joint lines, dense vivid green moss blanketing the surface in organic patches, orange lichen and dark water stain",
        "lighting": "soft overcast diffused light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    # ════════════════════════════════════════
    # G3 건축/소재 5종 (brick_wall 스킵)
    # ════════════════════════════════════════

    "merge_clockwork_gears": {
        "tag": "Merge Clockwork Gears",
        "subject": "a woman lying face up within an antique clock mechanism",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same brass and copper clockwork texture as the mechanism surrounding her — identical gear tooth patterns, identical coil lines, identical engraving marks and metal patina at the exact same scale, continuing seamlessly from the mechanism surface across her skin without any color shift or break. Her body IS the clockwork mechanism itself — she IS the gears. Her body is virtually invisible within the clockwork.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "The open movement of a massive antique clock mechanism fills the entire frame from edge to edge — interlocking brass and copper gear wheels of every size, escapement pallets, coiled mainsprings, jeweled pivot points, warm golden-brown engraved metal",
        "lighting": "warm focused amber studio light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, steampunk fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_marble_column_wall": {
        "tag": "Merge Marble Column Wall",
        "subject": "a woman lying face up on a white Carrara marble surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same white Carrara marble texture as the surface beneath her — identical flowing grey and gold vein patterns at the exact same scale, direction and branching, identical surface sheen and translucency, the veins continuing seamlessly from the marble surface across her skin without any offset or interruption. As if the marble veins pass straight through her body. Her body is virtually invisible against the marble.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large slab of white Carrara marble fills the entire frame from edge to edge — smooth polished surface with flowing grey and gold mineral veins branching and curving across the stone, faint translucent depth in the white",
        "lighting": "soft museum directional light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_islamic_tile_wall": {
        "tag": "Merge Islamic Tile Wall",
        "subject": "a woman lying face up on a hand-painted Islamic geometric tile surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Islamic geometric tile pattern as the surface beneath her — identical turquoise cobalt white terracotta eight-pointed star polygon motifs at the exact same scale, with grout lines continuing seamlessly across her skin without any offset, color shift or break. As if the tile pattern passes straight through her body without interruption. Her body is virtually invisible within the tiles.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A surface of hand-painted Islamic geometric tiles fills the entire frame from edge to edge — repeating eight-pointed star polygon pattern in deep turquoise, cobalt blue, white and terracotta, every tile edge sharp, crisp pale cream grout lines",
        "lighting": "flat even raking light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_stained_glass_window": {
        "tag": "Merge Stained Glass Window",
        "subject": "a woman standing within a Gothic cathedral stained glass window",
        "body": "full body visible, arms relaxed at sides, eyes closed, facing camera",
        "outfit": "Total immersion illusion — her body IS the stained glass itself. She is not standing in front of the glass, she IS the glass. The stained glass light passes straight through her body: ruby red panels glow through her torso, sapphire blue panels illuminate her legs, emerald panels wash her arms. Her body has NO visible outline — indistinguishable from the window around her. Her form is only revealed by the subtle shadow at her edges.",
        "material": "her body is made of the same colored glass as the window itself, luminous and transparent",
        "environment": "A large Gothic cathedral stained glass window fills the entire frame from edge to edge — bold black lead lines dividing the surface into panels of deep ruby red, sapphire blue, emerald green and amber gold, luminous light pouring through",
        "lighting": "luminous transmitted cathedral light glowing from behind, jewel-tone colored light",
        "style": "fine art environmental immersion photography, eye-level camera angle",
        "quality": "Eye-level camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_circuit_board": {
        "tag": "Merge Circuit Board",
        "subject": "a woman lying face up on a large printed circuit board",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same PCB texture as the board beneath her — identical vivid green substrate, identical copper trace lines branching at right angles at the exact same scale, identical silver solder points and black IC chip rectangles, continuing seamlessly from the board surface across her skin without any color shift or break. As if the circuit board pattern passes straight through her body without interruption.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large printed circuit board fills the entire frame from edge to edge — vivid green FR4 substrate with copper trace lines, silver solder points at intersections, rectangular black IC chips, gold-plated edge connectors",
        "lighting": "flat cool studio light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, cyberpunk tech fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    # ════════════════════════════════════════
    # G4 예술/회화 6종 (전원 SSS)
    # ════════════════════════════════════════

    "merge_klimt_gold_mural": {
        "tag": "Merge Klimt Gold Mural",
        "subject": "a woman lying face up on a Gustav Klimt style gold mural surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Klimt gold mosaic pattern as the mural beneath her — identical gold leaf shimmer, identical spiral and rectangle mosaic motifs in turquoise ruby ivory and black at the exact same scale and placement, continuing seamlessly from the mural surface across her skin without any color shift or break. As if the Klimt pattern passes straight through her body without interruption. Her body is virtually invisible within the painting.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large wall mural painted in the style of Gustav Klimt fills the entire frame from edge to edge — shimmering gold leaf background with swirling spiral and rectangle mosaic motifs in turquoise, ruby, ivory and black, dense decorative patterns in the manner of The Kiss",
        "lighting": "warm even gallery light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, Art Nouveau fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_vangogh_starry": {
        "tag": "Merge Van Gogh Starry",
        "subject": "a woman lying face up on a Van Gogh Starry Night canvas",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Van Gogh impasto swirling texture as the canvas — identical ultramarine and cobalt blue turbulent brushstroke patterns, identical golden star halos, paint ridges continuing seamlessly from the canvas surface across her skin at the exact same scale and direction without any color shift or break. Her body is virtually invisible within the painting.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large canvas reproduction of Van Gogh's Starry Night style fills the entire frame from edge to edge — turbulent ultramarine and cobalt blue swirling brushstroke patterns, radiant golden yellow star halos, thick impasto oil paint ridges",
        "lighting": "flat even gallery light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, Post-Impressionist fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_ukiyo_wave_print": {
        "tag": "Merge Ukiyo Wave Print",
        "subject": "a woman lying face up on a Hokusai Great Wave ukiyo-e print surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Hokusai woodblock print style as the wave surface — identical indigo Prussian blue wave line patterns and white foam tips, identical flat graphic print texture and woodblock grain, continuing seamlessly from the print surface across her skin at the exact same scale without any color shift or break. Her body is virtually invisible within the print.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large reproduction of Hokusai's Great Wave style ukiyo-e woodblock print fills the entire frame from edge to edge — bold indigo and Prussian blue wave crests with white foam claw tips, flat graphic woodblock print style with visible grain texture",
        "lighting": "flat even diffused light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, Japanese ukiyo-e fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_mondrian_grid": {
        "tag": "Merge Mondrian Grid",
        "subject": "a woman lying face up on a Mondrian De Stijl canvas surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Mondrian grid pattern as the canvas — identical bold black horizontal and vertical lines at the exact same position and width passing continuously across her body, identical primary red yellow blue white blocks in the exact same placement, continuing seamlessly from the canvas surface across her skin without any offset, color shift or break. Her body is virtually invisible within the painting.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large Mondrian De Stijl canvas fills the entire frame from edge to edge — bold black horizontal and vertical lines of uniform width dividing the entire surface into rectangular blocks of primary red, primary yellow, primary blue and white",
        "lighting": "flat even studio light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, De Stijl abstract fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_pollock_splatter": {
        "tag": "Merge Pollock Splatter",
        "subject": "a woman lying face up on a Jackson Pollock action painting canvas",
        "body": "full body visible, arms spread wide, hair loose, eyes closed",
        "outfit": "Body fully painted with: the exact same Pollock drip pattern as the canvas — identical black white sienna red splatter trails looping and crossing at the exact same density and directionality, continuing seamlessly from the canvas surface across her skin without any color shift or break. Her body is virtually invisible within the painting. Only the subtle three-dimensional rise of her form and the shadow pooling at her sides distinguish her from the canvas.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A large Jackson Pollock action painting canvas laid flat fills the entire frame from edge to edge — chaotic overlapping drip and splatter trails in black, white, raw sienna and cadmium red, gestural poured lines looping and crossing in all directions",
        "lighting": "flat even studio light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, Abstract Expressionist fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

    "merge_byzantine_mosaic": {
        "tag": "Merge Byzantine Mosaic",
        "subject": "a woman lying face up on a Byzantine mosaic surface",
        "body": "full body visible, arms relaxed slightly away from sides, eyes closed",
        "outfit": "Body fully painted with: the exact same Byzantine mosaic texture — identical gold silver lapis lazuli blue terracotta red and ivory tesserae at the exact same scale and irregular angle, grout lines continuing seamlessly from the mosaic surface across her skin without any color shift or break. Her body is virtually invisible within the mosaic. Only the subtle three-dimensional rise of her form and the faint shadow at her sides distinguish her from the wall.",
        "material": "professional body paint pigments applied directly on bare skin, NOT clothing",
        "environment": "A Byzantine apse mosaic fills the entire frame from edge to edge — thousands of small square tesserae in gold, silver, lapis lazuli blue, terracotta red and ivory, hand-set with slight irregular angles, grout lines forming geometric patterns in the manner of Ravenna's San Vitale mosaics",
        "lighting": "warm directional museum light",
        "style": "fine art environmental camouflage photography, overhead top-down camera angle, Byzantine art fine art",
        "quality": "Overhead top-down camera angle, portrait 2:3 vertical, ultra-detailed, hyperrealistic"
    },

}


def save_presets(presets: dict, output_dir: Path) -> list:
    output_dir.mkdir(parents=True, exist_ok=True)
    saved = []
    for name, data in presets.items():
        path = output_dir / f"{name}.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        saved.append(name)
        print(f"  ✅ {name}.json")
    return saved


if __name__ == "__main__":
    print("🌀 환경 일체 바디페인팅 프리셋 생성")
    print(f"   총 {len(PRESETS)}종")
    print()

    answer = input("저장할까요? (y/n): ")
    if answer.lower() == "y":
        saved = save_presets(PRESETS, PRESETS_DIR)
        print(f"\n✅ {len(saved)}개 프리셋 저장 완료")
        print("\ndashboard.py PRESET_CATEGORIES 추가 목록:")
        print('    "🌀 환경 일체 바디페인팅": [')
        for name in saved:
            print(f'        "{name}",')
        print("    ],")
    else:
        print("저장 취소됨")
