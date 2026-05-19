"""
LumineX core/builders.py
플랫폼별 프롬프트 빌더 함수
"""
from core.data import (
    MODEL_APPEARANCE, AGE_APPEARANCE, MODEL_TYPES, BODY_WEIGHT, BUST_SIZE, HIP_SIZE,
    OUTFIT_TYPES, MATERIALS, ENVIRONMENTS, STYLES, LIGHTING, CAMERA_ANGLES,
    FOOTWEAR, CAMERAS, HAIR_STYLES, HAIR_COLORS, MODEL_COUNT, ERA, CONCEPT,
    SPECIAL_EFFECTS, IMAGE_STYLE, PROPS, MAKEUP, ACCESSORIES, SKIN_TONES,
    POSES, WEATHER, EXPRESSION, TATTOO, BODY_OIL, BG_CROWD, COLOR_GRADES, ASPECT_RATIOS,
)

def build_gemini_prompt(data: dict, aspect: str, realism: bool) -> str:
    aspect_desc   = ASPECT_RATIOS.get(aspect, "")
    realism_kw    = "photorealistic, RAW photo, hyperrealistic, natural skin texture, pore detail, film grain, professional photographer" if realism else ""
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["gemini"] if isinstance(outfit_data, dict) else outfit_data
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')

    parts = [
        f"Professional fashion photograph, {CAMERA_ANGLES[data['angle']]}, model fills the entire frame.",
        f"{model_subject}: {MODEL_TYPES[data['model']]}{', ' + appearance if appearance else ''}.",
        f"Age: {age}." if age else "",
        f"Body adjustment: {body_str}." if body_str else "",
        f"Era: {era}." if era else "",
        f"Concept: {concept}." if concept else "",
        f"Expression: {expression}." if expression else "",
        f"Skin: {skin_tone}." if skin_tone else "",
        f"Body oil: {body_oil}." if body_oil else "",
        f"Tattoo/Body art: {tattoo}." if tattoo else "",
        f"Hair: {hair_str}." if hair_str else "",
        f"Makeup: {makeup}." if makeup else "",
        f"Accessories: {accessories}." if accessories else "",
        f"Props: {props}." if props else "",
        f"Pose: {pose}." if pose else "",
        f"Wearing: {outfit}, made of {MATERIALS[data['material']]}{', ' + footwear if footwear else ''}.",
        f"Environment: {ENVIRONMENTS[data['env']]}, background softly blurred bokeh.",
        f"Weather: {weather}." if weather else "",
        f"Background: {bg_crowd}." if bg_crowd else "",
        f"Special effects: {special_fx}." if special_fx else "",
        f"Lighting: {LIGHTING[data['light']]}.",
        f"Style reference: {STYLES[data['style']]}.",
        f"Image style: {img_style}." if img_style else "",
        f"Camera: {CAMERAS[data['camera']]}, sharp focus on model.",
        f"Color grade: {color_grade}." if color_grade else "",
    ]
    suffix = []
    if realism_kw: suffix.append(realism_kw)
    if aspect_desc: suffix.append(aspect_desc)
    suffix.append("model is the absolute primary subject, tight framing, background secondary")
    return " ".join(filter(None, parts)) + " " + ", ".join(suffix) + "."


