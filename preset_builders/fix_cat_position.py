# -*- coding: utf-8 -*-
"""
fix_cat_position.py
===================
PRESET_CATEGORIES } 닫힘 이후에 잘못 삽입된
Phenomenal 5 카테고리 블록을 올바른 위치로 이동

실행:
  cd C:\\Dev\\LumineX
  python preset_builders\\fix_cat_position.py
"""

import ast
import sys
from pathlib import Path

TARGET = Path(__file__).parent.parent / "core" / "presets_meta.py"

NEW_CAT_KEYS = [
    "Ferrofluid Glamour",
    "Murmuration Glamour",
    "Cymatics Glamour",
    "Micro Scale Glamour",
    "Mycelium Glamour",
]


def fix():
    raw = TARGET.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        print("[INFO] BOM 제거")
        raw = raw[3:]
    content = raw.decode("utf-8")
    lines = content.splitlines()

    # ── 1. 잘못 삽입된 블록 위치 찾기 ──
    extract_start = None
    extract_end = None

    for i, line in enumerate(lines):
        if extract_start is None:
            if any(k in line for k in NEW_CAT_KEYS):
                extract_start = i
                print(f"[INFO] 블록 시작: line {i+1} — {line.strip()[:60]}")
        if extract_start is not None:
            if "Mycelium Glamour" in lines[i]:
                # Mycelium 블록 끝 ],  찾기
                for j in range(i, min(i + 30, len(lines))):
                    if lines[j].strip() == "],":
                        extract_end = j
                        break
                if extract_end:
                    break

    if extract_start is None or extract_end is None:
        print("[ERROR] 블록을 찾을 수 없습니다")
        sys.exit(1)

    print(f"[INFO] 블록 범위: line {extract_start+1} ~ {extract_end+1}")

    # 블록 추출 (앞뒤 빈줄 포함)
    inserted_block = lines[extract_start:extract_end + 1]

    # 제거된 라인 목록
    new_lines = lines[:extract_start] + lines[extract_end + 1:]

    # ── 2. PRESET_CATEGORIES 닫힘 } 위치 찾기 ──
    anchor = "from core.hof_tier import HOF_TIER"
    anchor_idx = None
    for i, line in enumerate(new_lines):
        if anchor in line:
            anchor_idx = i
            break

    if anchor_idx is None:
        print(f"[ERROR] anchor '{anchor}' 없음")
        sys.exit(1)

    close_idx = None
    for i in range(anchor_idx - 1, -1, -1):
        if new_lines[i].strip() == "}":
            close_idx = i
            break

    if close_idx is None:
        print("[ERROR] PRESET_CATEGORIES 닫힘 } 없음")
        sys.exit(1)

    print(f"[INFO] 삽입 위치 (} 바로 앞): line {close_idx+1}")

    # ── 3. 들여쓰기 정규화 ──
    normalized = []
    for line in inserted_block:
        stripped = line.strip()
        if stripped == "":
            normalized.append("")
            continue
        # 카테고리 키 라인
        if stripped.startswith('"') and any(k in stripped for k in NEW_CAT_KEYS):
            normalized.append("    " + stripped)
        # 여는 [
        elif stripped == "[":
            normalized.append("    " + stripped)
        # 닫는 ],
        elif stripped in ("],", "]"):
            normalized.append("    " + stripped)
        # 프리셋 항목
        elif stripped.startswith('"'):
            normalized.append("        " + stripped)
        else:
            normalized.append("    " + stripped)

    # ── 4. } 앞에 삽입 ──
    final_lines = (
        new_lines[:close_idx] +
        [""] +
        normalized +
        [""] +
        new_lines[close_idx:]
    )

    final_content = "\n".join(final_lines)

    # ── 5. 문법 검증 ──
    try:
        ast.parse(final_content)
        print("[OK] 문법 정상")
    except SyntaxError as e:
        print(f"[ERROR] 수정 후 문법 오류: line {e.lineno} — {e.msg}")
        ctx = final_content.splitlines()
        s = max(0, e.lineno - 5)
        en = min(len(ctx), e.lineno + 5)
        for i, l in enumerate(ctx[s:en], start=s + 1):
            marker = " <<< HERE" if i == e.lineno else ""
            print(f"{i:4d}: {repr(l)}{marker}")
        sys.exit(1)

    TARGET.write_text(final_content, encoding="utf-8")
    print("[OK] 저장 완료")


if __name__ == "__main__":
    print("=== PRESET_CATEGORIES 위치 수정 시작 ===")
    fix()
    print("\n다음 단계:")
    print("  git add core/presets_meta.py")
    print('  git commit -m "fix: Phenomenal5 카테고리 삽입 위치 수정 + BOM 제거"')
    print("  git push")
