"""
add_cultural_bodypaint_v28.py
전통&문화 바디페인팅 52종 — 개별 JSON 파일 생성 패치

실행 위치: C:\\Dev\\LumineX\\ (프로젝트 루트)
실행 방법: python preset_builders/add_cultural_bodypaint_v28.py

구조: presets/ 폴더에 preset_name.json 개별 파일로 저장
고정형 42종 / 개방형 10종
"""

import json
from pathlib import Path

ROOT = Path(__file__).parent.parent
PRESET_DIR = ROOT / "presets"
DASHBOARD_FILE = ROOT / "dashboard.py"

# ── 개방형 10종 ────────────────────────────────────────────
OPEN_PRESETS = {
    "samurai_bodypaint": {
        "tag": "Samurai Body Paint",
        "subject": "a fine art female model with samurai-inspired body paint",
        "body": "strong athletic model, warrior stance, body art canvas",
        "outfit": "full body paint art — samurai clan crest and irezumi tattoo patterns, armor motifs and dragon designs, artistic body coverage, painted on bare skin",
        "material": "fine art body paint, traditional Japanese warrior motif brushwork",
        "environment": "samurai castle courtyard, stone walls, cherry blossoms falling",
        "lighting": "overcast dramatic sky, cool blue-grey light, falling petal atmosphere",
        "style": "fine art samurai body paint editorial, Japanese warrior fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "ninja_bodypaint": {
        "tag": "Kunoichi Body Paint",
        "subject": "a fine art female model with kunoichi ninja stealth body paint",
        "body": "athletic stealth model, Japanese ninja beauty, body art canvas",
        "outfit": "full body paint art — geometric shadow and concealment patterns, clan crest motifs, dark stealth-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, dark geometric shadow pattern brushwork",
        "environment": "Japanese castle night, moonlit stone wall, cherry blossom moonlight",
        "lighting": "dramatic moonlight, deep shadow contrast, mysterious Japanese night atmosphere",
        "style": "fine art kunoichi body paint editorial, Japanese ninja art photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "hanbok_modern_bodypaint": {
        "tag": "Modern Hanbok Body Paint",
        "subject": "a fine art female model with contemporary Korean hanbok fusion body paint",
        "body": "elegant modern model, contemporary Korean beauty, body art canvas",
        "outfit": "full body paint art — modern hanbok silhouette abstracted, jeogori and chima elements reinterpreted in contemporary palette, artistic Korean heritage fusion body coverage, painted on bare skin",
        "material": "fine art body paint, contemporary Korean aesthetic brushwork",
        "environment": "Seoul modern gallery, clean white walls, contemporary Korean art space",
        "lighting": "gallery clean white studio light, contemporary minimal atmosphere",
        "style": "fine art contemporary hanbok body paint editorial, modern Korean fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "tang_dynasty_bodypaint": {
        "tag": "Tang Dynasty Body Paint",
        "subject": "a fine art female model with Tang dynasty Dunhuang mural body paint",
        "body": "graceful model, Tang dynasty beauty ideal, body art canvas",
        "outfit": "full body paint art — Tang dynasty flying apsara and court motifs, Dunhuang cave mural aesthetic, celestial dancer patterns and gold leaf coverage, painted on bare skin",
        "material": "fine art body paint, Tang dynasty mural-style pigments and gold leaf",
        "environment": "Dunhuang cave mural setting, celestial flying figures backdrop, oasis desert light",
        "lighting": "Dunhuang warm desert light, golden cave mural glow, celestial atmosphere",
        "style": "fine art Tang dynasty body paint editorial, Dunhuang heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "harem_bodypaint": {
        "tag": "Harem Body Paint",
        "subject": "a fine art female model with Persian harem miniature painting body paint",
        "body": "graceful sensual model, Persian beauty ideal, body art canvas",
        "outfit": "full body paint art — Persian manuscript miniature painting aesthetic, arabesque and floral scrollwork patterns, lapis and gold body coverage, painted on bare skin",
        "material": "fine art body paint, Persian miniature-style pigments and gold leaf",
        "environment": "Persian palace garden, cypress trees, geometric water channel, tile pavilion",
        "lighting": "warm Persian garden golden light, lapis blue water reflection",
        "style": "fine art Persian harem body paint editorial, Iranian heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "shaman_bodypaint": {
        "tag": "Shaman Body Paint",
        "subject": "a fine art female model with Siberian shaman spirit body paint",
        "body": "athletic powerful model, Siberian shaman spiritual presence, body art canvas",
        "outfit": "full body paint art — shamanic spirit sigil and ritual patterns, ochre and chalk earth pigment aesthetic, petroglyph-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, earth pigment shamanic pattern brushwork",
        "environment": "Siberian taiga forest, fire ceremony, northern sky, reindeer in distance",
        "lighting": "Siberian firelight, northern twilight glow, shamanic spirit atmosphere",
        "style": "fine art Siberian shaman body paint editorial, indigenous heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "dashiki_bodypaint": {
        "tag": "Dashiki Body Paint",
        "subject": "a fine art female model with West African dashiki pattern body paint",
        "body": "vibrant graceful model, West African beauty, body art canvas",
        "outfit": "full body paint art — West African dashiki medallion collar patterns, folk art geometric and floral motifs, vibrant African textile-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, West African folk art pigment brushwork",
        "environment": "West African marketplace, colorful fabric stalls, golden afternoon",
        "lighting": "West African warm afternoon sun, marketplace golden glow, vibrant atmosphere",
        "style": "fine art dashiki body paint editorial, West African cultural heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "dirndl_bodypaint": {
        "tag": "Dirndl Body Paint",
        "subject": "a fine art female model with Bavarian folk pattern body paint",
        "body": "curvaceous cheerful model, Bavarian beauty, body art canvas",
        "outfit": "full body paint art — Bavarian alpine folk art patterns, edelweiss and mountain flower motifs, Germanic folk embroidery-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, Bavarian folk art floral brushwork",
        "environment": "Bavarian alpine meadow, Neuschwanstein Castle backdrop, edelweiss flowers",
        "lighting": "Bavarian alpine golden afternoon, crystal clear mountain air, festive atmosphere",
        "style": "fine art Bavarian folk body paint editorial, Germanic heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "haida_bodypaint": {
        "tag": "Haida Formline Body Paint",
        "subject": "a fine art female model with Haida Pacific Northwest formline body paint",
        "body": "strong graceful model, Pacific Northwest indigenous beauty, body art canvas",
        "outfit": "full body paint art — Haida formline design aesthetic, ovoid and U-form creature motifs, Pacific Northwest indigenous art-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, Haida formline curvilinear brushwork",
        "environment": "British Columbia coastline, ancient red cedar totem poles, Pacific Northwest rainforest",
        "lighting": "Pacific Northwest filtered forest light, cedar wood warm tone",
        "style": "fine art Haida formline body paint editorial, Pacific Northwest indigenous heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "polynesian_bodypaint": {
        "tag": "Polynesian Body Paint",
        "subject": "a fine art female model with Polynesian tapa cloth pattern body paint",
        "body": "athletic graceful model, Polynesian beauty, body art canvas",
        "outfit": "full body paint art — Polynesian tapa kapa cloth geometric patterns, Pacific island tribal motifs, sea creature and wave-inspired body coverage, painted on bare skin",
        "material": "fine art body paint, Polynesian tapa geometric brushwork",
        "environment": "Hawaiian black sand beach, volcanic coastline, Pacific sunset",
        "lighting": "Pacific golden sunset, volcanic sand warm glow, tropical Polynesian atmosphere",
        "style": "fine art Polynesian body paint editorial, Pacific Islander heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
}

# ── 고정형 42종 ────────────────────────────────────────────
FIXED_PRESETS = {
    "geisha_bodypaint": {
        "tag": "Geisha Body Paint",
        "subject": "a fine art female model with full geisha-inspired body paint",
        "body": "slender elegant model, graceful posture, body art canvas",
        "outfit": "body fully painted with: white oshiroi base coat covering entire body, delicate red and black kamon family crest patterns, ukiyo-e style cherry blossom and crane motifs in vermillion and gold, NO clothing, NO fabric, painted on bare skin",
        "material": "fine art body paint — white gofun pigment base, vermillion lacquer patterns, gold leaf accents, ink brushwork details",
        "environment": "Gion Matsuri festival backdrop, paper lanterns, wooden machiya townhouse",
        "lighting": "warm paper lantern glow, golden hour side lighting, soft bokeh background",
        "style": "fine art geisha body paint editorial, ukiyo-e fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "maiko_bodypaint": {
        "tag": "Maiko Body Paint",
        "subject": "a fine art female model with maiko apprentice geisha body paint",
        "body": "youthful slender model, delicate features, body art canvas",
        "outfit": "body fully painted with: cascading weeping willow and sakura petal patterns in soft pink and pale green, red kanzashi hair ornament motifs incorporated into shoulder paint, dense floral coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — soft pink and pale green pigments, delicate brushwork, gold detail accents",
        "environment": "Kyoto bamboo grove, stone lanterns, moss-covered garden path",
        "lighting": "dappled bamboo light, soft diffused daylight, ethereal green ambiance",
        "style": "fine art maiko body paint editorial, Japanese garden photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "kimono_bodypaint": {
        "tag": "Kimono Body Paint",
        "subject": "a fine art female model with traditional kimono pattern body paint",
        "body": "elegant slender model, refined posture, body art canvas",
        "outfit": "body fully painted with: kacho-fugetsu flower-bird-wind-moon motifs — dense chrysanthemum and pine wave patterns, gold foil obi belt stripe painted across torso, indigo and crimson palette covering full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — indigo and crimson pigments, gold foil details, traditional Japanese motif brushwork",
        "environment": "traditional Japanese room, shoji screens, ikebana flower arrangement",
        "lighting": "soft shoji diffused light, warm interior glow, elegant shadow play",
        "style": "fine art kimono body paint editorial, Vogue Japan fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "noh_bodypaint": {
        "tag": "Noh Theater Body Paint",
        "subject": "a fine art female model with Noh theater mask body paint",
        "body": "statuesque model, theatrical presence, body art canvas",
        "outfit": "body fully painted with: Noh men mask face motif extended across chest, gold foil hitatare court robe geometric patterns covering full body, pine and bamboo symbolic motifs in gold and white NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold leaf, white gofun pigment, black sumi ink geometric patterns",
        "environment": "Noh theater stage, hinoki cypress wood floor, pine tree backdrop painting",
        "lighting": "dramatic stage spotlight, warm theatrical amber, deep shadow contrast",
        "style": "fine art Noh theater body paint editorial, Japanese performing arts photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, dramatic fine art photography"
    },
    "kabuki_bodypaint": {
        "tag": "Kabuki Body Paint",
        "subject": "a fine art female model with full kabuki kumadori body paint",
        "body": "dramatic expressive model, theatrical stage presence, body art canvas",
        "outfit": "body fully painted with: kabuki kumadori red and black stripe patterns covering entire body from face to feet — bold radiating red lines on white base across chest shoulders arms legs, intensely dense kumadori coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — vivid red bengara pigment, stark white oshiroi base, black sumi ink stripes, intensely contrasting theatrical patterns",
        "environment": "Kabuki-za theater stage, dramatic red curtain, golden stage props",
        "lighting": "powerful stage spotlight, theatrical high contrast, deep dramatic shadows",
        "style": "fine art kabuki body paint editorial, Japanese theatrical fine art photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, dramatic theater body paint photography"
    },
    "geisha_white_bodypaint": {
        "tag": "Oiran Body Paint",
        "subject": "a fine art female model with oiran courtesan white base and pattern body paint",
        "body": "elegant statuesque model, oiran courtesan beauty, body art canvas",
        "outfit": "body fully painted with: white oshiroi powder base covering entire body as canvas, dense red hana kanzashi flower hair ornament pattern recreation across shoulders and chest, black lacquer karaori brocade pattern in gold outlined arabesque flowers at torso NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — stark white gofun base, red and gold brocade pattern brushwork, lacquer black outline details",
        "environment": "Yoshiwara pleasure quarter lantern-lit street, gold screen backdrop, maple leaves",
        "lighting": "Yoshiwara lantern warm amber glow, gold screen reflection, elegant night atmosphere",
        "style": "fine art oiran body paint editorial, Edo period Japanese heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "hanbok_bodypaint": {
        "tag": "Hanbok Body Paint",
        "subject": "a fine art female model with traditional Korean hanbok pattern body paint",
        "body": "graceful elegant model, refined Korean beauty, body art canvas",
        "outfit": "body fully painted with: hanji paper mulberry texture pattern on jeogori upper body section, flowing chima skirt silhouette painted in obangsaek five cardinal colors — red blue yellow white black — lotus and peony motifs dense coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — obangsaek five cardinal color pigments, lotus and peony motif brushwork, dancheong temple color palette",
        "environment": "Gyeongbokgung palace courtyard, stone balustrade, traditional Korean architecture",
        "lighting": "golden afternoon light, soft palace courtyard glow, elegant heritage atmosphere",
        "style": "fine art hanbok body paint editorial, Korean heritage fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "joseon_bodypaint": {
        "tag": "Joseon Court Body Paint",
        "subject": "a fine art female model with Joseon royal court regalia body paint",
        "body": "regal statuesque model, imperial bearing, body art canvas",
        "outfit": "body fully painted with: royal heolyeong phoenix chest badge pattern expanded across entire torso, gold crown silla-style ornament motifs on shoulders, blue and red royal court color scheme with dense embroidery pattern NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — royal blue and crimson pigments, gold leaf crown motifs, phoenix embroidery pattern",
        "environment": "Gyeongbokgung Geunjeongjeon throne hall, dragon pillars, royal court setting",
        "lighting": "imperial golden hour light, majestic hall illumination, regal shadow depth",
        "style": "fine art Joseon royal body paint editorial, Korean imperial heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, royal fine art body painting photography"
    },
    "gisaeng_bodypaint": {
        "tag": "Gisaeng Body Paint",
        "subject": "a fine art female model with gisaeng court entertainer body paint",
        "body": "graceful artistic model, elegant performance presence, body art canvas",
        "outfit": "body fully painted with: minhwa folk painting style — magpie crane and peony motifs in vivid color, ink brushwork calligraphy strokes as body paint, dancheong red and blue temple patterns dense coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — minhwa vivid pigments, sumi ink calligraphy brushwork, dancheong temple color accents",
        "environment": "moonlit pavilion over water, lotus pond reflection, silk lanterns",
        "lighting": "moonlit water reflection, paper lantern warm glow, romantic night atmosphere",
        "style": "fine art gisaeng body paint editorial, Joseon era artistic photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "korean_shaman_bodypaint": {
        "tag": "Korean Mudang Shaman Body Paint",
        "subject": "a fine art female model with Korean mudang shaman ritual body paint",
        "body": "powerful expressive model, Korean shaman spiritual presence, body art canvas",
        "outfit": "body fully painted with: Korean shaman gut ritual color bands in obangsaek — alternating red white blue black yellow stripes covering full body, samjogo three-legged crow and sun wheel motifs on torso, charm seal bujok talisman patterns NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — obangsaek ritual color pigments, shamanic bujok talisman brushwork",
        "environment": "Korean mountain shrine, ritual altar with offerings, fire ceremony, sacred ropes",
        "lighting": "fire ceremony warm light, mountain shrine sacred atmosphere, spiritual glow",
        "style": "fine art Korean shaman body paint editorial, Korean spiritual heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "qipao_bodypaint": {
        "tag": "Qipao Body Paint",
        "subject": "a fine art female model with Chinese qipao pattern body paint",
        "body": "slender elegant model, Shanghai glamour presence, body art canvas",
        "outfit": "body fully painted with: dense red and gold phoenix and peony embroidery patterns covering entire body on deep black base, qipao mandarin collar line painted at neck, diagonal frog button motifs on torso NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep black lacquer base, vermillion red and gold phoenix motifs, dense silk embroidery pattern recreation",
        "environment": "1930s Shanghai art deco interior, geometric tile floor, ornate carved screens",
        "lighting": "art deco pendant lights, warm amber Shanghai night glow, elegant shadow play",
        "style": "fine art Shanghai qipao body paint editorial, vintage Chinese glamour photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "cheongsam_bodypaint": {
        "tag": "Cheongsam Body Paint",
        "subject": "a fine art female model with cheongsam silk pattern body paint",
        "body": "sleek elegant model, refined Chinese beauty, body art canvas",
        "outfit": "body fully painted with: dense magnolia blossom and gold foil dragon patterns, cobalt blue and jade green color scheme on ivory base covering full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — cobalt blue and jade green pigments, gold foil dragon details, magnolia motif brushwork",
        "environment": "classical Chinese garden, pavilion over water, willow tree reflections",
        "lighting": "soft garden diffused light, jade-green water reflection, serene daylight",
        "style": "fine art cheongsam body paint editorial, classical Chinese garden photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "hanfu_bodypaint": {
        "tag": "Hanfu Body Paint",
        "subject": "a fine art female model with Tang dynasty hanfu cloud pattern body paint",
        "body": "graceful flowing model, classical Chinese beauty, body art canvas",
        "outfit": "body fully painted with: yunwen cloud and crane patterns from Tang dynasty silk, flying apsara celestial dancer motifs, pale blue and gold palette dense coverage full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — pale celestial blue pigments, gold cloud motifs, Tang dynasty silk pattern brushwork",
        "environment": "Tang dynasty palace garden, lotus pond, weeping willow, classical architecture",
        "lighting": "golden afternoon Tang palace light, warm imperial glow, celestial atmosphere",
        "style": "fine art hanfu body paint editorial, Tang dynasty heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "ming_bodypaint": {
        "tag": "Ming Dynasty Body Paint",
        "subject": "a fine art female model with Ming dynasty blue-and-white porcelain body paint",
        "body": "elegant refined model, Ming imperial bearing, body art canvas",
        "outfit": "body fully painted with: qinghua blue-and-white porcelain dragon and phoenix patterns — cobalt blue on stark white base, dense fish scale and lotus scroll patterns covering entire body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — cobalt blue pigment on white gesso base, porcelain-style precision brushwork, Ming dynasty motifs",
        "environment": "Ming dynasty imperial kiln workshop, blue-and-white porcelain vessels, white studio",
        "lighting": "clean white studio light, porcelain-style high key illumination, crisp shadow definition",
        "style": "fine art Ming porcelain body paint editorial, Chinese heritage fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "sari_bodypaint": {
        "tag": "Sari Body Paint",
        "subject": "a fine art female model with Indian sari pattern body paint",
        "body": "graceful curvy model, classical Indian beauty, body art canvas",
        "outfit": "body fully painted with: Banarasi silk brocade peacock and lotus patterns in deep magenta and gold, dense zari gold thread work recreation covering full body, pallu end drape pattern on shoulder NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep magenta and gold pigments, peacock and lotus motif brushwork, zari gold thread pattern recreation",
        "environment": "Indian palace courtyard, pink sandstone columns, marigold garlands",
        "lighting": "warm Rajasthani golden hour, pink palace sandstone glow, festive atmosphere",
        "style": "fine art sari body paint editorial, Indian heritage fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "belly_bodypaint": {
        "tag": "Belly Dance Body Paint",
        "subject": "a fine art female model with belly dancer coin and chain body paint",
        "body": "curvaceous model, sensual dancer physique, body art canvas",
        "outfit": "body fully painted with: golden coin and chain trompe l'oeil patterns across hips and torso, Moorish geometric arabesque patterns in gold and turquoise covering full body, kohl eye motif on navel NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold metallic pigment, turquoise and deep purple accents, arabesque geometric brushwork",
        "environment": "Moroccan riad courtyard, mosaic fountain, carved stucco walls, lanterns",
        "lighting": "warm lantern-lit Moroccan interior, geometric shadow play, golden atmosphere",
        "style": "fine art belly dance body paint editorial, Oriental fusion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "odalisque_bodypaint": {
        "tag": "Odalisque Body Paint",
        "subject": "a fine art female model with Ottoman odalisque Iznik tile body paint",
        "body": "voluptuous graceful model, Ottoman harem beauty, body art canvas",
        "outfit": "body fully painted with: Iznik tile tulip and carnation patterns in cobalt blue and red on white base, arabesque medallion patterns covering entire body dense coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — cobalt blue and Ottoman red on white gesso base, Iznik floral motif precision brushwork",
        "environment": "Topkapi Palace harem chamber, Iznik tile walls, fountain, silk cushions",
        "lighting": "soft Ottoman interior light, azure tile reflection, sensual ambient glow",
        "style": "fine art odalisque body paint editorial, Ottoman heritage fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "mughal_bodypaint": {
        "tag": "Mughal Body Paint",
        "subject": "a fine art female model with Mughal pietra dura floral body paint",
        "body": "elegant graceful model, Mughal court beauty, body art canvas",
        "outfit": "body fully painted with: pietra dura inlay floral patterns in white marble base with colored stone inlay recreation, Taj Mahal arabesque motifs in dense coverage, jade green and lapis blue accent flowers NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — white marble base, jade green and lapis blue inlay recreation, Mughal floral precision brushwork",
        "environment": "Taj Mahal reflecting pool, white marble architecture, garden symmetry",
        "lighting": "Taj Mahal golden sunrise light, marble reflection pool glow, ethereal atmosphere",
        "style": "fine art Mughal body paint editorial, Indian Mughal heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "persian_bodypaint": {
        "tag": "Persian Court Body Paint",
        "subject": "a fine art female model with Persian court geometric and calligraphy body paint",
        "body": "regal elegant model, Persian court bearing, body art canvas",
        "outfit": "body fully painted with: Islamic geometric star polygon patterns in lapis lazuli and cinnabar, Nastaliq calligraphy poetry scrolls across torso and arms, dense Safavid arabesque floral coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — lapis lazuli deep blue, cinnabar red, Safavid arabesque pattern brushwork",
        "environment": "Isfahan Imam Mosque, muqarnas vaulting, blue tile interior, arch reflections",
        "lighting": "Isfahan mosque interior light, blue tile luminescence, spiritual atmosphere",
        "style": "fine art Persian court body paint editorial, Iranian heritage architecture photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "moroccan_bodypaint": {
        "tag": "Moroccan Body Paint",
        "subject": "a fine art female model with Moroccan zellige tile body paint",
        "body": "graceful model, Moroccan beauty, body art canvas",
        "outfit": "body fully painted with: zellige geometric mosaic patterns in cobalt blue and white, dense interlocking star polygon tile patterns covering entire body, arabesque border patterns at limbs NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — cobalt blue on stark white base, zellige mosaic precision pattern brushwork",
        "environment": "Marrakech riad courtyard, blue zellige fountain, carved stucco, terracotta pots",
        "lighting": "Moroccan midday courtyard light, blue zellige reflection, warm terracotta glow",
        "style": "fine art Moroccan body paint editorial, North African heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "ottoman_bodypaint": {
        "tag": "Ottoman Body Paint",
        "subject": "a fine art female model with Ottoman imperial pattern body paint",
        "body": "statuesque model, imperial Ottoman presence, body art canvas",
        "outfit": "body fully painted with: Ottoman imperial tughra calligraphy signature motif expanded across chest, Iznik tulip and saz leaf patterns in dense coverage, imperial red and gold on black base full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — imperial Ottoman red, gold leaf, black lacquer base, Iznik pattern brushwork",
        "environment": "Topkapi Palace throne room, imperial tile walls, stained glass windows",
        "lighting": "Topkapi stained glass colored light, imperial golden glow, majestic atmosphere",
        "style": "fine art Ottoman imperial body paint editorial, Turkish heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "thai_bodypaint": {
        "tag": "Thai Temple Body Paint",
        "subject": "a fine art female model with Thai temple mural and naga body paint",
        "body": "graceful elegant model, Thai classical dancer presence, body art canvas",
        "outfit": "body fully painted with: Wat Pho gold naga serpent scales covering entire body, Buddha's halo mandala pattern on torso, Ramayana epic mural motifs in gold and lacquer red NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold leaf naga scale coverage, lacquer red accent motifs, Thai temple mural style brushwork",
        "environment": "Wat Pho temple interior, golden Buddha statue, intricate mosaic columns",
        "lighting": "temple interior golden glow, incense light shimmer, sacred atmosphere",
        "style": "fine art Thai temple body paint editorial, Theravada Buddhist heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "balinese_bodypaint": {
        "tag": "Balinese Goddess Body Paint",
        "subject": "a fine art female model with Balinese Barong and legong dance body paint",
        "body": "graceful dancer model, Balinese goddess presence, body art canvas",
        "outfit": "body fully painted with: Barong mythical lion face motif centered on chest expanded with gold prada fabric pattern recreation, legong dancer headdress flower motifs on shoulders, tropical hibiscus and frangipani patterns dense coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold prada metallic pigment, Barong red and black accents, tropical floral brushwork",
        "environment": "Bali Pura Besakih temple terrace, stone kala demon gates, tropical palms, incense smoke",
        "lighting": "tropical golden sunset, temple torch glow, sacred Balinese atmosphere",
        "style": "fine art Balinese goddess body paint editorial, Indonesian spiritual heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "kebaya_bodypaint": {
        "tag": "Kebaya Body Paint",
        "subject": "a fine art female model with Javanese batik kebaya pattern body paint",
        "body": "slender elegant model, Javanese refined beauty, body art canvas",
        "outfit": "body fully painted with: traditional batik tulis hand-drawn parang diagonal stripe patterns in deep indigo and cream — wax resist crack texture recreation, mega mendung cloud batik motifs on shoulders, dense interlocking kawung circle patterns covering full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep indigo nila dye tone, cream on dark base, wax-resist crack texture effect, batik motif brushwork",
        "environment": "Yogyakarta Kraton royal palace, traditional Javanese pavilion, batik workshop setting",
        "lighting": "traditional Javanese interior warm light, batik workshop natural light, cultural atmosphere",
        "style": "fine art Javanese batik body paint editorial, Indonesian heritage fashion photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "batik_bodypaint": {
        "tag": "Batik Body Paint",
        "subject": "a fine art female model with Indonesian batik pattern body paint",
        "body": "elegant graceful model, Indonesian beauty, body art canvas",
        "outfit": "body fully painted with: Javanese batik sido mukti prosperity pattern — dense lotus and butterfly motifs in sogan brown and indigo blue on cream, wax resist crackle texture throughout, flora and fauna batik coverage entire body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — sogan dark brown and indigo pigments, cream base, wax resist crackle texture recreation, traditional batik brushwork",
        "environment": "Borobudur Buddhist temple, ancient stone relief carvings, tropical sunrise",
        "lighting": "Borobudur golden sunrise light, ancient stone warm glow, spiritual atmosphere",
        "style": "fine art batik body paint editorial, Javanese Buddhist heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "ikat_bodypaint": {
        "tag": "Ikat Body Paint",
        "subject": "a fine art female model with Central Asian ikat silk pattern body paint",
        "body": "elegant model, Silk Road beauty, body art canvas",
        "outfit": "body fully painted with: Uzbek ikat adras silk diamond and chevron patterns in vivid turquoise and crimson on golden yellow base, resist-dye bleed edge effect throughout, dense geometric coverage full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — turquoise and crimson on golden yellow, ikat bleed-edge resist dye effect, geometric diamond pattern brushwork",
        "environment": "Samarkand Registan courtyard, blue mosaic tilework, Silk Road bazaar setting",
        "lighting": "Central Asian midday sun, blue tile luminescence, Silk Road golden atmosphere",
        "style": "fine art ikat body paint editorial, Central Asian Silk Road heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "ao_dai_bodypaint": {
        "tag": "Ao Dai Body Paint",
        "subject": "a fine art female model with Vietnamese ao dai floral pattern body paint",
        "body": "slender graceful model, Vietnamese beauty, body art canvas",
        "outfit": "body fully painted with: lotus blossom and bamboo stem patterns in soft jade green and pink on white base, traditional Vietnamese chrysanthemum motifs at collar and hem line, dense floral coverage full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — jade green and soft pink pigments, lotus and bamboo motif brushwork, Vietnamese floral pattern",
        "environment": "Hoi An ancient town, yellow heritage buildings, lantern festival, river reflection",
        "lighting": "Hoi An lantern festival warm glow, water reflection, romantic Vietnamese atmosphere",
        "style": "fine art ao dai body paint editorial, Vietnamese heritage fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "tibetan_bodypaint": {
        "tag": "Tibetan Thangka Body Paint",
        "subject": "a fine art female model with Tibetan thangka mandala body paint",
        "body": "serene model, spiritual presence, body art canvas",
        "outfit": "body fully painted with: Kalachakra Wheel of Time mandala centered on torso, lotus petal concentric rings radiating outward, Tibetan Buddhist deity silhouette flame halo patterns covering full body in gold and deep vermillion NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold mineral pigment, deep vermillion and lapis blue, Tibetan thangka mandala precision brushwork",
        "environment": "Potala Palace terrace, Himalayan snow peaks, prayer flag strings, incense smoke",
        "lighting": "high altitude Himalayan golden light, prayer flag color scatter, spiritual atmosphere",
        "style": "fine art Tibetan thangka body paint editorial, Himalayan spiritual heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "scythian_bodypaint": {
        "tag": "Scythian Animal Style Body Paint",
        "subject": "a fine art female model with Scythian gold animal style body paint",
        "body": "athletic warrior model, Eurasian steppe beauty, body art canvas",
        "outfit": "body fully painted with: Scythian toreutics gold animal style — curled panther and stag in dynamic pose tiled across body, knotted animal combat scenes in gold on dark base, Pazyryk carpet border patterns at limbs NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold metallic pigment on black base, Scythian animal style curvilinear brushwork",
        "environment": "Eurasian steppe grassland, kurgan burial mound, golden sky, ancient nomadic setting",
        "lighting": "steppe golden sunset, ancient burial mound dramatic sky, nomadic warrior atmosphere",
        "style": "fine art Scythian body paint editorial, Eurasian nomadic heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "mayan_bodypaint": {
        "tag": "Mayan Body Paint",
        "subject": "a fine art female model with Mayan jade mosaic and jaguar body paint",
        "body": "athletic graceful model, Mayan warrior beauty, body art canvas",
        "outfit": "body fully painted with: jade green mosaic mask fragments tiled across full body, jaguar spot patterns on limbs, Mayan glyphic inscription bands at joints, dense Pakal jade burial mask motif on chest NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — jade green and black pigments, mosaic tile pattern brushwork, jaguar spot texture",
        "environment": "Palenque jungle temple, carved stone glyphs, tropical rainforest mist",
        "lighting": "jungle filtered green light, ancient stone warm glow, mysterious atmosphere",
        "style": "fine art Mayan body paint editorial, Mesoamerican heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "hopi_bodypaint": {
        "tag": "Hopi Kachina Body Paint",
        "subject": "a fine art female model with Hopi kachina doll geometric body paint",
        "body": "athletic graceful model, Native American Pueblo beauty, body art canvas",
        "outfit": "body fully painted with: Hopi kachina doll body paint — geometric stepped pyramid cloud and lightning patterns in turquoise and terracotta, eagle feather motifs on arms, corn stalk sacred symbols on torso NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — turquoise and terracotta pigments, geometric kachina precision brushwork",
        "environment": "Hopi mesa village, sandstone cliff dwelling, Arizona desert canyon landscape",
        "lighting": "Southwestern desert golden hour, red sandstone warm glow, sacred pueblo atmosphere",
        "style": "fine art Hopi kachina body paint editorial, Native American heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "olmec_bodypaint": {
        "tag": "Olmec Body Paint",
        "subject": "a fine art female model with Olmec jaguar deity body paint",
        "body": "strong athletic model, Mesoamerican beauty, body art canvas",
        "outfit": "body fully painted with: Olmec were-jaguar deity face motif expanded chest to full body — jade green and black jaguar transformation patterns, flaming eyebrow and cleft head divine symbol, dense jungle green coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — jade green and deep black pigments, Olmec were-jaguar motif brushwork",
        "environment": "Olmec heartland tropical coast, La Venta basalt colossal head, Gulf of Mexico jungle",
        "lighting": "Gulf Coast tropical golden light, ancient stone warm glow, primordial Mesoamerican atmosphere",
        "style": "fine art Olmec body paint editorial, ancient Mesoamerican heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "maori_bodypaint": {
        "tag": "Maori Ta Moko Body Paint",
        "subject": "a fine art female model with Maori ta moko spiral body paint",
        "body": "strong athletic model, Polynesian warrior beauty, body art canvas",
        "outfit": "body fully painted with: Maori ta moko facial tattoo spiral koru patterns extended across entire body — dense double spiral and pakati notch patterns covering face chest arms legs, deep blue-black puhoro leg pattern coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep blue-black ko pigment, koru spiral precision brushwork, ta moko traditional pattern recreation",
        "environment": "New Zealand coastline, volcanic rock beach, native pohutukawa tree, Pacific Ocean",
        "lighting": "dramatic Pacific coastal light, volcanic rock dark contrast, powerful Maori atmosphere",
        "style": "fine art Maori ta moko body paint editorial, New Zealand indigenous heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "yoruba_bodypaint": {
        "tag": "Yoruba Adire Body Paint",
        "subject": "a fine art female model with Yoruba adire indigo resist-dye body paint",
        "body": "graceful strong model, West African beauty, body art canvas",
        "outfit": "body fully painted with: Yoruba adire eleko starch-resist paste patterns in deep indigo on white — geometric and figurative motifs from Oshun river goddess iconography, cassava paste resist texture recreation, dense indigo coverage full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep indigo on white base, starch-resist texture recreation, Yoruba adire pattern brushwork",
        "environment": "Osun-Osogbo sacred grove, river shrine, tropical forest, ritual space",
        "lighting": "sacred grove dappled light, river shimmer, Yoruba spiritual atmosphere",
        "style": "fine art Yoruba adire body paint editorial, West African heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "kente_bodypaint": {
        "tag": "Kente Body Paint",
        "subject": "a fine art female model with Ghanaian kente cloth pattern body paint",
        "body": "regal strong model, Ghanaian royal beauty, body art canvas",
        "outfit": "body fully painted with: Asante kente cloth woven strip patterns in royal gold green and black — geometric meander and hourglass motifs in dense horizontal and vertical band coverage, adinkra symbol accents integrated NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — royal gold, green and black pigments, kente woven pattern precision brushwork",
        "environment": "Kumasi Asante royal palace, throne room, traditional stool regalia",
        "lighting": "Ghanaian golden afternoon light, royal court warm glow, majestic atmosphere",
        "style": "fine art kente body paint editorial, Ghanaian Asante royal heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "adinkra_bodypaint": {
        "tag": "Adinkra Symbol Body Paint",
        "subject": "a fine art female model with Ghanaian adinkra symbol body paint",
        "body": "regal athletic model, Ghanaian beauty, body art canvas",
        "outfit": "body fully painted with: Adinkra symbols stamped in dense coverage — Gye Nyame supreme being symbol large on chest, Sankofa return-to-roots bird centered, Dwennimmen ram horn strength pattern on shoulders, dense black on ochre background entire body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — black calaba dye on ochre earth base, adinkra stamp pattern precision",
        "environment": "Ghana funeral cloth dyeing setting, traditional calabash stamps, outdoor workspace",
        "lighting": "West African outdoor morning light, natural dye workshop atmosphere, cultural warmth",
        "style": "fine art adinkra body paint editorial, Ghanaian indigenous philosophy photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "zulu_bodypaint": {
        "tag": "Zulu Body Paint",
        "subject": "a fine art female model with Zulu beadwork pattern body paint",
        "body": "strong graceful model, Zulu beauty, body art canvas",
        "outfit": "body fully painted with: Zulu isishunka love letter beadwork patterns — geometric triangle and diamond shapes in white red and black with blue green accent, trompe l'oeil beaded collar and band recreation, dense beadwork pattern coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — white, red and black with blue green accents, Zulu bead pattern precision brushwork",
        "environment": "KwaZulu-Natal grassland, traditional beehive hut, acacia tree savanna",
        "lighting": "South African warm savanna light, golden grass backdrop, cultural atmosphere",
        "style": "fine art Zulu beadwork body paint editorial, South African Zulu heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "scottish_bodypaint": {
        "tag": "Scottish Tartan Body Paint",
        "subject": "a fine art female model with Scottish tartan plaid and Celtic body paint",
        "body": "athletic model, Scottish Highland beauty, body art canvas",
        "outfit": "body fully painted with: Royal Stewart tartan plaid crossing grid pattern in vivid red green navy and yellow covering full body, Pictish beast spiral at shoulder, Celtic thistle motif on torso NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — vivid tartan red, green and navy, woven plaid grid precision brushwork",
        "environment": "Scottish Highland moorland, misty glen, ruined castle, purple heather fields",
        "lighting": "Scottish Highland dramatic overcast light, moody mist atmosphere, ancient landscape",
        "style": "fine art Scottish tartan body paint editorial, Highland heritage photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "byzantine_bodypaint": {
        "tag": "Byzantine Mosaic Body Paint",
        "subject": "a fine art female model with Byzantine gold mosaic tesserae body paint",
        "body": "regal statuesque model, Byzantine empress presence, body art canvas",
        "outfit": "body fully painted with: Byzantine gold glass tesserae mosaic pattern covering entire body — Christ Pantocrator halo nimbus pattern on chest, imperial purple loros sash painted diagonally, mosaic tile grout lines throughout dense gold coverage NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — gold leaf tesserae recreation, imperial purple accents, Byzantine mosaic grid line brushwork",
        "environment": "Hagia Sophia interior, Byzantine gold mosaic apse, candlelit sacred space",
        "lighting": "Byzantine candlelight, gold mosaic luminescence, sacred spiritual atmosphere",
        "style": "fine art Byzantine mosaic body paint editorial, Eastern Roman heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "flamenco_bodypaint": {
        "tag": "Flamenco Body Paint",
        "subject": "a fine art female model with Spanish flamenco carnation and mantilla body paint",
        "body": "dramatic curvaceous model, Andalusian flamenco dancer presence, body art canvas",
        "outfit": "body fully painted with: mantilla lace veil pattern across shoulders and face, carnation and rose dense floral coverage in deep red and black, polka dot lunares pattern recreation with ruffled flounce silhouette lines painted NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — deep red and black pigments, lace pattern precision brushwork, carnation and polka dot motifs",
        "environment": "Sevilla flamenco tablao stage, Moorish arched interior, red carnations, dark ambiance",
        "lighting": "dramatic flamenco stage spotlight, deep shadow contrast, passionate Andalusian atmosphere",
        "style": "fine art flamenco body paint editorial, Andalusian heritage fashion photography",
        "quality": "shot on Canon EOS R5, ultra-sharp 8K, fine art body painting photography"
    },
    "sumerian_bodypaint": {
        "tag": "Sumerian Body Paint",
        "subject": "a fine art female model with Sumerian cuneiform and lapis lazuli body paint",
        "body": "regal statuesque model, Mesopotamian goddess presence, body art canvas",
        "outfit": "body fully painted with: cuneiform wedge script inscription bands covering torso and limbs, lapis lazuli blue and gold Sumerian deity star rosette patterns, Ishtar Gate bull and dragon motifs in bright cobalt blue on white base NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — lapis lazuli blue and gold on white base, cuneiform precision wedge brushwork",
        "environment": "ancient Mesopotamian ziggurat temple, Ishtar Gate replica, Euphrates river at dusk",
        "lighting": "Mesopotamian sunset, ancient brick warm glow, sacred ziggurat atmosphere",
        "style": "fine art Sumerian body paint editorial, ancient Mesopotamian heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
    "voodoo_bodypaint": {
        "tag": "Voodoo Veve Body Paint",
        "subject": "a fine art female model with Haitian Vodou veve symbol body paint",
        "body": "powerful mysterious model, Caribbean spiritual beauty, body art canvas",
        "outfit": "body fully painted with: Erzulie Freda love goddess veve heart and mirror symbol centered on chest, Baron Samedi skull and cross cemetery veve on shoulders, dense white on black veve symbol coverage full body NO clothing NO fabric, painted on bare skin",
        "material": "fine art body paint — white cornmeal ash tones on deep black base, veve symbol precision ritual brushwork",
        "environment": "Haitian peristyle ceremony space, ritual drums, candles and offerings, purple and black altar",
        "lighting": "ceremony candlelight, purple ritual glow, Vodou spiritual atmosphere",
        "style": "fine art Vodou veve body paint editorial, Caribbean spiritual heritage photography",
        "quality": "shot on Hasselblad H6D, ultra-sharp 8K, fine art body painting photography"
    },
}

ALL_PRESETS = {**FIXED_PRESETS, **OPEN_PRESETS}

# ── dashboard.py 앵커 ──────────────────────────────────────
DASHBOARD_ANCHOR = '        # 2026-06-08 카테고리 누락 복구\n        "banksy_stencil","shadow_art_nude",'
DASHBOARD_INSERT = '''        # 2026-06-08 카테고리 누락 복구
        "banksy_stencil","shadow_art_nude",
        # v28 — 전통&문화 바디페인팅 52종 (중복 9종 제거)
        # 일본
        "geisha_bodypaint","maiko_bodypaint","kimono_bodypaint","noh_bodypaint",
        "kabuki_bodypaint","samurai_bodypaint","geisha_white_bodypaint","ninja_bodypaint",
        # 한국
        "hanbok_bodypaint","joseon_bodypaint","gisaeng_bodypaint",
        "hanbok_modern_bodypaint","korean_shaman_bodypaint",
        # 중국
        "qipao_bodypaint","cheongsam_bodypaint","hanfu_bodypaint",
        "tang_dynasty_bodypaint","ming_bodypaint",
        # 남아시아/중동
        "sari_bodypaint","belly_bodypaint","odalisque_bodypaint",
        "harem_bodypaint","mughal_bodypaint",
        "persian_bodypaint","moroccan_bodypaint","ottoman_bodypaint",
        # 동남아/중앙아
        "thai_bodypaint","balinese_bodypaint","kebaya_bodypaint",
        "batik_bodypaint","ikat_bodypaint","ao_dai_bodypaint",
        "tibetan_bodypaint","shaman_bodypaint","scythian_bodypaint",
        # 아메리카/오세아니아
        "mayan_bodypaint","hopi_bodypaint","olmec_bodypaint",
        "maori_bodypaint","polynesian_bodypaint","haida_bodypaint",
        # 아프리카
        "yoruba_bodypaint","kente_bodypaint","dashiki_bodypaint",
        "adinkra_bodypaint","zulu_bodypaint",
        # 유럽/고대
        "scottish_bodypaint","byzantine_bodypaint","flamenco_bodypaint","dirndl_bodypaint",
        "sumerian_bodypaint","voodoo_bodypaint",'''


def create_preset_files():
    """presets/ 폴더에 개별 JSON 파일 생성"""
    if not PRESET_DIR.exists():
        print(f"❌ presets 폴더 없음: {PRESET_DIR}")
        return 0

    created = 0
    skipped = 0
    for name, data in ALL_PRESETS.items():
        fpath = PRESET_DIR / f"{name}.json"
        if fpath.exists():
            skipped += 1
            continue
        with open(fpath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        created += 1

    print(f"✅ presets/ 파일 생성: {created}개 (스킵: {skipped}개)")
    return created


def patch_dashboard():
    """dashboard.py PRESET_CATEGORIES에 52종 key 목록 추가"""
    if not DASHBOARD_FILE.exists():
        print(f"❌ dashboard.py 없음")
        return False

    with open(DASHBOARD_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    if "geisha_bodypaint" in content:
        print("⚠️  dashboard.py 이미 패치됨")
        return False

    if DASHBOARD_ANCHOR not in content:
        print("❌ 앵커 없음 — dashboard.py 수동 확인 필요")
        return False

    new_content = content.replace(DASHBOARD_ANCHOR, DASHBOARD_INSERT)
    with open(DASHBOARD_FILE, "w", encoding="utf-8") as f:
        f.write(new_content)

    print("✅ dashboard.py PRESET_CATEGORIES 패치 완료")
    return True


def verify():
    print("\n── 검증 ──────────────────────────────")
    spot = ["geisha_bodypaint","kabuki_bodypaint","tibetan_bodypaint",
            "byzantine_bodypaint","voodoo_bodypaint","haida_bodypaint",
            "joseon_bodypaint","ming_bodypaint","flamenco_bodypaint"]

    # 파일 존재 확인
    missing = [k for k in spot if not (PRESET_DIR / f"{k}.json").exists()]
    found = len(spot) - len(missing)
    print(f"presets/ 파일: {found}/{len(spot)}개 확인")
    if missing:
        for m in missing:
            print(f"  ❌ {m}.json")

    # dashboard 확인
    if DASHBOARD_FILE.exists():
        with open(DASHBOARD_FILE, "r", encoding="utf-8") as f:
            content = f.read()
        for k in ["geisha_bodypaint", "kabuki_bodypaint", "voodoo_bodypaint"]:
            print(f"  {'✅' if k in content else '❌'} dashboard: {k}")


if __name__ == "__main__":
    print("=" * 55)
    print("  LumineX v28 — 전통&문화 바디페인팅 52종 패치")
    print(f"  고정형 42종 / 개방형 10종")
    print("=" * 55)

    n = create_preset_files()
    ok = patch_dashboard()
    verify()

    if n > 0 or ok:
        print("\n🎉 완료! 다음 단계:")
        print('   Select-String "geisha_bodypaint" presets\\geisha_bodypaint.json')
        print('   Select-String "kabuki_bodypaint" dashboard.py')
        print("   git add -A ; git commit -m 'feat: 전통문화 바디페인팅 52종 추가 (v28)'")
        print("\n📋 SSS 후보 테스트 순서:")
        print("   kabuki → joseon → tibetan → byzantine → mayan → sari")
