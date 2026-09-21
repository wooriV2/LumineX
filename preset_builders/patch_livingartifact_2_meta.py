# -*- coding: utf-8 -*-
r"""
patch_livingartifact_2_meta.py
Register all Living Artifact presets (presets/la_*.json) into
core/presets_meta.py -> PRESET_CATEGORIES.

- Groups presets by their JSON "category" field (must start with "🏺 Living Artifact")
- Creates missing categories, appends missing keys to existing ones (idempotent)
- Tier sets (HOF/SSS) are NOT touched — tiers are assigned after generation review
- Backup: core/presets_meta.py.bak_livingartifact
- AST validation before writing; aborts without writing on any error

Run (PowerShell, from C:\Dev\LumineX):
    $env:PYTHONUTF8="1"
    python preset_builders\patch_livingartifact_2_meta.py --dry     (preview only)
    python preset_builders\patch_livingartifact_2_meta.py
"""
import ast
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRESETS_DIR = ROOT / "presets"
META = ROOT / "core" / "presets_meta.py"
KEY_PREFIX = "la_"
CAT_PREFIX = "🏺 Living Artifact"
TARGET = "PRESET_CATEGORIES"


def collect_groups():
    groups = {}
    for path in sorted(PRESETS_DIR.glob(f"{KEY_PREFIX}*.json")):
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception as e:
            print(f"[ERROR] invalid JSON: {path.name} ({e})")
            return None
        cat = data.get("category", "")
        if not cat.startswith(CAT_PREFIX):
            print(f"[WARN] skipped (category not Living Artifact): {path.name} -> {cat!r}")
            continue
        groups.setdefault(cat, []).append(path.stem)
    return groups


def find_dict(tree):
    for node in tree.body:
        if isinstance(node, ast.Assign) and isinstance(node.value, ast.Dict):
            if any(isinstance(t, ast.Name) and t.id == TARGET for t in node.targets):
                return node.value
        if isinstance(node, ast.AnnAssign) and isinstance(node.value, ast.Dict):
            if isinstance(node.target, ast.Name) and node.target.id == TARGET:
                return node.value
    return None


def make_locator(text):
    lines = text.splitlines(keepends=True)
    starts, pos = [], 0
    for ln in lines:
        starts.append(pos)
        pos += len(ln)

    def to_abs(lineno, col_bytes):
        # ast col offsets are UTF-8 byte offsets -> convert to char offset
        line = lines[lineno - 1]
        char_col = len(line.encode("utf-8")[:col_bytes].decode("utf-8", errors="ignore"))
        return starts[lineno - 1] + char_col

    return to_abs


def prev_nonspace(text, pos):
    i = pos - 1
    while i >= 0 and text[i] in " \t\r\n":
        i -= 1
    return text[i] if i >= 0 else ""


def key_lines(keys, indent=8, per_line=3):
    out = []
    for i in range(0, len(keys), per_line):
        chunk = ", ".join(json.dumps(k, ensure_ascii=False) for k in keys[i:i + per_line])
        out.append(" " * indent + chunk + ",\n")
    return "".join(out)


def main():
    dry = "--dry" in sys.argv

    if not META.is_file():
        print(f"[ERROR] not found: {META}")
        return 1
    groups = collect_groups()
    if groups is None:
        return 1
    if not groups:
        print("[INFO] no Living Artifact presets found. nothing to do.")
        return 0

    text = META.read_text(encoding="utf-8-sig")
    tree = ast.parse(text)
    dnode = find_dict(tree)
    if dnode is None:
        print(f"[ERROR] {TARGET} dict not found in {META.name}")
        return 1
    to_abs = make_locator(text)

    # map existing categories -> list node, and all registered keys
    existing = {}
    registered = {}
    for k, v in zip(dnode.keys, dnode.values):
        if isinstance(k, ast.Constant) and isinstance(k.value, str) and isinstance(v, ast.List):
            existing[k.value] = v
            for el in v.elts:
                if isinstance(el, ast.Constant) and isinstance(el.value, str):
                    registered.setdefault(el.value, k.value)

    edits = []  # (abs_pos, insert_text)
    new_cats, appended = 0, 0

    for cat, keys in groups.items():
        for key in keys:
            if key in registered and registered[key] != cat:
                print(f"[WARN] {key} already registered under {registered[key]!r}")
        if cat in existing:
            lst = existing[cat]
            have = {el.value for el in lst.elts if isinstance(el, ast.Constant)}
            missing = [k for k in keys if k not in have]
            if not missing:
                print(f"[SKIP] {cat}: all {len(keys)} keys present")
                continue
            close = to_abs(lst.end_lineno, lst.end_col_offset) - 1  # position of ']'
            prev = prev_nonspace(text, close)
            lead = "" if prev in (",", "[") else ","
            edits.append((close, lead + "\n" + key_lines(missing) + "    "))
            appended += len(missing)
            print(f"[ADD]  {cat}: +{len(missing)} keys")
        else:
            close = to_abs(dnode.end_lineno, dnode.end_col_offset) - 1  # position of '}'
            prev = prev_nonspace(text, close)
            lead = "" if prev in (",", "{") else ","
            block = (lead + "\n    " + json.dumps(cat, ensure_ascii=False) + ": [\n"
                     + key_lines(keys) + "    ],\n")
            edits.append((close, block))
            new_cats += 1
            appended += len(keys)
            print(f"[NEW]  {cat}: {len(keys)} keys")

    if not edits:
        print("\nDone. no changes needed.")
        return 0

    new_text = text
    for pos, ins in sorted(edits, key=lambda e: e[0], reverse=True):
        new_text = new_text[:pos] + ins + new_text[pos:]

    # AST validation before writing
    try:
        new_tree = ast.parse(new_text)
    except SyntaxError as e:
        print(f"[ERROR] AST validation failed, file NOT written: {e}")
        return 1
    ndict = find_dict(new_tree)
    check = {}
    for k, v in zip(ndict.keys, ndict.values):
        if isinstance(k, ast.Constant) and isinstance(k.value, str) and k.value.startswith(CAT_PREFIX):
            check[k.value] = set(ast.literal_eval(v))
    for cat, keys in groups.items():
        miss = [k for k in keys if k not in check.get(cat, set())]
        if miss:
            print(f"[ERROR] verification failed for {cat}: missing {miss[:3]}... file NOT written")
            return 1

    if dry:
        print(f"\n[DRY] AST OK. would add {new_cats} categories / {appended} keys. nothing written.")
        return 0

    backup = META.with_suffix(".py.bak_livingartifact")
    shutil.copy2(META, backup)
    META.write_text(new_text, encoding="utf-8")
    print(f"\nDone. AST OK. categories added={new_cats}, keys added={appended}")
    print(f"backup: {backup.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
