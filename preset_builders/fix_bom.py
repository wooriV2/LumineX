# -*- coding: utf-8 -*-
"""
fix_bom.py
==========
core/presets_meta.py UTF-8 BOM 제거 + 문법 검증

실행:
  cd C:\\Dev\\LumineX
  python preset_builders\\fix_bom.py
"""

import ast
import sys
from pathlib import Path

TARGET = Path(__file__).parent.parent / "core" / "presets_meta.py"


def fix_bom():
    # BOM 포함 읽기
    raw = TARGET.read_bytes()

    if raw.startswith(b'\xef\xbb\xbf'):
        print("[INFO] UTF-8 BOM 감지 — 제거 중...")
        raw = raw[3:]
    else:
        print("[INFO] BOM 없음")

    content = raw.decode("utf-8")

    # 문법 검증
    try:
        ast.parse(content)
        print("[OK] 문법 정상")
    except SyntaxError as e:
        print(f"[ERROR] BOM 제거 후에도 문법 오류: line {e.lineno} — {e.msg}")
        lines = content.splitlines()
        start = max(0, e.lineno - 5)
        end = min(len(lines), e.lineno + 5)
        for i, line in enumerate(lines[start:end], start=start + 1):
            marker = " <<< HERE" if i == e.lineno else ""
            print(f"{i:4d}: {repr(line)}{marker}")
        sys.exit(1)

    # BOM 없이 저장
    TARGET.write_text(content, encoding="utf-8")
    print("[OK] BOM 제거 후 저장 완료")


if __name__ == "__main__":
    print("=== BOM 제거 시작 ===")
    fix_bom()
    print("\n다음 단계:")
    print("  git add core/presets_meta.py")
    print('  git commit -m "fix: presets_meta.py UTF-8 BOM 제거"')
    print("  git push")
