# -*- coding: utf-8 -*-
"""
Glass Face 계열 제목 정리 (키는 그대로, title만 수정)
- Real Face 갸루 7개: 'PP3' 같은 오타를 'P3'으로 (이전 단계 체계 P3·P5·P9·P18·P50·P100·P150 표기, 신 체계와 구분)
- 가슴/허리 피어싱 K1·K2: 'K1' -> 'P50 + C1', 'K2' -> 'P100 + C2' (참 축 표기로 통일)
- 대상: presets/la_*.json 과 preset_builders/la_glassface_bundle.json
"""
import json, os, re, glob

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRESETS = os.path.join(ROOT, "presets")
BUNDLE = os.path.join(HERE, "la_glassface_bundle.json")

def fix_title(key, title):
    if key.startswith("la_realface_gyaru_pp"):
        return title.replace(" PP", " P", 1)
    if key in ("la_glassface_bustp_k1", "la_glassface_waistp_k1"):
        return title.replace("피어싱 K1", "피어싱 P50 + C1", 1)
    if key in ("la_glassface_bustp_k2", "la_glassface_waistp_k2"):
        return title.replace("피어싱 K2", "피어싱 P100 + C2", 1)
    return title

changed = 0
for path in sorted(glob.glob(os.path.join(PRESETS, "la_*.json"))):
    key = os.path.basename(path)[:-5]
    with open(path, encoding="utf-8-sig") as f:
        d = json.load(f)
    new = fix_title(key, d["title"])
    if new != d["title"]:
        d["title"] = new
        with open(path, "w", encoding="utf-8") as f:
            json.dump(d, f, ensure_ascii=False, indent=2)
        changed += 1
        print("[FIX]", key, "->", new)

with open(BUNDLE, encoding="utf-8-sig") as f:
    items = json.load(f)
bchanged = 0
for x in items:
    new = fix_title(x["key"], x["title"])
    if new != x["title"]:
        x["title"] = new
        bchanged += 1
with open(BUNDLE, "w", encoding="utf-8") as f:
    json.dump(items, f, ensure_ascii=False, indent=1)

print(f"[OK] preset titles fixed: {changed}, bundle titles fixed: {bchanged}")
assert changed == 11 and bchanged == 11, "expected 11 titles (7 gyaru + 4 K)"
