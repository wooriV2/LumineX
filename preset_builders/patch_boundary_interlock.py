# -*- coding: utf-8 -*-
r"""
기존 등록 프리셋의 경계 문장 교체: "흐릿한 전환 구역(hazy transition zone)" 문장을
"재질끼리 자연스럽게 맞물려 닿는다(interlock)" 문장으로 바꾸고, 효과 미확인이던 보호 문장("never left bare")을 지운다.
(2026-10-07 시험: 흐릿한 전환 구역 문장이 은색 선·띠를 만들었고, 맞물림 문장은 시험 12개 중 11개에서 사라지거나 아주 가는 선만 남음)

프리셋 파일을 직접 고치므로 제목·메타·이전 수정(재질명 제목, 중복 단어)은 그대로 유지됩니다.
이미 바뀐 파일은 건너뛰므로 여러 번 실행해도 안전합니다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_boundary_interlock.py          # 시험 실행(파일 안 고침, 개수만 보고)
  python preset_builders\patch_boundary_interlock.py --apply  # 실제로 고침
"""
import json, os, re, sys, glob, collections

P1 = re.compile(r"The boundaries between regions are hazy and feathered — there is no visible line at all\. Each transition zone is about a hand's width wide, and across it the neighbouring (?P<n>patterns|materials|leaf colours) dissolve into each other, (?P<e>motifs|elements|flakes) from one thinning out as (?P=e) from the other appear, density fading rather than stopping abruptly, never a hard edge\.")
# Structure Pack '큰 조각' 구조의 경계 문장
P3 = re.compile(r"The patch edges are hazy and feathered — there is no visible outline at all\. Around each patch, a transition zone about a hand's width wide lets the patch's material and the background material dissolve into each other, elements from one thinning out as elements from the other appear, density fading rather than stopping abruptly, never a hard edge\.")
P2 = re.compile(r" Even inside a transition zone the skin is never left bare: at every point one (?:pattern|material|colour), or a mixture of the two, fully covers it\.?")
NEW3 = ("Where a patch meets the background, the two materials interlock naturally: elements of one reach into the other and the two materials simply touch, "
        "so the edge of every patch is made only of the patch's material and the background material, each in its own colours, with no gap between them.")
def _new(m):
    n, e = m.group("n"), m.group("e")
    u = {"patterns": "patterns", "materials": "materials", "leaf colours": "colours"}[n]
    tail = "each in its own colours, with no gap between them" if n != "leaf colours" else "with no gap between them"
    return f"Where two regions meet, the {n} interlock naturally: {e} of one reach into the other and the two {u} simply touch, so the boundary is made only of the two neighbouring {u}, {tail}."
def _dups(t): return len(re.findall(r"\b(\w+) \1\b", t))
def interlock(t):
    """흐릿한 전환 구역 문장 → 맞물림 경계 문장(변형 C). 보호 문장 삭제. 바꿀 것이 없으면 None."""
    n0 = t.count("hazy and feathered")
    if n0 == 0: return None
    d0, c0 = _dups(t), t.count(".,")
    t, a = P1.subn(_new, t); t, c = P3.subn(NEW3, t); t, b = P2.subn("", t)
    assert a + c == n0 and b == n0, (a, c, b, n0)
    t = re.sub(r"(?<=[a-z])\.,", ",", t)
    assert "hand's width" not in t and "dissolve" not in t and "Even inside a transition zone" not in t and "hazy and feathered" not in t
    assert _dups(t) <= d0 and t.count(".,") <= c0 and ".." not in t.replace("...", "") and " ," not in t
    return t


PRESETS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")

def main():
    apply = "--apply" in sys.argv
    files = sorted(glob.glob(os.path.join(PRESETS_DIR, "*.json")))
    changed = collections.Counter(); failed = []; skipped_nofield = 0
    for path in files:
        try:
            with open(path, "r", encoding="utf-8-sig") as f:
                d = json.load(f)
        except Exception:
            continue
        if not isinstance(d, dict) or not isinstance(d.get("prompt"), str): skipped_nofield += 1; continue
        if "hazy and feathered" not in d["prompt"]: continue
        try:
            new = interlock(d["prompt"])
        except AssertionError as e:
            failed.append((os.path.basename(path), str(e))); continue
        changed[d.get("category", "?")] += 1
        if apply:
            d["prompt"] = new
            if isinstance(d.get("meta"), dict): d["meta"]["boundary"] = "interlock-v1"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(d, f, ensure_ascii=False, indent=2)
    total = sum(changed.values())
    print(("적용 완료" if apply else "시험 실행(파일은 안 바뀜)") + f": 교체 대상 {total}개")
    for c in sorted(changed): print(f"  {c}: {changed[c]}개")
    if failed:
        print(f"실패 {len(failed)}개 (안 건드림):")
        for n, e in failed[:20]: print("  ", n, e)
    else:
        print("실패 0개")

if __name__ == "__main__":
    main()
