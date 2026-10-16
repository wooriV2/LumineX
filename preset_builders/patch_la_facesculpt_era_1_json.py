# -*- coding: utf-8 -*-
r"""
Face Sculpt Era Icon Formula 65개(기존 메이크업과 겹치지 않는 13종 x 5개) -> presets/la_facesculpt_era_NNN.json

  la_facesculpt_era_065_bundle.json  (신규 카테고리: 🏺 Living Artifact · Face Sculpt Era Icon Formula)
  구성: 서양 60s 모드·90s 그런지, 흑인 90s R&B 시크, 동유럽 아이스, 중동·남아시아 글램, 크롬 메탈릭, 비비드 컬러 팝, 초콜릿 모노크롬, 화이트 포인트 골드, 노르딕 쉴드메이든, 파리 오트쿠튀르 그래픽, 아이스 퀸 서리 균열, 포슬린 조각상 (13종 x 5개)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_facesculpt_era_1_json.py
  python preset_builders\patch_livingartifact_2_meta.py     (신규 카테고리라 메타 등록 필요)
사전 준비: la_facesculpt_era_065_bundle.json 을 preset_builders\ 폴더에 두세요.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PRESETS_DIR = os.path.join(HERE, "..", "presets")
BUNDLES = ["la_facesculpt_era_065_bundle.json"]

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
