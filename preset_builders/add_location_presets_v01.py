# city: 3개
# surreal: 2개
# 합계: 21개


import json, shutil
from pathlib import Path

PRESETS_DIR = Path(r"C:\Dev\LumineX\presets")

# ---- nature ----
path = PRESETS_DIR / "son_doong_jungle.json"
path.write_text(json.dumps({"tag": "Son Doong Jungle", "subject": "a woman standing in the world's largest cave", "body": "full body shot", "outfit": "minimal flowing fabric, natural movement", "material": "sheer lightweight fabric", "environment": "Hang Son Doong cave, Vietnam, massive cave chamber with internal jungle, rays of light piercing through ceiling collapse, misty atmosphere, underground river, ancient stalactites, lush tropical vegetation inside cave, ethereal fog", "lighting": "dramatic god rays from ceiling opening, soft diffused jungle light, misty golden atmosphere", "style": "editorial nature photography, National Geographic, otherworldly", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "son_doong_jungle.json")

path = PRESETS_DIR / "waitomo_glow.json"
path.write_text(json.dumps({"tag": "Waitomo Glow", "subject": "a woman in a glowworm cave", "body": "full body shot", "outfit": "minimal dark flowing fabric", "material": "sheer dark fabric", "environment": "Waitomo glowworm caves, New Zealand, thousands of bioluminescent glowworms covering cave ceiling like a galaxy, dark underground river, starfield reflection on black water, absolute darkness except glowing ceiling", "lighting": "bioluminescent blue-green glow from above, galaxy-like ceiling light, deep shadows, ethereal underwater reflection", "style": "bioluminescent nature editorial, magical realism photography", "quality": "shot on Sony A7R V, long exposure, ultra-sharp, 8K, stunning"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "waitomo_glow.json")

path = PRESETS_DIR / "dead_vlei_ghost.json"
path.write_text(json.dumps({"tag": "Dead Vlei Ghost", "subject": "a woman among ancient dead trees in white desert", "body": "full body shot", "outfit": "minimal light flowing fabric, wind movement", "material": "sheer white fabric", "environment": "Dead Vlei, Namibia, white clay pan surrounded by towering burnt orange sand dunes, blackened dead camel thorn trees 900 years old, blinding white salt flat ground, surreal desolate landscape, cloudless deep blue sky", "lighting": "harsh overhead desert sun, extreme contrast, stark shadows from dead trees, bleached white ground reflection", "style": "surreal desert editorial, fine art nature photography, minimalist", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "dead_vlei_ghost.json")

path = PRESETS_DIR / "danxia_rainbow.json"
path.write_text(json.dumps({"tag": "Danxia Rainbow", "subject": "a woman on rainbow-colored rock formations", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "lightweight fabric", "environment": "Zhangye Danxia Landform, China, undulating rock formations in layers of vivid red, orange, yellow, green, teal and purple, rippling color bands across hillsides, dramatic cloud shadows, vast surreal landscape", "lighting": "golden hour light enhancing rock colors, dramatic cloud-filtered sunlight, vivid saturated natural colors", "style": "geological wonder editorial, vivid nature photography, surreal landscape", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "danxia_rainbow.json")

path = PRESETS_DIR / "cenote_sacred.json"
path.write_text(json.dumps({"tag": "Cenote Sacred", "subject": "a woman in a sacred Maya cenote", "body": "full body shot", "outfit": "minimal wet fabric, natural flowing", "material": "sheer wet fabric", "environment": "Cenote Ik Kil, Mexico, circular natural pool open to sky, hanging vines cascading from circular limestone opening above, crystal clear turquoise water, dappled sunlight through vines, ancient Mayan sacred atmosphere, lush green foliage around rim", "lighting": "shaft of sunlight through circular opening, turquoise water reflection, dappled jungle light, sacred golden glow", "style": "sacred nature editorial, mystical underwater photography", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "cenote_sacred.json")

path = PRESETS_DIR / "socotra_alien.json"
path.write_text(json.dumps({"tag": "Socotra Alien", "subject": "a woman among alien dragon blood trees", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "lightweight fabric", "environment": "Socotra Island, Yemen, dragon blood trees with umbrella-shaped canopies creating alien forest, crimson red sap, surreal otherworldly landscape, misty mountains, endemic plants found nowhere else on earth, ancient alien atmosphere", "lighting": "diffused misty light through dragon tree canopy, ethereal fog, otherworldly atmosphere", "style": "alien world editorial, surreal nature photography, sci-fi landscape", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "socotra_alien.json")

path = PRESETS_DIR / "lake_natron.json"
path.write_text(json.dumps({"tag": "Lake Natron", "subject": "a woman at the edge of a crimson alkaline lake", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer fabric", "environment": "Lake Natron, Tanzania, deep crimson red alkaline lake surface, thousands of flamingos in pink clouds, salt crusted shoreline with mineral patterns, steam rising from hot springs, Mount Ol Doinyo Lengai volcano in background, apocalyptic beauty", "lighting": "harsh equatorial sun, blood red water reflection, dramatic volcanic sky", "style": "extreme nature editorial, apocalyptic beauty photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "lake_natron.json")

path = PRESETS_DIR / "namib_star_desert.json"
path.write_text(json.dumps({"tag": "Namib Star Desert", "subject": "a woman under infinite stars in Namib desert", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer fabric", "environment": "Namib Desert, Namibia, world's oldest desert, towering red sand dunes silhouetted against Milky Way, infinite star field, zero light pollution, ancient desert silence, perfect arc of galaxy overhead", "lighting": "Milky Way starlight, subtle moonlight on dune ridges, deep darkness, star reflection", "style": "astrophotography editorial, night desert fine art photography", "quality": "shot on Sony A7R V, long exposure, ultra-sharp, 8K, stunning"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "namib_star_desert.json")

# ---- heritage ----
path = PRESETS_DIR / "petra_rose.json"
path.write_text(json.dumps({"tag": "Petra Rose", "subject": "a woman in the rose-red ancient city of Petra", "body": "full body shot", "outfit": "minimal flowing fabric, desert wind movement", "material": "sheer lightweight fabric", "environment": "Petra, Jordan, Al-Khazneh Treasury carved into rose-red sandstone cliff, narrow Siq canyon passage, warm amber rock walls with natural color variations, ancient Nabataean carvings, desert atmosphere, golden sand floor", "lighting": "warm desert sunlight on rose sandstone, golden canyon glow, dramatic rock face shadows", "style": "ancient world editorial, archaeological wonder photography, Lawrence of Arabia aesthetic", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "petra_rose.json")

path = PRESETS_DIR / "angkor_dawn.json"
path.write_text(json.dumps({"tag": "Angkor Dawn", "subject": "a woman at the ancient jungle temple of Angkor", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer lightweight fabric", "environment": "Angkor Wat, Cambodia, ancient Khmer temple towers reflected in still lotus pond, jungle trees reclaiming stone walls, morning mist, golden sunrise light, moss-covered stone carvings, sacred ancient atmosphere", "lighting": "golden sunrise reflection on temple pond, misty morning light, warm amber glow through jungle canopy", "style": "ancient civilization editorial, mystical archaeology photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "angkor_dawn.json")

path = PRESETS_DIR / "tikal_skyrise.json"
path.write_text(json.dumps({"tag": "Tikal Skyrise", "subject": "a woman atop a Maya pyramid above the jungle", "body": "full body shot", "outfit": "minimal flowing fabric, wind movement", "material": "sheer lightweight fabric", "environment": "Tikal Temple IV, Guatemala, standing above jungle canopy on Maya pyramid summit, endless green rainforest stretching to horizon, other pyramid tops emerging from mist, howler monkeys in distance, dawn atmosphere, ancient Maya civilization", "lighting": "dramatic sunrise above cloud layer, warm golden light on pyramid stone, misty jungle atmosphere below", "style": "lost civilization editorial, above-the-clouds photography, ancient power", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "tikal_skyrise.json")

path = PRESETS_DIR / "bagan_balloon.json"
path.write_text(json.dumps({"tag": "Bagan Balloon", "subject": "a woman among thousands of ancient temples at dawn", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer lightweight fabric", "environment": "Bagan, Myanmar, plain stretching to horizon filled with over 2000 ancient Buddhist temples and pagodas, hot air balloons floating at dawn, golden morning mist, ancient pagoda silhouettes, spiritual atmosphere", "lighting": "golden hour dawn light, warm mist filtering sunlight, balloon glow, spiritual amber atmosphere", "style": "spiritual wonder editorial, ancient civilization photography", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "bagan_balloon.json")

path = PRESETS_DIR / "ellora_rock_temple.json"
path.write_text(json.dumps({"tag": "Ellora Rock Temple", "subject": "a woman inside a temple carved from solid rock", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer lightweight fabric", "environment": "Ellora Caves, India, Kailasa Temple carved entirely from single basalt cliff, intricate Hindu sculptures covering every surface, massive courtyard hewn from rock, ancient craftsmanship beyond imagination, dramatic scale", "lighting": "dramatic sunlight into carved rock courtyard, deep shadow details, ancient stone warmth", "style": "ancient wonder editorial, architectural archaeology photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "ellora_rock_temple.json")

path = PRESETS_DIR / "derinkuyu_underground.json"
path.write_text(json.dumps({"tag": "Derinkuyu Underground", "subject": "a woman in an ancient underground city", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer fabric", "environment": "Derinkuyu underground city, Cappadocia Turkey, ancient carved stone tunnels and chambers 8 levels deep, narrow passages with circular stone doors, candlelit alcoves, ancient city hewn from volcanic tuff rock, mysterious labyrinthine atmosphere", "lighting": "torch and candlelight, dramatic shadow play on carved stone walls, mysterious underground glow", "style": "underground civilization editorial, mysterious archaeology photography", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "derinkuyu_underground.json")

path = PRESETS_DIR / "tigers_nest_cliff.json"
path.write_text(json.dumps({"tag": "Tigers Nest Cliff", "subject": "a woman at the cliff monastery of Tiger's Nest", "body": "full body shot", "outfit": "minimal flowing fabric, mountain wind", "material": "sheer lightweight fabric", "environment": "Paro Taktsang Tiger's Nest monastery, Bhutan, ancient Buddhist monastery clinging to sheer 900m cliff face, prayer flags streaming in wind, Himalayan mountain backdrop, pine forest below, clouds at eye level, sacred spiritual atmosphere", "lighting": "Himalayan golden light, dramatic cliff shadows, prayer flag colors, misty mountain atmosphere", "style": "spiritual mountain editorial, sacred place photography, Himalayan aesthetic", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "tigers_nest_cliff.json")

path = PRESETS_DIR / "naoshima_art_island.json"
path.write_text(json.dumps({"tag": "Naoshima Art Island", "subject": "a woman on the art island of Naoshima", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer lightweight fabric", "environment": "Naoshima Island, Japan, Yayoi Kusama yellow pumpkin sculpture on sea pier, Seto Inland Sea, minimalist Japanese architecture, outdoor art installations, serene island atmosphere, perfect blue water", "lighting": "soft Japanese coastal light, golden hour sea reflection, minimal clean shadows", "style": "contemporary art island editorial, Japanese minimalist photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "naoshima_art_island.json")

# ---- city ----
path = PRESETS_DIR / "sheikh_zayed_dawn.json"
path.write_text(json.dumps({"tag": "Sheikh Zayed Dawn", "subject": "a woman at the Grand Mosque of Abu Dhabi", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer white fabric", "environment": "Sheikh Zayed Grand Mosque, Abu Dhabi, pristine white marble columns and domes, perfect reflection pool at pre-dawn, 82 domes and 1000 columns, intricate floral mosaic floor, serene spiritual atmosphere, still water mirror reflection", "lighting": "pre-dawn blue hour, warm interior mosque lighting reflecting on water, spiritual glow, perfect symmetry", "style": "architectural wonder editorial, Islamic art photography, serene luxury", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "sheikh_zayed_dawn.json")

path = PRESETS_DIR / "livraria_lello_staircase.json"
path.write_text(json.dumps({"tag": "Livraria Lello Staircase", "subject": "a woman on the iconic red staircase of Livraria Lello", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer lightweight fabric", "environment": "Livraria Lello bookstore, Porto Portugal, famous crimson red Art Nouveau double staircase, ornate carved wood details, stained glass ceiling flooding warm colored light, floor-to-ceiling bookshelves, gothic fairy tale interior", "lighting": "warm stained glass colored light from ceiling, dramatic staircase shadows, rich amber and crimson tones", "style": "architectural fantasy editorial, Art Nouveau interior photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "livraria_lello_staircase.json")

path = PRESETS_DIR / "palacio_de_sal.json"
path.write_text(json.dumps({"tag": "Palacio de Sal", "subject": "a woman in a hotel built entirely of salt", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer white fabric", "environment": "Palacio de Sal hotel, Uyuni Bolivia, walls floors and furniture all constructed from salt blocks, ethereal white crystalline interior, salt brick texture everywhere, surreal all-white environment, Uyuni salt flat visible through windows", "lighting": "soft diffused light through salt walls, crystalline white reflection, ethereal glow, pure white atmosphere", "style": "surreal architecture editorial, crystalline white photography", "quality": "shot on Hasselblad H6D, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "palacio_de_sal.json")

# ---- surreal ----
path = PRESETS_DIR / "richat_eye.json"
path.write_text(json.dumps({"tag": "Richat Eye", "subject": "a woman at the Eye of the Sahara", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer fabric", "environment": "Richat Structure, Mauritania, ancient eroded geological dome forming perfect concentric circles in Sahara desert, visible from space, ancient ring formations stretching to horizon, desert rocks and sand, alien precision geometry", "lighting": "harsh Saharan sun, dramatic shadow in concentric rock rings, ancient geological light", "style": "geological mystery editorial, alien precision photography, Sahara wonder", "quality": "shot on Sony A7R V, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "richat_eye.json")

path = PRESETS_DIR / "marble_caves_water.json"
path.write_text(json.dumps({"tag": "Marble Caves Water", "subject": "a woman in the marble cathedral caves", "body": "full body shot", "outfit": "minimal flowing fabric", "material": "sheer fabric", "environment": "Marble Caves, Patagonia Chile, smooth marble walls swirled with white grey and blue patterns, turquoise glacial water reflecting cave ceiling, boat-accessible water cave, stunning natural marble sculpture, cathedral-like chambers", "lighting": "turquoise water reflection dancing on marble walls, ethereal blue-white light, natural marble cathedral glow", "style": "natural wonder editorial, marble cathedral photography", "quality": "shot on Canon EOS R5, ultra-sharp, 8K, stunning, realistic proportions"}, indent=2, ensure_ascii=False), encoding="utf-8")
print("저장:", "marble_caves_water.json")

print("\n✅ 완료!")
