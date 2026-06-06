"""
add_new_presets_v15.py
바디페인팅 확장 40개

🎨 명화/작가 — 퍼블릭 도메인 (14개)
  cezanne_body, gauguin_tropics, toulouse_lautrec, schiele_body,
  degas_dancer, renoir_soft, botticelli_venus, titian_goddess,
  rubens_baroque, ingres_odalisque, waterhouse_nymph, rossetti_dante,
  alma_tadema, vigee_lebrun

🎨 생존/최근 작가 — 내부 테스트용 (6개)
  banksy_stencil, keith_haring_body, yayoi_kusama, takashi_murakami,
  jean_dubuffet, jean_cocteau

🌍 부족/문화 계열 (10개)
  bodi_clay, ndebele_pattern, tuareg_indigo, mursi_lip, himba_ochre,
  surma_body, asaro_mudmen, kayapo_brasil, nuba_scarification, kayan_neck

🔬 과학/자연 계열 (10개)
  thermal_scan, bioluminescent_deep, microscope_pollen, xray_body,
  mri_scan_body, neural_map, geologic_strata, crystal_lattice,
  solar_system_body, dna_double_helix

총 프리셋: 480 → 520개
바디페인팅 카테고리: 101 → 141개
"""

import json
from pathlib import Path
import os

PRESETS_DIR = Path("presets")
PRESETS_DIR.mkdir(exist_ok=True)
V15_DIR = Path("/home/claude/presets_v15")

added = 0
skipped = 0

for json_file in sorted(V15_DIR.glob("*.json")):
    name = json_file.stem
    dest = PRESETS_DIR / json_file.name
    if dest.exists():
        print(f"⏭️  skip: {name}")
        skipped += 1
    else:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        with open(dest, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"✅ added: {name}")
        added += 1

print(f"\n완료: {added}개 추가, {skipped}개 스킵")
print(f"총 프리셋: 480 → {480 + added}개")
print(f"바디페인팅 카테고리: 101 → {101 + added}개")