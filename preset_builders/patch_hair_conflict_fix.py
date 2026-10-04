# -*- coding: utf-8 -*-
r"""
등록된 la_* 프리셋의 "머리 묘사 충돌"을 점검하고(기본: 아무것도 바꾸지 않음) 필요하면 수정합니다.

문제: 메이크업 설명 48종 중 33종에 머리 묘사(예: "long black hair in fine neat braids")가 이미 들어 있는데,
      별도 헤어 문구("braided hair" 등)가 또 붙어서 같은 인물의 머리가 두 번, 서로 다르게 적혀 있습니다.

모드
  --mode remove  충돌하는 메이크업 속 머리 문장만 삭제 (머리 색은 지정되지 않은 채로 남음)
  (두 모드 모두: 메이크업 속 머리 문장과 별도 헤어 문구가 함께 있는 프리셋만 수정, 머리 묘사가 하나뿐인 프리셋은 그대로 둠)
  --mode reroll  위 삭제 + 구 헤어 문구(스타일만 있는 8종)를 새 축("{색상} hair styled in {스타일}", 30x31)으로 교체
                 (같은 프리셋 안의 모든 인물에게 적용, 키를 시드로 써서 재실행해도 결과가 같음)
옵션
  --apply        실제로 파일을 수정 (없으면 점검만 하고 샘플 5개를 보여줌)
  --include-tiered  core/hof_tier.py, core/sss_tier.py 에 올라 있는 프리셋도 수정 (기본은 건너뜀)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_hair_conflict_fix.py                    # 점검만(remove 기준)
  python preset_builders\patch_hair_conflict_fix.py --mode reroll      # 점검만(reroll 기준)
  python preset_builders\patch_hair_conflict_fix.py --mode reroll --apply
적용 후에는 git diff --stat 으로 변경 파일 수를 확인하고 커밋하세요.
"""
import argparse, glob, json, os, random, re, sys

CLAUSES = [
    "long black hair in twin tails tied with pink and black ribbons under a blunt fringe",
    "long black hair in twin tails with pink and black ribbons under a blunt fringe",
    "long pastel rainbow hair in twin tails crowded with colourful plastic clips",
    "glossy black hair braided and pinned into a low chignon with a red ribbon",
    "long black hair loosely tousled with a few strands across the face",
    "long pale-blonde hair in two thick braids and a braided crown",
    "long black hair in fine neat braids swept back from the face",
    "long light-brown hair in twin tails tied with pastel ribbons",
    "thick glossy dark-brown hair set in a high backcombed style",
    "huge voluminous light-brown curls with a big pink satin bow",
    "long voluminous dark-brown waves swept over one shoulder",
    "long light-brown hair in a thick braid over one shoulder",
    "long bleached blonde hair with sun-streaked highlights",
    "black hair in a high coiled updo with gold hairpins",
    "long dark-brown hair in an effortless tousled updo",
    "long dark-brown hair in glossy voluminous waves",
    "long bleached platinum hair with a neon streak",
    "long teased jet-black hair with silver streaks",
    "hair set in glossy voluminous old-film waves",
    "long braids piled into a high sculpted crown",
    "ribbons and tiny toys kept on the hair",
    "towering teased bleached-blonde hair",
    "long teased neon-pink and lime hair",
    "long teased neon pink and lime hair",
    "long straight platinum-blonde hair",
    "long voluminous honey-blonde waves",
    "long voluminous chestnut waves",
    "long straight jet-black hair",
    "long sleek chestnut waves",
    "long glossy black waves",
    "long sleek black waves",
    "long sleek black hair"
]
OLD_AXIS = ["curly", "wavy", "twin-tail", "braided", "elegant updo", "high ponytail", "sleek straight", "low bun"]
NEW_STYLES = [
    "sleek straight",
    "wavy",
    "curly",
    "high ponytail",
    "elegant updo",
    "braided",
    "low bun",
    "twin-tail",
    "a natural afro in a full rounded silhouette",
    "long locs gathered loosely",
    "cornrows braided tight against the scalp",
    "half-up, top section lifted with the length flowing loose below",
    "a short pixie cut",
    "a chin-length bob",
    "a low chignon knot at the nape",
    "an intricate fishtail braid",
    "a high top-knot bun",
    "a sleek wet-look slicked straight back",
    "two small space buns on top of the head",
    "many small bantu knots covering the scalp",
    "flat glossy finger waves styled close to the scalp",
    "tight zigzag crimped waves",
    "long thick box braids",
    "a classic French braid from the crown",
    "countless fine micro braids",
    "a layered tousled shag cut",
    "a layered wolf cut with curtain bangs",
    "a mohawk with volume along the centre of the scalp",
    "vintage victory rolls framing the face",
    "a crown braid wrapping around the head",
    "natural curls gathered into a high rounded puff"
]
NEW_COLORS = [
    "deep jet-black with a glossy sheen",
    "natural soft black",
    "deep dark brown",
    "warm chestnut-brown",
    "cool ash-brown",
    "rich chocolate-brown",
    "deep reddish mahogany-brown",
    "vivid copper-orange",
    "warm auburn red-brown",
    "soft strawberry-blonde",
    "warm honey-blonde",
    "bright golden-blonde",
    "icy platinum-blonde",
    "soft champagne-blonde",
    "sleek silver-grey",
    "cool ash-grey",
    "deep burgundy wine-red",
    "soft rose-gold",
    "dark roots fading smoothly into sun-kissed lighter ends (balayage)",
    "a distinct two-tone ombre with dark roots and a sharp transition to light ends",
    "soft pastel-pink",
    "soft pastel-lavender",
    "soft pastel-mint-green",
    "soft pastel-peach",
    "bold vivid electric-blue",
    "bold vivid violet-purple",
    "bold vivid magenta-pink",
    "bold vivid emerald-green",
    "bold vivid tangerine-orange",
    "pure icy-white"
]
PUNCT_RE = re.compile(r",\s*,|,\s*\.|\(\s*,")
OLD_RE = re.compile(r"(?<=, )(?:" + "|".join(re.escape(x) for x in OLD_AXIS) + r") hair(?=[,.])")
ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
PRESETS_DIR = os.path.join(ROOT, "presets")

