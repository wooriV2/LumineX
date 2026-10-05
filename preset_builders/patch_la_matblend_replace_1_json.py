# -*- coding: utf-8 -*-
r"""
la_matblend_replace_134_bundle.json (134개) -> 등록된 la_matblend{3|4}_{solo|duo|trio}_* 중 꽃·수정·촛농이 들어간 프리셋만 덮어쓰기.
새 프리셋은 꽃·수정·촛농·팔 올린 자세를 뺐고, UV네온은 이미지당 1명 이하이며 문장부호 오타를 고쳤습니다.
꽃·수정·촛농이 없는 나머지 46개는 그대로 둡니다. 키와 카테고리가 같으므로 메타 등록은 필요 없습니다.
사용법: python preset_builders\patch_la_matblend_replace_1_json.py
"""
import json
import os

BUNDLE_PATH = os.path.join(os.path.dirname(__file__), "la_matblend_replace_134_bundle.json")
PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    with open(BUNDLE_PATH, "r", encoding="utf-8") as f:
        presets = json.load(f)
    os.makedirs(PRESETS_DIR, exist_ok=True)
    existing = [it["key"] for it in presets if os.path.exists(os.path.join(PRESETS_DIR, it["key"] + ".json"))]
    if existing:
        print(f"주의: 이미 있던 키 {len(existing)}개를 덮어씁니다 (예: {existing[0]})")
    written, by_cat = 0, {}
    for item in presets:
        out = {k: item[k] for k in ("key", "category", "title", "prompt", "meta")}
        with open(os.path.join(PRESETS_DIR, f"{item['key']}.json"), "w", encoding="utf-8") as f2:
            json.dump(out, f2, ensure_ascii=False, indent=2)
        written += 1
        by_cat[item["category"]] = by_cat.get(item["category"], 0) + 1
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for c, cnt in by_cat.items():
        print(f"  {c}: {cnt}개")

if __name__ == "__main__":
    main()
