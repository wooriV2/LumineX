# -*- coding: utf-8 -*-
"""
dashboard.py 분리 패치 (A안)
PRESET_CATEGORIES + HOF_TIER + SSS_TIER + SS_TIER 를
core/presets_meta.py 로 추출하고
dashboard.py 에는 import 한 줄로 대체

실행: python preset_builders\patch_extract_presets_meta.py
위치: C:\Dev\LumineX\ 에서 실행
"""

from pathlib import Path
import re

DASHBOARD  = Path("dashboard.py")
META_OUT   = Path("core/presets_meta.py")

assert DASHBOARD.exists(), "dashboard.py 없음 — 프로젝트 루트에서 실행하세요."
assert Path("core").exists(), "core/ 폴더 없음."

text = DASHBOARD.read_text(encoding="utf-8")
original_len = len(text.splitlines())

# ─────────────────────────────────────────────────────────
# 1. 추출 범위 결정
#    PRESET_CATEGORIES = { ... } 시작
#    SS_TIER = { ... } 끝 (마지막 닫는 } 다음 줄)
# ─────────────────────────────────────────────────────────

START_MARKER = "\nPRESET_CATEGORIES = {"
END_MARKER   = "\n}\n\n# ─── 다크 테마 CSS"

assert START_MARKER in text, f"PRESET_CATEGORIES 시작 마커를 찾을 수 없어요."
assert END_MARKER   in text, f"SS_TIER 종료 마커를 찾을 수 없어요."

start_idx = text.index(START_MARKER) + 1        # \n 뒤부터
end_idx   = text.index(END_MARKER)   + len("\n}\n")   # } 포함해서 자르기

extracted_block = text[start_idx:end_idx]
print(f"추출 범위: 약 {len(extracted_block.splitlines())}줄")

# ─────────────────────────────────────────────────────────
# 2. core/presets_meta.py 생성
# ─────────────────────────────────────────────────────────

META_HEADER = '''\
# -*- coding: utf-8 -*-
"""
LumineX Preset Metadata
카테고리 정의 + HOF / SSS / SS 티어

dashboard.py 에서 분리 (A안)
패치 시 이 파일만 수정하면 됩니다.
"""

'''

META_OUT.write_text(META_HEADER + extracted_block, encoding="utf-8")
meta_lines = len(META_OUT.read_text(encoding="utf-8").splitlines())
print(f"✅ core/presets_meta.py 생성 완료 ({meta_lines}줄)")

# ─────────────────────────────────────────────────────────
# 3. dashboard.py 에서 추출 블록 제거 → import 한 줄로 대체
# ─────────────────────────────────────────────────────────

IMPORT_LINE = "from core.presets_meta import PRESET_CATEGORIES, HOF_TIER, SSS_TIER, SS_TIER\n"

new_text = text[:start_idx] + IMPORT_LINE + text[end_idx:]

# ─────────────────────────────────────────────────────────
# 4. 기존 import 블록 바로 뒤에 위치 조정
#    (from core.builders import ... 다음 줄에 삽입되도록)
#    → 이미 위에서 PRESET_CATEGORIES 위치에 삽입됐으므로 OK
#    단, 중복 import 방지 확인
# ─────────────────────────────────────────────────────────

if new_text.count("from core.presets_meta import") > 1:
    # 혹시 두 번 들어갔으면 첫 번째 것만 남기기
    second = new_text.index("from core.presets_meta import",
                             new_text.index("from core.presets_meta import") + 1)
    new_text = new_text[:second] + new_text[second + len(IMPORT_LINE):]
    print("⚠️  중복 import 제거됨")

DASHBOARD.write_text(new_text, encoding="utf-8")
new_lines = len(new_text.splitlines())
print(f"✅ dashboard.py 저장 완료 ({original_len}줄 → {new_lines}줄, -{original_len - new_lines}줄 감소)")

# ─────────────────────────────────────────────────────────
# 5. 검증
# ─────────────────────────────────────────────────────────

verify = DASHBOARD.read_text(encoding="utf-8")

checks = [
    ("from core.presets_meta import" in verify,       "import 줄 존재"),
    ("PRESET_CATEGORIES = {"         not in verify,   "PRESET_CATEGORIES 원본 제거됨"),
    ("HOF_TIER = {"                  not in verify,   "HOF_TIER 원본 제거됨"),
    ("SSS_TIER = {"                  not in verify,   "SSS_TIER 원본 제거됨"),
    ("SS_TIER = {"                   not in verify,   "SS_TIER 원본 제거됨"),
]

all_ok = True
for ok, label in checks:
    icon = "✅" if ok else "❌"
    print(f"  {icon} {label}")
    if not ok:
        all_ok = False

# presets_meta.py 검증
meta_text = META_OUT.read_text(encoding="utf-8")
meta_checks = [
    ("PRESET_CATEGORIES = {" in meta_text, "PRESET_CATEGORIES 존재"),
    ("HOF_TIER = {"          in meta_text, "HOF_TIER 존재"),
    ("SSS_TIER = {"          in meta_text, "SSS_TIER 존재"),
    ("SS_TIER = {"           in meta_text, "SS_TIER 존재"),
]
for ok, label in meta_checks:
    icon = "✅" if ok else "❌"
    print(f"  {icon} presets_meta.py: {label}")
    if not ok:
        all_ok = False

if all_ok:
    print("\n🎉 분리 완료! streamlit run dashboard.py 로 재시작하세요.")
    print(f"   dashboard.py : {new_lines}줄")
    print(f"   presets_meta : {meta_lines}줄")
else:
    print("\n❌ 일부 검증 실패 — 위 항목 확인 필요")