def load_tiered():
    keys = set()
    for name in ("hof_tier.py", "sss_tier.py"):
        path = os.path.join(ROOT, "core", name)
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8-sig") as f:
                keys |= set(re.findall(r"[\"'](la_[A-Za-z0-9_]+)[\"']", f.read()))
    return keys

def remove_clauses(text):
    removed = 0
    for c in CLAUSES:
        n = text.count(c)
        if not n:
            continue
        t = text.replace(", " + c, "")
        if c in t:
            t = t.replace(c + ", ", "")
        removed += n
        text = t
    return text, removed

def reroll_axis(text, key):
    rng = random.Random(key)
    count = [0]
    def sub(_m):
        count[0] += 1
        return f"{rng.choice(NEW_COLORS)} hair styled in {rng.choice(NEW_STYLES)}"
    return OLD_RE.sub(sub, text), count[0]

def process(item, mode):
    """returns (new_prompt or None, info) ; None = 변경 없음/건너뜀"""
    p = item["prompt"]
    q, removed = remove_clauses(p)
    if not removed:
        return None, "해당없음"
    if not (OLD_RE.search(p) or "hair styled in" in p):
        return None, "헤어 문구 하나뿐(충돌 아님)"      # 머리 묘사가 이것 하나뿐이면 지우지 않음
    if len(PUNCT_RE.findall(q)) > len(PUNCT_RE.findall(p)):      # 삭제 때문에 새로 생긴 문장부호 이상만 거름
        return None, "문장부호 이상"
    replaced = 0
    if mode == "reroll":
        q, replaced = reroll_axis(q, item["key"])
    if "hair" not in q:
        return None, "머리 문구 없음"
    return q, {"removed": removed, "replaced": replaced}

def prefix_of(key):
    for pre in ("la_core_", "la_preg_", "la_mixedrand_", "la_mixed7_", "la_mixed_", "la_mix3_"):
        if key.startswith(pre):
            return pre
    return "_".join(key.split("_")[:2])

def snippet(before, after):
    for c in CLAUSES:
        i = before.find(c)
        if i >= 0:
            b = before[max(0, i - 70): i + len(c) + 130].replace("\n", " ")
            j = after.find(before[max(0, i - 40): i - 5]) if i > 40 else 0
            a = after[max(0, j): max(0, j) + len(b)].replace("\n", " ")
            return b, a
    return before[:200], after[:200]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--mode", choices=["remove", "reroll"], default="remove")
    ap.add_argument("--apply", action="store_true")
    ap.add_argument("--include-tiered", action="store_true")
    a = ap.parse_args()
    files = sorted(glob.glob(os.path.join(PRESETS_DIR, "la_*.json")))
    tiered = set() if a.include_tiered else load_tiered()
    if tiered:
        print(f"티어(HOF/SSS) 보유 la_* 키 {len(tiered)}개는 건너뜁니다 (포함하려면 --include-tiered)")
    stats, skipped, samples, changed = {}, {}, [], []
    for path in files:
        with open(path, "r", encoding="utf-8") as f:
            item = json.load(f)
        key = item.get("key", os.path.basename(path)[:-5])
        item["key"] = key
        pre = prefix_of(key)
        s = stats.setdefault(pre, [0, 0, 0])
        s[0] += 1
        if key in tiered:
            skipped["티어 보유"] = skipped.get("티어 보유", 0) + 1
            s[2] += 1
            continue
        newp, info = process(item, a.mode)
        if newp is None:
            if info != "해당없음":
                skipped[info] = skipped.get(info, 0) + 1
                s[2] += 1
            continue
        s[1] += 1
        changed.append((path, item, newp))
        if len(samples) < 5 and (not samples or pre not in [x[0] for x in samples]):
            samples.append((pre, key) + snippet(item["prompt"], newp))
    print(f"모드: {a.mode} | 대상 la_* 프리셋 {len(files)}개")
    print(f"{'접두어':<16}{'전체':>6}{'변경':>7}{'건너뜀':>8}")
    for pre, (tot, ch, sk) in sorted(stats.items()):
        print(f"{pre:<16}{tot:>6}{ch:>7}{sk:>8}")
    print(f"합계: 변경 대상 {len(changed)}개" + (f" | 건너뜀 사유 {skipped}" if skipped else ""))
    for pre, key, b, af in samples:
        print(f"\n[샘플] {key}\n  전: …{b}…\n  후: …{af}…")
    if not a.apply:
        print("\n(점검만 실행했습니다. 실제로 수정하려면 --apply 를 붙이세요.)")
        return
    for path, item, newp in changed:
        item["prompt"] = newp
        with open(path, "w", encoding="utf-8") as f:
            json.dump(item, f, ensure_ascii=False, indent=2)
    print(f"\n적용 완료: {len(changed)}개 파일 수정. git diff --stat 으로 확인 후 커밋하세요.")

if __name__ == "__main__":
    main()
