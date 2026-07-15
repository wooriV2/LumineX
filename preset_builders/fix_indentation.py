# -*- coding: utf-8 -*-
"""
fix_indentation.py
==================
core/presets_meta.py IndentationError 진단 및 수정

실행:
  cd C:\Dev\LumineX
  python preset_builders\fix_indentation.py
"""

import sys
from pathlib import Path

TARGET = Path(__file__).parent.parent / "core" / "presets_meta.py"


def diagnose():
    """문법 오류 위치 찾기"""
    import ast
    content = TARGET.read_text(encoding="utf-8")
    try:
        ast.parse(content)
        print("[OK] 문법 오류 없음")
        return None
    except SyntaxError as e:
        print(f"[ERROR] {e.msg} — line {e.lineno}")
        lines = content.splitlines()
        start = max(0, e.lineno - 5)
        end = min(len(lines), e.lineno + 5)
        print("\n--- 문제 구간 ---")
        for i, line in enumerate(lines[start:end], start=start + 1):
            marker = " <<< HERE" if i == e.lineno else ""
            print(f"{i:4d}: {repr(line)}{marker}")
        return e.lineno


def fix():
    """
    패치 스크립트가 삽입한 카테고리 블록의 들여쓰기 정규화
    PRESET_CATEGORIES dict 내부는 4칸 들여쓰기가 표준
    """
    content = TARGET.read_text(encoding="utf-8")
    lines = content.splitlines()
    fixed_lines = []
    inside_new_cats = False

    # Phenomenal 5 카테고리 키 목록
    NEW_CAT_KEYS = [
        '"🧲 Ferrofluid Glamour"',
        '"🐦 Murmuration Glamour"',
        '"🎵 Cymatics Glamour"',
        '"🔬 Micro Scale Glamour"',
        '"🫧 Mycelium Glamour"',
    ]

    for line in lines:
        stripped = line.lstrip()

        # 새 카테고리 블록 시작 감지
        if any(key in line for key in NEW_CAT_KEYS):
            inside_new_cats = True

        if inside_new_cats:
            # 빈 줄은 그대로
            if stripped == "":
                fixed_lines.append("")
                continue

            # 카테고리 키 라인: 4칸
            if stripped.startswith('"🧲') or stripped.startswith('"🐦') or \
               stripped.startswith('"🎵') or stripped.startswith('"🔬') or \
               stripped.startswith('"🫧'):
                fixed_lines.append("    " + stripped)
                continue

            # 닫는 ] + 쉼표: 4칸
            if stripped in ("],", "]"):
                fixed_lines.append("    " + stripped)
                # 마지막 카테고리 닫힘 후 종료
                if stripped == "],":
                    inside_new_cats = False
                continue

            # 프리셋 항목: 8칸
            if stripped.startswith('"') and (stripped.endswith('",') or stripped.endswith('"')):
                fixed_lines.append("        " + stripped)
                continue

            # 여는 [: 4칸
            if stripped == "[":
                fixed_lines.append("    " + stripped)
                continue

            fixed_lines.append(line)
        else:
            fixed_lines.append(line)

    fixed_content = "\n".join(fixed_lines)

    # 수정 후 파싱 확인
    import ast
    try:
        ast.parse(fixed_content)
        TARGET.write_text(fixed_content, encoding="utf-8")
        print("[OK] 들여쓰기 수정 완료 및 저장")
    except SyntaxError as e:
        print(f"[ERROR] 수정 후에도 오류 존재: line {e.lineno} — {e.msg}")
        print("수동 확인이 필요합니다.")
        sys.exit(1)


if __name__ == "__main__":
    print("=== presets_meta.py 들여쓰기 진단 ===")
    err_line = diagnose()

    if err_line:
        print("\n=== 수정 시도 ===")
        fix()
        print("\n=== 수정 후 재진단 ===")
        diagnose()
        print("\n다음 단계:")
        print("  git add core/presets_meta.py")
        print('  git commit -m "fix: presets_meta.py IndentationError 수정"')
        print("  git push")
    else:
        print("수정 불필요")
