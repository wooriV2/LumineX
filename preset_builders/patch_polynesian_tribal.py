"""
preset_builders/patch_polynesian_tribal.py
polynesian_tribal.json — 바디페인팅 감지 키워드 누락 수정
outfit에 "painted directly on bare skin" 추가
실행: python preset_builders/patch_polynesian_tribal.py
"""

import json
from pathlib import Path

PRESET_PATH = Path("presets/polynesian_tribal.json")

def patch():
    if not PRESET_PATH.exists():
        print(f"[ERROR] {PRESET_PATH} 없음.")
        return

    with open(PRESET_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    old_outfit = data.get("outfit", "")
    print(f"[현재] outfit: {old_outfit}")

    # painted directly on bare skin 추가
    if "painted directly on bare skin" in old_outfit:
        print("[WARN] 이미 패치됨.")
        return

    new_outfit = old_outfit.replace(
        "covering entire figure",
        "painted directly on bare skin, NOT wearing fabric, covering entire figure"
    )

    # subject/tag/body 누락 보완
    if "tag" not in data:
        data["tag"] = "Polynesian Tribal"
    if "subject" not in data:
        data["subject"] = "a Polynesian tribal body art female model"
    if "body" not in data:
        data["body"] = "powerful voluptuous frame, Polynesian goddess proportions, statuesque island curves"

    data["outfit"] = new_outfit
    data["negative"] = "clothing, fabric, wearing, dressed, outfit, garment, painted on bare skin, NO clothing"

    with open(PRESET_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"[OK] 수정 완료")
    print(f"[새값] outfit: {new_outfit}")

if __name__ == "__main__":
    patch()
