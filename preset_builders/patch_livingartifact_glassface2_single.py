# -*- coding: utf-8 -*-
"""
Living Artifact - Glass Face family, batch 2 (single-file, no external data file needed)
 - hip piercing transparent 7, hip real body 7, hip pregnant 4, waist new bodies 4 = 22 presets
 - writes presets/{key}.json  (title, category, platform, aspect_ratio, prompt)
 - options: --force (overwrite existing), --md review.md
 - after this, run patch_livingartifact_2_meta.py
"""
import json, os, re, base64, zlib, argparse
from collections import Counter

DATA_B64 = (
    "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"
)

REQUIRED = ("key", "title", "category", "platform", "aspect_ratio", "prompt")

def find_root():
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.dirname(here)
    if os.path.isdir(os.path.join(root, "presets")) or os.path.isdir(os.path.join(root, "core")):
        return root
    return os.getcwd()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--md", default=None)
    a = ap.parse_args()

    items = json.loads(zlib.decompress(base64.b64decode("".join(DATA_B64.split()))).decode("utf-8"))
    keys = [x["key"] for x in items]
    assert len(items) == 22 and len(keys) == len(set(keys)), "bundle integrity check failed"
    for x in items:
        for r in REQUIRED:
            assert r in x and x[r], (x.get("key"), r)
        assert x["key"].startswith("la_"), x["key"]
        assert not re.search(r"[\uac00-\ud7a3]", x["prompt"]), "korean in prompt: " + x["key"]

    presets = os.path.join(find_root(), "presets")
    os.makedirs(presets, exist_ok=True)
    made = skipped = 0
    md = []
    for x in items:
        data = {"title": x["title"], "category": x["category"], "platform": x["platform"],
                "aspect_ratio": x["aspect_ratio"], "prompt": x["prompt"]}
        path = os.path.join(presets, x["key"] + ".json")
        md.append("## %s\n`%s` - %s\n\n```\n%s\n```\n" % (x["title"], x["key"], x["aspect_ratio"], x["prompt"]))
        if os.path.exists(path) and not a.force:
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        made += 1
    if a.md:
        with open(a.md, "w", encoding="utf-8") as f:
            f.write("# Glass Face batch 2 review\n\n" + "\n".join(md))

    c = Counter(x["category"] for x in items)
    print("[OK] created %d, skipped %d (existing), total %d" % (made, skipped, len(items)))
    for k, v in c.items():
        print("  %3d  %s" % (v, k))
    print("presets dir:", presets)

if __name__ == "__main__":
    main()
