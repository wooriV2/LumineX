import glob, inspect, json, re, sys, traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
import core.builders as B

def head(t):
    print("\n" + "=" * 64); print(t); print("=" * 64)

# [1] 최상위 심볼
head("[1] builders.py 심볼")
for name, obj in vars(B).items():
    if callable(obj) and getattr(obj, "__module__", "") == B.__name__:
        try: print(f"  def {name}{inspect.signature(obj)}")
        except Exception: print(f"  def {name}(?)")
    elif isinstance(obj, dict) and not name.startswith("__"):
        print(f"  dict {name}  len={len(obj)}  sample={list(obj)[:5]}")

# [2] 소스가 참조하는 data 키
head("[2] builders.py가 참조하는 data 키")
src = (ROOT / "core" / "builders.py").read_text(encoding="utf-8")
ref = sorted(set(re.findall(r"data(?:\.get)?\s*[\(\[]\s*['\"]([^'\"]+)['\"]", src)))
print("  " + ", ".join(ref) if ref else "  (없음 — data 딕셔너리를 안 쓴다)")

# [3] 딕셔너리 조회 지점
head("[3] 대문자 상수 조회 지점")
for m in re.finditer(r"^.*\b([A-Z_]{3,})\s*\[.*$", src, re.M):
    print(f"  L{src[:m.start()].count(chr(10))+1}: {m.group(0).strip()}")

# [4] 프리셋 JSON 실제 키
head("[4] 프리셋 JSON 키")
files = sorted(glob.glob(str(ROOT / "presets" / "*.json")))
print(f"  총 {len(files)}개")
schemas = {}
for f in files:
    try: d = json.load(open(f, encoding="utf-8-sig"))
    except Exception as e: print(f"  [PARSE FAIL] {Path(f).name}: {e}"); continue
    schemas.setdefault(tuple(sorted(d)), []).append(Path(f).stem)
for ks, names in sorted(schemas.items(), key=lambda x: -len(x[1])):
    print(f"\n  {len(names)}개 | {', '.join(ks)}")
    print(f"    예: {', '.join(names[:4])}")

# [5] 차집합 — 이게 §9의 답
head("[5] 판정: 빌더 요구 키 - JSON 보유 키")
for ks, names in schemas.items():
    missing = [k for k in ref if k not in ks]
    print(f"  [{names[0]} 계열 {len(names)}개] 결손: {missing or '없음'}")

# [6] 실제 호출
head("[6] 실호출")
entries = [n for n in vars(B) if n.startswith("build") and callable(getattr(B, n))]
sample = files[0] if files else None
if sample:
    d = json.load(open(sample, encoding="utf-8-sig"))
    print(f"  대상: {Path(sample).stem}")
    for n in entries:
        try:
            out = getattr(B, n)(d)
            print(f"\n  --- {n} OK ---\n  {str(out)[:400]}")
        except Exception as e:
            print(f"\n  --- {n} {type(e).__name__}: {e} ---")
