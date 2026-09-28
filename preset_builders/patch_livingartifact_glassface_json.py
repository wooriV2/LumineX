# -*- coding: utf-8 -*-
"""
Living Artifact · Glass Face 계열 등록 (JSON 생성)
- 입력 : preset_builders/la_glassface_bundle.json  (128개: key/title/category/platform/aspect_ratio/prompt)
- 출력 : presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
- 카테고리 5종
    🏺 Living Artifact · Glass Face 3-Split   (77)
    🏺 Living Artifact · Real Face Piercing   (23)
    🏺 Living Artifact · Vessel Body          (3)
    🏺 Living Artifact · Duo Statue           (4)
    🏺 Living Artifact · Glass Face Scene     (21)
- 옵션 : --force (기존 파일 덮어쓰기), --md review.md (검토용 md 생성)
- 이 스크립트 실행 후 patch_livingartifact_2_meta.py 로 카테고리를 PRESET_CATEGORIES 에 반영한다.
"""
import json, os, re, argparse, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PRESETS = os.path.join(ROOT, "presets")
BUNDLE = os.path.join(HERE, "la_glassface_bundle.json")

REQUIRED = ("key", "title", "category", "platform", "aspect_ratio", "prompt")

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()

    with open(BUNDLE, encoding="utf-8-sig") as f:
        items = json.load(f)

    # ---- 검증 ----
    keys = [x["key"] for x in items]
    assert len(keys) == len(set(keys)), "duplicate keys"
    for x in items:
        for r in REQUIRED:
            assert r in x and x[r], (x.get("key"), r)
        assert x["key"].startswith("la_"), x["key"]
        assert not re.search(r"[\uac00-\ud7a3]", x["prompt"]), f"korean in prompt: {x['key']}"
        assert x["aspect_ratio"] in ("2:3", "3:4", "4:5", "3:2"), x["key"]

    os.makedirs(PRESETS, exist_ok=True)
    made = skipped = 0
    md = []
    for x in items:
        data = {"title": x["title"], "category": x["category"], "platform": x["platform"],
                "aspect_ratio": x["aspect_ratio"], "prompt": x["prompt"]}
        path = os.path.join(PRESETS, x["key"] + ".json")
        md.append(f"## {x['title']}\n`{x['key']}` · {x['aspect_ratio']}\n\n```\n{x['prompt']}\n```\n")
        if os.path.exists(path) and not a.force:
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1

    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Living Artifact · Glass Face 계열 검토\n\n" + "\n".join(md))

    c = Counter(x["category"] for x in items)
    print(f"[OK] created {made}, skipped {skipped} (existing), total {len(items)}")
    for k, v in c.items():
        print(f"  {v:3d}  {k}")

if __name__ == "__main__":
    main()
