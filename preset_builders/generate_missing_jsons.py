# -*- coding: utf-8 -*-
"""
generate_missing_jsons.py
presets_meta.py를 직접 파싱해서 JSON 생성 (import 방식 대신 파일 직접 읽기)
실행: python preset_builders/generate_missing_jsons.py
"""
import json
import sys
import importlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"

print(f"ROOT: {ROOT}")
print(f"PRESETS_DIR: {PRESETS_DIR}")

# UTF-8 강제 설정
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

# presets_meta.py를 UTF-8로 강제 로드
import importlib.util
spec = importlib.util.spec_from_file_location(
    "presets_meta",
    ROOT / "core" / "presets_meta.py",
)
mod = importlib.util.module_from_spec(spec)
# UTF-8로 소스 읽기
source = (ROOT / "core" / "presets_meta.py").read_text(encoding="utf-8")
code = compile(source, str(ROOT / "core" / "presets_meta.py"), "exec")
exec(code, mod.__dict__)

PRESET_CATEGORIES = mod.PRESET_CATEGORIES

created = []
skipped = []
errors  = []

for category, presets in PRESET_CATEGORIES.items():
    if not isinstance(presets, list):
        continue
    for preset in presets:
        if not isinstance(preset, dict):
            continue

        preset_id = preset.get("id")
        prompt    = preset.get("prompt", "")

        if not preset_id:
            continue

        json_path = PRESETS_DIR / f"{preset_id}.json"

        if json_path.exists():
            skipped.append(preset_id)
            continue

        try:
            data = {
                "id":       preset_id,
                "prompt":   prompt,
                "category": category,
            }
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            created.append(preset_id)
            print(f"  OK: {preset_id}")
        except Exception as e:
            errors.append((preset_id, str(e)))
            print(f"  ERR: {preset_id} - {e}")

print(f"\n{'='*50}")
print(f"Created: {len(created)}")
print(f"Skipped: {len(skipped)}")
print(f"Errors:  {len(errors)}")
if errors:
    for pid, err in errors:
        print(f"   - {pid}: {err}")
