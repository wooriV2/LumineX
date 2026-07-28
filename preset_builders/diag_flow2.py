import glob, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT  = []
def p(s=""): OUT.append(str(s))

# [A] JSON 스키마 그룹 (끊긴 부분 복구)
p("=" * 60); p("[A] 프리셋 스키마 그룹"); p("=" * 60)
files = sorted(glob.glob(str(ROOT / "presets" / "*.json")))
schemas, bad = {}, []
for f in files:
    try: d = json.load(open(f, encoding="utf-8-sig"))
    except Exception as e: bad.append(f"{Path(f).name}: {e}"); continue
    schemas.setdefault(tuple(sorted(d)), []).append(Path(f).stem)
p(f"총 {len(files)}개 / 파싱실패 {len(bad)}개")
for b in bad[:20]: p("  FAIL " + b)
for ks, names in sorted(schemas.items(), key=lambda x: -len(x[1])):
    p(f"\n  [{len(names)}개] {', '.join(ks)}")
    p(f"    예: {', '.join(names[:5])}")

# [B] prompt / gemini / chatgpt 키 사용 맥락
p("\n" + "=" * 60); p("[B] prompt/gemini/chatgpt 참조 맥락"); p("=" * 60)
src = (ROOT / "core" / "builders.py").read_text(encoding="utf-8").splitlines()
for i, line in enumerate(src, 1):
    if re.search(r"data(?:\.get)?\s*[\(\[]\s*['\"](prompt|gemini|chatgpt)['\"]", line):
        for j in range(max(0, i - 4), min(len(src), i + 4)):
            p(f"  {'>>' if j + 1 == i else '  '} L{j+1}: {src[j]}")
        p("  " + "-" * 40)

# [C] 프리셋을 읽는 코드가 어디 있나
p("\n" + "=" * 60); p("[C] 프리셋 로드 / 빌더 호출 지점"); p("=" * 60)
pats = {
    "presets 경로":  r"presets[/\\]|PRESET_DIR|presets_dir",
    "json.load":     r"json\.loads?\s*\(",
    "빌더 호출":     r"build_(gemini|chatgpt|midjourney)_prompt\s*\(",
    "9필드 접근":    r"\[['\"](subject|environment|lighting|quality|tag)['\"]\]",
}
for py in sorted(ROOT.glob("*.py")) + sorted(ROOT.glob("core/*.py")):
    if py.name == Path(__file__).name: continue
    try: lines = py.read_text(encoding="utf-8").splitlines()
    except Exception: continue
    hits = [(lbl, n, l.strip()) for lbl, pt in pats.items()
            for n, l in enumerate(lines, 1) if re.search(pt, l)]
    if hits:
        p(f"\n--- {py.relative_to(ROOT)} ---")
        for lbl, n, l in hits[:40]:
            p(f"  [{lbl}] L{n}: {l[:160]}")

Path(ROOT / "diag_report.txt").write_text("\n".join(OUT), encoding="utf-8")
print("\n".join(OUT[:80]))
print(f"\n... 전문: {ROOT / 'diag_report.txt'}")
