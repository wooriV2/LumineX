# -*- coding: utf-8 -*-
"""
이미 생성된 la_preg_*.json, la_mixed_*.json 950개 preset 파일의 category 필드를
"🤰 Living Artifact · ..." -> "🏺 Living Artifact · ..." 로 고칩니다.
(등록 스크립트가 🏺로 시작하는 카테고리만 인식해서, 🤰로 저장된 950개가
patch_livingartifact_2_meta.py에서 전부 스킵됐습니다.)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\fix_pregnant_category_emoji.py
  python preset_builders\patch_livingartifact_2_meta.py
  git add -A
  git commit -m "Fix category emoji for Pregnant Formula presets (🤰 -> 🏺) and register"
  git push
"""
import json
import os
import glob

PRESETS_DIR = os.path.join(os.path.dirname(__file__), "..", "presets")

def main():
    patterns = ["la_preg_*.json", "la_mixed_*.json"]
    fixed = 0
    skipped = 0
    for pattern in patterns:
        for path in glob.glob(os.path.join(PRESETS_DIR, pattern)):
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            cat = data.get("category", "")
            if cat.startswith("🤰"):
                data["category"] = "🏺" + cat[1:]
                with open(path, "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                fixed += 1
            else:
                skipped += 1
    print(f"수정 완료: {fixed}개 파일의 category를 🏺로 변경했습니다. (이미 🏺였거나 대상 아님: {skipped}개)")

if __name__ == "__main__":
    main()
