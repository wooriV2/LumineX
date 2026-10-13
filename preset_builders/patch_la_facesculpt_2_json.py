# -*- coding: utf-8 -*-
r"""
Face Sculpt Formula 300개(v2: 귀 스타일·피어싱 단계 P5~P200·추가 축 랜덤 풀 반영) -> presets/la_facesculpt_NNN.json 을 같은 키로 덮어씁니다.

  la_facesculpt_300_bundle_v2.json  (신규 카테고리: 🏺 Living Artifact · Face Sculpt Formula)
  구성: 눈 주인공 120(정면) + 립 주인공 120(45도, 신규 입술 6종 포함) + 얼굴 유형 60(바비·브랫츠·서큐버스·세이렌)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_facesculpt_2_json.py
  (같은 키를 덮어쓰므로 메타 등록 스크립트는 다시 돌릴 필요가 없습니다. 돌려도 'keys added=0' 입니다.)
사전 준비: la_facesculpt_300_bundle_v2.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_facesculpt_300_bundle_v2.json"]

def main():
    os.makedirs(PRESETS_DIR, exist_ok=True)
    written, by_cat, overwritten = 0, {}, 0
    for name in BUNDLES:
        path = os.path.join(HERE, name)
        if not os.path.exists(path):
            raise SystemExit(f"번들 파일이 없습니다: {path}")
        with open(path, "r", encoding="utf-8") as f:
            presets = json.load(f)
        for item in presets:
            if not item["category"].startswith("🏺 Living Artifact"):
                raise SystemExit(f"카테고리 접두어 오류: {item['key']}")
            target = os.path.join(PRESETS_DIR, item["key"] + ".json")
            if os.path.exists(target):
                overwritten += 1
            out = {k: item[k] for k in ("key", "category", "title", "prompt", "meta")}
            with open(target, "w", encoding="utf-8") as f2:
                json.dump(out, f2, ensure_ascii=False, indent=2)
            written += 1
            by_cat[item["category"]] = by_cat.get(item["category"], 0) + 1
    if overwritten:
        print(f"주의: 이미 있던 키 {overwritten}개를 덮어썼습니다.")
    print(f"완료: {written}개 preset 파일을 {PRESETS_DIR} 에 생성했습니다.")
    for c, cnt in by_cat.items():
        print(f"  {c}: {cnt}개")

if __name__ == "__main__":
    main()
