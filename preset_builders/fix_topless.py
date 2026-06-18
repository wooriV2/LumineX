import json

path = "C:/Dev/LumineX/presets/topless_editorial.json"
with open(path, "r", encoding="utf-8") as f:
    data = json.load(f)

data["subject"] = "a stunning high fashion editorial female model"
data["body"] = "slim elegant figure, natural bare skin, artistic editorial presence"
data["outfit"] = "bare upper body, high fashion editorial styling, minimal lower coverage, artistic nude fashion"
data["material"] = "bare skin as canvas, minimal fabric lower garment, high art fashion context"
data["environment"] = "luxury minimal art studio, white seamless backdrop, high fashion editorial space"
data["lighting"] = "dramatic Helmut Newton editorial light, strong shadow play, artistic body sculpting light"
data["style"] = "Helmut Newton bare editorial, high art fashion photography, artistic figure study"
data["quality"] = "shot on Hasselblad H6D, black and white editorial grade, portrait 2:3 vertical"

with open(path, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("OK topless_editorial rewritten")
