import json

vs_files = ["barely_there","cruise_hostess","crystal_goddess","new_year_countdown","pool_goddess","red_carpet","showgirl"]
slim_files = ["long_legs_focus"]

for f in vs_files:
    path = f"C:/Dev/LumineX/presets/{f}.json"
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    data["body"] = "Victoria's Secret Angel - perfect VS glamour physique"
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"OK {f}")

for f in slim_files:
    path = f"C:/Dev/LumineX/presets/{f}.json"
    with open(path, "r", encoding="utf-8") as fp:
        data = json.load(fp)
    data["body"] = "super slim runway model physique"
    with open(path, "w", encoding="utf-8") as fp:
        json.dump(data, fp, ensure_ascii=False, indent=2)
    print(f"OK {f}")