def build_chatgpt_prompt(data: dict, aspect: str) -> str:
    aspect_map    = {"세로 2:3 — 인물 기본": "vertical portrait 2:3", "세로 3:4 — 전신샷": "vertical portrait 3:4", "가로 16:9 — 시네마틱": "wide cinematic 16:9", "가로 4:3 — 화보": "wide editorial 4:3", "정방형 1:1 — 인스타": "square format 1:1"}
    aspect_desc   = aspect_map.get(aspect, "vertical portrait 2:3")
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '')
    age           = AGE_APPEARANCE.get(data.get('age', ''), '')
    model         = MODEL_TYPES[data['model']]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit        = outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data
    material      = MATERIALS[data['material']]
    env           = ENVIRONMENTS[data['env']]
    light         = LIGHTING[data['light']]
    style         = STYLES[data['style']]
    camera        = CAMERAS[data['camera']]
    angle         = CAMERA_ANGLES[data['angle']]
    footwear      = FOOTWEAR.get(data.get('footwear', ''), '')
    pose          = POSES.get(data.get('pose', ''), '')
    color_grade   = COLOR_GRADES.get(data.get('color_grade', ''), '')
    hair_style    = HAIR_STYLES.get(data.get('hair_style', ''), '')
    hair_color    = HAIR_COLORS.get(data.get('hair_color', ''), '')
    hair_str      = " ".join(filter(None, [hair_color, hair_style]))
    makeup        = MAKEUP.get(data.get('makeup', ''), '')
    accessories   = ACCESSORIES.get(data.get('accessories', ''), '')
    skin_tone     = SKIN_TONES.get(data.get('skin_tone', ''), '')
    count_data    = MODEL_COUNT.get(data.get('model_count', '1명 — 싱글 모델 (기본)'), MODEL_COUNT['1명 — 싱글 모델 (기본)'])
    model_subject = count_data['prompt']
    era           = ERA.get(data.get('era', ''), '')
    concept       = CONCEPT.get(data.get('concept', ''), '')
    special_fx    = SPECIAL_EFFECTS.get(data.get('special_effects', ''), '')
    img_style     = IMAGE_STYLE.get(data.get('image_style', ''), '')
    props         = PROPS.get(data.get('props', ''), '')
    body_weight   = BODY_WEIGHT.get(data.get('body_weight', ''), '')
    bust_size     = BUST_SIZE.get(data.get('bust_size', ''), '')
    hip_size      = HIP_SIZE.get(data.get('hip_size', ''), '')
    body_str      = ", ".join(filter(None, [body_weight, bust_size, hip_size]))
    weather       = WEATHER.get(data.get('weather', ''), '')
    expression    = EXPRESSION.get(data.get('expression', ''), '')
    tattoo        = TATTOO.get(data.get('tattoo', ''), '')
    body_oil      = BODY_OIL.get(data.get('body_oil', ''), '')
    bg_crowd      = BG_CROWD.get(data.get('bg_crowd', ''), '')
    appearance_desc = f"with {appearance}" if appearance else ""

    return (
        f"Professional fashion photograph, {aspect_desc}, {angle}. "
        f"{model_subject} {appearance_desc}, {model}, commanding the frame. "
        f"{'Age: ' + age + '. ' if age else ''}"
        f"{'Body adjustment: ' + body_str + '. ' if body_str else ''}"
        f"{'Era: ' + era + '. ' if era else ''}"
        f"{'Concept: ' + concept + '. ' if concept else ''}"
        f"{'Expression: ' + expression + '. ' if expression else ''}"
        f"{'Skin: ' + skin_tone + '. ' if skin_tone else ''}"
        f"{'Body oil: ' + body_oil + '. ' if body_oil else ''}"
        f"{'Tattoo: ' + tattoo + '. ' if tattoo else ''}"
        f"{'Hair: ' + hair_str + '. ' if hair_str else ''}"
        f"{'Makeup: ' + makeup + '. ' if makeup else ''}"
        f"{'Accessories: ' + accessories + '. ' if accessories else ''}"
        f"{'Props: ' + props + '. ' if props else ''}"
        f"{'Pose: ' + pose + '. ' if pose else ''}"
        f"Wearing {outfit}, crafted from {material}{', ' + footwear if footwear else ''}. "
        f"Scene at {env}, {'Weather: ' + weather + '. ' if weather else ''}"
        f"{'Background: ' + bg_crowd + '. ' if bg_crowd else ''}"
        f"{'Special effects: ' + special_fx + '. ' if special_fx else ''}"
        f"bathed in {light}. "
        f"{'Image style: ' + img_style + '. ' if img_style else ''}"
        f"Style of {style}, captured on {camera}. "
        f"{'Color grade: ' + color_grade + '. ' if color_grade else ''}"
        f"Photorealistic, hyperrealistic skin texture, award-winning fashion photography."
    )


def build_midjourney_prompt(data: dict, aspect: str) -> str:
    ar_map        = {"세로 2:3 — 인물 기본":"2:3","세로 3:4 — 전신샷":"3:4","가로 16:9 — 시네마틱":"16:9","가로 4:3 — 화보":"4:3","정방형 1:1 — 인스타":"1:1"}
    ar            = ar_map.get(aspect, "2:3")
    appearance    = MODEL_APPEARANCE.get(data.get('appearance', ''), '').split(',')[0]
    model_short   = MODEL_TYPES[data['model']].split(',')[0]
    outfit_data   = OUTFIT_TYPES[data['outfit']]
    outfit_short  = (outfit_data["chatgpt"] if isinstance(outfit_data, dict) else outfit_data).split(',')[0]
    material_short = MATERIALS[data['material']].split(',')[0]
    env_short     = ENVIRONMENTS[data['env']].split(',')[0]
    light_short   = LIGHTING[data['light']].split(',')[0]
    style_short   = STYLES[data['style']].split(',')[0]
    footwear_short = FOOTWEAR.get(data.get('footwear', ''), '').split(',')[0]
    tags = [t for t in [appearance, model_short, outfit_short, material_short, footwear_short, env_short, light_short, style_short, "photorealistic", "hyperrealistic", "fashion editorial", "sharp focus", "8K"] if t]
    return f"{', '.join(tags)} --ar {ar} --style raw --q 2"