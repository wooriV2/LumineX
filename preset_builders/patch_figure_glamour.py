# -*- coding: utf-8 -*-
"""
patch_figure_glamour.py
💎 Figure Glamour 카테고리 37종 JSON 생성 + presets_meta.py 패치
실행: python preset_builders\patch_figure_glamour.py  (프로젝트 루트에서)
"""

import json
import os
import ast

PRESET_DIR = "presets"
META_PATH  = "core/presets_meta.py"

# ── 37종 프리셋 정의 ───────────────────────────────────────────
PRESETS = {
    # ── A. 슈퍼 글래머 (4종) ──────────────────────────────────
    "super_lingerie_glamour": {
        "subject": "a super glamour model with impossibly tiny corseted waist, 0.55 waist-to-hip ratio, extremely wide round heavy hips, maximum pinup hourglass silhouette, lush full bust",
        "appearance": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
        "lighting": "soft beauty dish light, even flattering illumination",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "super_sheer_glamour": {
        "subject": "a super glamour model with impossibly tiny corseted waist, 0.55 waist-to-hip ratio, extremely wide round heavy hips, maximum pinup hourglass silhouette, lush full bust",
        "appearance": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "super_slit_glamour": {
        "subject": "a super glamour model with impossibly tiny corseted waist, 0.55 waist-to-hip ratio, extremely wide round heavy hips, maximum pinup hourglass silhouette, lush full bust",
        "appearance": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "super_corset_glamour": {
        "subject": "a super glamour model with impossibly tiny corseted waist, 0.55 waist-to-hip ratio, extremely wide round heavy hips, maximum pinup hourglass silhouette, lush full bust",
        "appearance": "Korean beauty, fair porcelain skin, sharp elegant facial features, K-beauty aesthetic",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── B. 핫 글래머 (5종) ──────────────────────────────────
    "hot_bikini_glamour": {
        "subject": "a hot glamour model with dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",
        "appearance": "Brazilian beauty, bronzed tan glowing skin, voluptuous curves, tropical glamour",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "luxury infinity pool edge, tropical resort, palm trees",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "playful vibrant mood, energetic joyful atmosphere, fresh editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "hot_lingerie_glamour": {
        "subject": "a hot glamour model with dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",
        "appearance": "Brazilian beauty, bronzed tan glowing skin, voluptuous curves, tropical glamour",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
        "lighting": "soft beauty dish light, even flattering illumination",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "hot_sheer_glamour": {
        "subject": "a hot glamour model with dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",
        "appearance": "Brazilian beauty, bronzed tan glowing skin, voluptuous curves, tropical glamour",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "hot_slit_glamour": {
        "subject": "a hot glamour model with dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",
        "appearance": "Brazilian beauty, bronzed tan glowing skin, voluptuous curves, tropical glamour",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Santorini cliff, blue dome church, Aegean sea at night",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "hot_corset_glamour": {
        "subject": "a hot glamour model with dramatically cinched narrow waist, va-va-voom wide round hips, 0.65 waist-to-hip ratio, full bust, smoldering hourglass figure, red carpet curves",
        "appearance": "Brazilian beauty, bronzed tan glowing skin, voluptuous curves, tropical glamour",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── C. VS 앤젤 (5종) ──────────────────────────────────────
    "angel_bikini_glamour": {
        "subject": "a Victoria's Secret Angel body with toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "playful vibrant mood, energetic joyful atmosphere, fresh editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "tanning oil sheen, golden bronzed glistening skin, beach goddess oil",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "angel_lingerie_glamour": {
        "subject": "a Victoria's Secret Angel body with toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "Paris fashion week modernist runway stage, fashion show",
        "lighting": "professional octabox strobe, high-contrast glamour lighting",
        "style": "Victoria's Secret fashion show editorial, VS Angel body, glamorous lingerie runway",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "angel_sheer_glamour": {
        "subject": "a Victoria's Secret Angel body with toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Paris fashion week modernist runway stage, fashion show",
        "lighting": "professional octabox strobe, high-contrast glamour lighting",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "angel_slit_glamour": {
        "subject": "a Victoria's Secret Angel body with toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "angel_corset_glamour": {
        "subject": "a Victoria's Secret Angel body with toned flat abs, model-perfect 34-24-35 proportions, legs over 90cm long, subtle feminine hourglass, runway-ready athletic glamour",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "professional octabox strobe, high-contrast glamour lighting",
        "style": "Balmain power glamour, structured couture editorial, bold luxury",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── D. 블랙 글래머 (5종) ─────────────────────────────────
    "black_bikini_glamour": {
        "subject": "a Black beauty hourglass goddess with impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks, African goddess proportions",
        "appearance": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "black_lingerie_glamour": {
        "subject": "a Black beauty hourglass goddess with impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks, African goddess proportions",
        "appearance": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Balmain power glamour, structured couture editorial, bold luxury",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "black_sheer_glamour": {
        "subject": "a Black beauty hourglass goddess with impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks, African goddess proportions",
        "appearance": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Balmain power glamour, structured couture editorial, bold luxury",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "black_slit_glamour": {
        "subject": "a Black beauty hourglass goddess with impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks, African goddess proportions",
        "appearance": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Balmain power glamour, structured couture editorial, bold luxury",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "black_corset_glamour": {
        "subject": "a Black beauty hourglass goddess with impossibly dramatic waist-to-hip ratio, extremely wide round hips, ultra-narrow waist, very thick powerful thighs, powerfully lifted full round buttocks, African goddess proportions",
        "appearance": "Black beauty, rich deep dark skin, powerful striking features, African goddess",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "dark baroque opulent chamber, velvet and gold interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Alexander McQueen dramatic fashion editorial, dark artistic photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── E. 브라질 부티 (5종) ─────────────────────────────────
    "brazil_bikini_glamour": {
        "subject": "a Brazilian carnival goddess with massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, heavy full rounded buttocks projecting dramatically, samba dancer curves",
        "appearance": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "Miami Beach sunset, Ocean Drive, warm pink sky",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "playful vibrant mood, energetic joyful atmosphere, fresh editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "tanning oil sheen, golden bronzed glistening skin, beach goddess oil",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "brazil_lingerie_glamour": {
        "subject": "a Brazilian carnival goddess with massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, samba dancer curves",
        "appearance": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
        "lighting": "soft beauty dish light, even flattering illumination",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "brazil_sheer_glamour": {
        "subject": "a Brazilian carnival goddess with massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, samba dancer curves",
        "appearance": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "brazil_slit_glamour": {
        "subject": "a Brazilian carnival goddess with massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, samba dancer curves",
        "appearance": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Santorini cliff, blue dome church, Aegean sea at night",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "brazil_corset_glamour": {
        "subject": "a Brazilian carnival goddess with massive round bubble butt dominating silhouette, extremely wide hips with very narrow waist, powerfully thick thighs, samba dancer curves",
        "appearance": "Brazilian beauty, bronzed tan skin, full voluptuous curves, tropical glamour",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── F. 콜롬비안 레게톤 (4종) ────────────────────────────
    "latina_lingerie_glamour": {
        "subject": "a Colombian reggaeton goddess with extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, thick powerful thighs, bronzed Latin skin glistening",
        "appearance": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "luxury hotel suite, penthouse bedroom, floor-to-ceiling windows",
        "lighting": "soft beauty dish light, even flattering illumination",
        "style": "Harper's Bazaar sensual fashion editorial, cinematic glamour",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "latina_sheer_glamour": {
        "subject": "a Colombian reggaeton goddess with extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, thick powerful thighs, bronzed Latin skin glistening",
        "appearance": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "latina_slit_glamour": {
        "subject": "a Colombian reggaeton goddess with extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, thick powerful thighs, bronzed Latin skin glistening",
        "appearance": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Santorini cliff, blue dome church, Aegean sea at night",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "latina_corset_glamour": {
        "subject": "a Colombian reggaeton goddess with extreme exaggerated hourglass figure, impossibly tiny cinched waist, explosively wide dramatic round hips, full sculpted bust, thick powerful thighs, bronzed Latin skin glistening",
        "appearance": "Colombian beauty, exotic Latin features, olive skin, sultry dark eyes",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── I. 레전드 바스트 (4종) ──────────────────────────────
    "bust_bikini_glamour": {
        "subject": "a legendary bust goddess with mythologically enormous full bust completely dominating entire silhouette, Rubenesque upper body, maximalist buxom editorial, larger-than-life chest presence",
        "appearance": "Latina beauty, bronzed tan glowing skin, voluptuous curves",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "Maldives overwater villa, crystal turquoise sea, tropical paradise",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "playful vibrant mood, energetic joyful atmosphere, fresh editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "tanning oil sheen, golden bronzed glistening skin, beach goddess oil",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "bust_slit_glamour": {
        "subject": "a legendary bust goddess with mythologically enormous full bust completely dominating entire silhouette, Rubenesque upper body, maximalist buxom editorial, larger-than-life chest presence",
        "appearance": "Latina beauty, bronzed tan glowing skin, voluptuous curves",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "Santorini cliff, blue dome church, Aegean sea at night",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "luxury opulent mood, sophisticated elegant atmosphere, high-end editorial",
        "color_grade": "warm golden film grade, vintage golden hour tone",
        "body_oil": "satin skin finish, smooth silky sheen, elegant glow",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "bust_sheer_glamour": {
        "subject": "a legendary bust goddess with mythologically enormous full bust completely dominating entire silhouette, Rubenesque upper body, maximalist buxom editorial, larger-than-life chest presence",
        "appearance": "Latina beauty, bronzed tan glowing skin, voluptuous curves",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "Monaco luxury terrace, Mediterranean night view, superyachts harbor",
        "lighting": "professional octabox strobe, high-contrast glamour lighting",
        "style": "Thierry Mugler power fashion editorial, dark haute couture photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "bust_corset_glamour": {
        "subject": "a legendary bust goddess with mythologically enormous full bust completely dominating entire silhouette, Rubenesque upper body, maximalist buxom editorial, larger-than-life chest presence",
        "appearance": "Latina beauty, bronzed tan glowing skin, voluptuous curves",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "Dubai luxury penthouse rooftop, city skyline at night, Burj Khalifa view",
        "lighting": "golden hour warm backlight, skin luminosity, glowing",
        "style": "Versace campaign bold luxury glamour, structured couture editorial",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "cinematic teal and orange color grade, Hollywood film look",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },

    # ── J. 아마조네스 (5종) ──────────────────────────────────
    "amazon_bikini_glamour": {
        "subject": "an Amazon warrior goddess with powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "micro string bikini, tiny triangle top, string thong bottom, minimal coverage, Sports Illustrated swimsuit style",
        "material": "wet-look spandex, soaking wet appearance, body-hugging",
        "environment": "dramatic volcanic cliff, stormy ocean, powerful nature",
        "lighting": "strong rim backlight, silhouette definition, halo effect",
        "style": "Sports Illustrated swimsuit editorial, luxury beach photography",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "amazon_lingerie_glamour": {
        "subject": "an Amazon warrior goddess with powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "luxury silk lace fashion set, elegant runway lingerie editorial, glamorous couture",
        "material": "delicate lace fabric, intricate lacework, feminine luxury texture",
        "environment": "Palace of Versailles golden hall, ornate chandeliers, luxury interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Balmain power glamour, structured couture editorial, bold luxury",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "amazon_sheer_glamour": {
        "subject": "an Amazon warrior goddess with powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "sheer mesh fashion bodysuit, avant-garde couture editorial, artistic runway",
        "material": "crystal mesh, rhinestone-embellished sheer fabric",
        "environment": "dramatic volcanic cliff, stormy ocean, powerful nature",
        "lighting": "strong rim backlight, silhouette definition, halo effect",
        "style": "Alexander McQueen dramatic fashion editorial, dark artistic photography",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "amazon_slit_glamour": {
        "subject": "an Amazon warrior goddess with powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "structured crop top, asymmetrical high-slit runway skirt, fashion editorial",
        "material": "liquid satin, ultra-glossy wet-look finish",
        "environment": "dramatic volcanic cliff, stormy ocean, powerful nature",
        "lighting": "strong rim backlight, silhouette definition, halo effect",
        "style": "Alexander McQueen dramatic fashion editorial, dark artistic photography",
        "mood": "powerful commanding mood, intense dominant atmosphere, fierce editorial",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "high gloss body oil, heavily oiled glistening skin, wet-look shine",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
    "amazon_corset_glamour": {
        "subject": "an Amazon warrior goddess with powerfully muscular sculpted frame, defined abs, strong broad shoulders, yet dramatic feminine waist-to-hip curve, battle-hardened glamour, oiled skin",
        "appearance": "Mixed race exotic beauty, unique blend of features, strikingly beautiful face",
        "outfit": "corset mini dress, cinched waist, décolletage emphasis, dramatic silhouette",
        "material": "metallic gold foil, mirror-finish gold surface",
        "environment": "dark baroque opulent chamber, velvet and gold interior",
        "lighting": "dramatic chiaroscuro, deep shadows and sharp highlights",
        "style": "Alexander McQueen dramatic fashion editorial, dark artistic photography",
        "mood": "dark glamour mood, intense dramatic atmosphere, powerful editorial energy",
        "color_grade": "dark moody color grade, deep shadows, dramatic contrast",
        "body_oil": "metallic body gloss, chrome-like skin sheen, futuristic metallic finish",
        "framing": "full body head-to-toe shot, model fills the entire frame",
        "quality": "ultra-sharp, 8K, professional photography"
    },
}

# ── 1. JSON 파일 생성 ──────────────────────────────────────────
os.makedirs(PRESET_DIR, exist_ok=True)
created = []
for key, data in PRESETS.items():
    path = os.path.join(PRESET_DIR, f"{key}.json")
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    created.append(key)

print(f"✅ JSON {len(created)}개 생성 완료")

# ── 2. presets_meta.py 에 카테고리 추가 ───────────────────────
meta_content = open(META_PATH, encoding="utf-8").read()

# 카테고리 키 목록
keys_list = "\n".join(f'        "{k}",' for k in PRESETS.keys())

new_category = f'''
    "💎 Figure Glamour": [
{keys_list}
    ],'''

# HOF 키 목록 (37종 전부)
hof_keys = list(PRESETS.keys())

# 삽입 위치: 마지막 카테고리 닫는 } 바로 앞
insert_marker = '\n}\n\n\n# HOF tier'
if insert_marker not in meta_content:
    insert_marker = '\n}\n\n# HOF tier'

meta_content = meta_content.replace(
    insert_marker,
    new_category + '\n}' + '\n\n# HOF tier',
    1
)

with open(META_PATH, "w", encoding="utf-8") as f:
    f.write(meta_content)

print(f"✅ presets_meta.py 카테고리 추가 완료")

# ── 3. hof_tier.py 에 HOF 키 추가 ────────────────────────────
HOF_PATH = "core/hof_tier.py"
hof_content = open(HOF_PATH, encoding="utf-8").read()

hof_lines = "\n".join(f'    "{k}",' for k in hof_keys)
new_hof_block = f'''
    # ── 💎 Figure Glamour HOF 37종 ──────────────────────────────
{hof_lines}'''

insert_hof_marker = "\n}\n\n\ndef add_hof"
if insert_hof_marker not in hof_content:
    insert_hof_marker = "\n}\n\n\ndef add_hof"

hof_content = hof_content.replace(
    "}\n\n\ndef add_hof",
    new_hof_block + "\n}\n\n\ndef add_hof",
    1
)

with open(HOF_PATH, "w", encoding="utf-8") as f:
    f.write(hof_content)

# 검증
import ast
try:
    ast.parse(hof_content)
    print("✅ hof_tier.py Syntax OK")
except SyntaxError as e:
    print(f"❌ hof_tier.py SyntaxError: {e}")

# HOF 개수 확인
exec(hof_content)
print(f"✅ HOF_TIER 총 {len(HOF_TIER)}종 확인")
print(f"✅ 모든 작업 완료!")
print(f"\n📋 커밋 명령어:")
print(f'git add core/ presets/; git commit -m "💎 Figure Glamour 37종 추가 (HOF)"; git push')
