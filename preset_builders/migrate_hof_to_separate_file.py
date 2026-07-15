# -*- coding: utf-8 -*-
"""
HOF_TIER를 core/hof_tier.py로 분리 + presets_meta.py에서 import로 교체
실행: python preset_builders/migrate_hof_to_separate_file.py
"""
from pathlib import Path
import re

META = Path("core/presets_meta.py")
HOF_FILE = Path("core/hof_tier.py")

def migrate():
    content = META.read_text(encoding="utf-8")
    lines = content.splitlines(keepends=True)

    # HOF_TIER 블록 찾기
    hof_start = None
    hof_end = None
    brace_depth = 0
    for i, line in enumerate(lines):
        if line.strip().startswith("HOF_TIER = {"):
            hof_start = i
            brace_depth = 0
        if hof_start is not None:
            brace_depth += line.count("{") - line.count("}")
            if brace_depth <= 0 and i > hof_start:
                hof_end = i
                break

    if hof_start is None or hof_end is None:
        print("❌ HOF_TIER 블록 탐지 실패")
        return

    print(f"HOF_TIER 블록: {hof_start+1}~{hof_end+1}줄")

    # HOF_TIER 블록 추출
    hof_block = "".join(lines[hof_start:hof_end+1])

    # core/hof_tier.py 생성
    hof_file_content = (
        "# -*- coding: utf-8 -*-\n"
        '"""\n'
        "LumineX HOF_TIER — Hall of Fame 프리셋 목록\n"
        "패치 시 이 파일만 수정하면 됩니다.\n"
        'add_hof(\"key\") 함수로 간편 추가 가능.\n'
        '"""\n\n'
        + hof_block
        + "\n\ndef add_hof(*keys):\n"
        "    for k in keys:\n"
        "        HOF_TIER.add(k)\n"
    )

    HOF_FILE.write_text(hof_file_content, encoding="utf-8")
    print(f"✅ {HOF_FILE} 생성 완료")

    # presets_meta.py에서 HOF_TIER 블록 → import 한 줄로 교체
    new_lines = (
        lines[:hof_start]
        + ["from core.hof_tier import HOF_TIER  # HOF 추가는 core/hof_tier.py에서\n"]
        + lines[hof_end+1:]
    )
    META.write_text("".join(new_lines), encoding="utf-8")
    print(f"✅ {META} HOF_TIER 블록 → import 교체 완료")

    # 검증
    new_content = META.read_text(encoding="utf-8")
    if "from core.hof_tier import HOF_TIER" in new_content:
        print("✅ import 확인")
    if "HOF_TIER = {" not in new_content:
        print("✅ 원본 블록 제거 확인")

    hof_content = HOF_FILE.read_text(encoding="utf-8")
    count = hof_content.count('",')
    print(f"✅ HOF 항목 수 (추정): {count}개")

    print("\n🎉 마이그레이션 완료!")
    print("앞으로 HOF 추가는 core/hof_tier.py 파일 하단에 추가하면 됩니다.")
    print('\ngit add core/ ; git commit -m "🔧 HOF_TIER core/hof_tier.py로 분리"; git push')

if __name__ == "__main__":
    migrate()
