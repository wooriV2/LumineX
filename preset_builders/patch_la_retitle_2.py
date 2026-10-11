# -*- coding: utf-8 -*-
r"""
번호만 있던 시리즈(Core·Mixed·Pregnant·Maximalist 5종·Wax/Obsidian/Crystal/Scale)의 제목을 공통 틀로 바꿉니다.
등록된 프리셋 파일(presets/*.json)의 prompt·meta에서 항목을 뽑아 title만 교체합니다. 이미 새 제목이면 건너뜁니다. (여러 번 실행해도 안전)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_retitle_2.py --dry    # 수정 없이 개수만 확인
  python preset_builders\patch_la_retitle_2.py          # 실제 수정 (옛 제목은 preset_builders\retitle2_old_titles_backup.json 에 저장)
"""
import glob, json, os, sys
# -*- coding: utf-8 -*-
"""공통 제목 틀: [시리즈 인원 #번호] · 체형 · 재질 · 포즈 · 배경 · 메이크업 (길이 약 50~80자). 기존 번들(title+meta)에서 항목을 뽑아 새 제목 매핑을 만든다."""
import re, json, collections
CNT = {"Solo": "솔로", "Duo": "듀오", "Trio": "트리오", "Quartet": "쿼르텟", "Quintet": "퀸텟"}
CNT_KO = ("솔로", "듀오", "트리오", "쿼르텟", "퀸텟")
POSE_RULES = [
 (r"^seated.*(bench)", "벤치 앉기"), (r"^seated.*(stool)", "스툴 앉기"), (r"^seated.*(chair|armchair)", "의자 앉기"),
 (r"^seated.*(steps|stairs|flight)", "계단 앉기"), (r"^seated.*(ledge|wall)", "턱 앉기"), (r"^seated", "앉기"),
 (r"kneeling on one knee", "한쪽 무릎 꿇기"), (r"kneeling on both", "양 무릎 꿇기"), (r"^reclining", "기대어 눕기"),
 (r"walking away", "뒤돌아 걷기"), (r"walk|stride", "걷기"), (r"leaning", "기대기"),
 (r"back fully|^back to the camera|^back three|back three", "뒷모습"), (r"hip pop", "힙 팝"),
 (r"profile", "옆모습"), (r"hands pressed together", "기도 자세"), (r"arms raised|raised above her head|raised overhead", "양팔 들기"),
 (r"sweeping her hair|hair streaming", "머리 넘기기"), (r"framing (her own |the )?face", "얼굴 감싸기"),
 (r"jump", "점프"), (r"lung", "런지"), (r"arms crossed", "팔짱"), (r"clasped behind her head", "손 깍지"),
 (r"s-curve", "S라인"), (r"hands? on (her|the) (hips|waist)|on her hips|fists pressing", "손 허리"),
 (r"three-quarter", "3/4 각도"), (r"one hand on her waist", "손 허리")]
def pose_ko(p):
    q = p.lower()
    for rx, ko in POSE_RULES:
        if re.search(rx, q): return ko
    return "서 있기"
def uniq(L):
    o = []
    for x in L:
        if x and x not in o: o.append(x)
    return o
def agg(L):
    u = uniq(L)
    if len(u) <= 2: return " / ".join(u)
    return f"{u[0]} 외 {len(u)-1}"
def mk_clean(s):
    s = s.strip()
    for _ in range(3):
        s = re.sub(r"\s*(아주 강함|강함|강화|포인트|\d단계)\s*$", "", s)
        s = re.sub(r"\((강화|포인트|강함)\)$", "", s).strip()
    return s
def mat_short(s):
    m = re.match(r"^([가-힣+]+)\s+(.*)$", s)
    if m:
        cat, var = m.group(1), m.group(2)
        w = var.split()
        return f"{cat} {' '.join(w[:2])}"
    return " ".join(s.split()[:3])
def parse(title):
    head, _, rest = title.partition(" (")
    rest = rest.rstrip(")")
    items = [x.strip() for x in re.split(r" · | ‖ ", rest)]
    return head, items
def build_head(head):
    for k, v in CNT.items(): head = re.sub(rf"\b{k}\b", v, head)
    return head
def material(items):
    ci = next((i for i, x in enumerate(items) if re.search(r"(솔로|듀오|트리오|쿼르텟|퀸텟)$", x)), None)
    if ci is None: return ""
    pre = re.sub(r"\s*(솔로|듀오|트리오|쿼르텟|퀸텟)$", "", items[ci]).strip()
    mats = []
    for x in items[ci + 1:]:
        if re.match(r"(앵글|조명|시간대|분위기|체형|인종|헤어|메이크업|배경|힐|신발|몸|극단)", x): break
        mats.append(x)
    mats = [m for m in mats if not any(m != n and n.startswith(m) for n in mats)]
    if len(mats) >= 2: mats = mats[-1:]
    mats = [y.strip() for m in mats for y in m.split(" / ")]
    if pre and "+" not in pre and pre != "새 재질" and not any(pre in m for m in mats): mats = [pre + " " + m for m in mats]
    mats = [mat_short(m) for m in mats]
    return agg(mats)
def retitle(p):
    head, items = parse(p["title"]); m = p["meta"]
    body = agg(m.get("physiques") or [x[3:] for x in items if x.startswith("체형 ")] and [y.strip() for x in items if x.startswith("체형 ") for y in x[3:].split(",")])
    mk = agg([mk_clean(x[5:]) for x in items if x.startswith("메이크업 ")])
    bg = next((re.sub(r"\(.*\)$", "", x[3:]) for x in items if x.startswith("배경 ")), "")
    poses = agg([pose_ko(x) for x in (m.get("poses") or []) if isinstance(x, str)]) if (m.get("group_size") or 1) == 1 else ""
    return " · ".join(x for x in [build_head(head), body, material(items), poses, bg, mk] if x)
def retitle_tank(p):
    head, items = parse(p["title"]); m = p["meta"]
    fills = "/".join(m["fills"]); cont = agg([c for c in m["contents"] if c])
    mk = agg([mk_clean(y) for x in items if x.startswith("메이크업 ") for y in x[5:].split(" / ")])
    kind = "듀얼바디 L3" if m["frame"] == "full" else "프레임 힙컷"
    return " · ".join(x for x in [head, kind, fills, "USSBBW", "수조" + ("+" + cont if cont else ""), mk] if x)

# -*- coding: utf-8 -*-
"""번호만 있던 시리즈(Core·Maximalist·Wax/Crystal 계열·Mixed·Pregnant·Mix3) 제목 개편: meta.composition 또는 프롬프트에서 항목을 뽑는다."""
CNT2 = {"Solo": "솔로", "Duo": "듀오", "Trio": "트리오", "Quartet": "쿼르텟", "Quintet": "퀸텟", "Sextet": "6인", "Septet": "7인", "Octet": "8인", "Nonet": "9인", "Decet": "10인"}
def head2(h):
    h = re.sub(r"\b(\d+)-Woman\b", r"\1인", h)
    for k, v in CNT2.items(): h = re.sub(rf"\b{k}\b", v, h)
    return h
def short(s, n=4): return " ".join(s.split()[:n])
def join(parts): return " · ".join(x for x in parts if x)
def core(p):
    comp = p["meta"].get("composition") or []
    rows = [c.split("/") for c in comp]
    rows = [r for r in rows if len(r) >= 3]
    pat = agg([short(r[2]) for r in rows])
    if len(rows) >= 6: return join([head2(p["title"]), pat])
    return join([head2(p["title"]), agg([r[1] for r in rows]), pat, agg([r[0] for r in rows])])
def mixed(p):
    comp = p["meta"].get("composition") or []
    rows = [c.split("·") for c in comp]
    rows = [r for r in rows if len(r) >= 3]
    pat = agg([short(r[2]) for r in rows])
    if len(rows) >= 6: return join([head2(p["title"]), pat])
    return join([head2(p["title"]), agg([r[1] for r in rows]), pat])
def preg(p):
    comp = p["meta"].get("composition") or []
    rows = [c.split("/") for c in comp]
    rows = [r for r in rows if len(r) >= 2]
    pat = agg([short(r[1]) for r in rows])
    if len(rows) >= 6: return join([head2(p["title"]), pat])
    return join([head2(p["title"]), agg([r[0] for r in rows]), pat])
def maxi(p):
    t = p["prompt"]
    body = agg([x.strip() for x in re.findall(r",\s*([A-Za-z][A-Za-z \-]*?) physique THE MOST EXTREME", t)])
    def _m(x):
        x = x.strip()
        if x.startswith("applied ") and x.endswith(" leaf"): return "금박 " + x[8:-5].title()
        return "스테인드글라스" if x == "stained glass" else short(x)
    mot = agg([_m(x) for x in re.findall(r"full body (.*?) (?:covering|flowing|clusters|growing|set directly|erupting)", t)] or [""])
    pose = ""
    if p["meta"].get("group_size", 1) == 1:
        ps = re.findall(r"Pose: ([^.\n—]*)", t); pose = agg([pose_ko(x) for x in ps]) if ps else ""
    n = p["meta"].get("group_size", 1)
    if n >= 6: return join([head2(p["title"]), mot])
    return join([head2(p["title"]), body, mot, pose])
def mix3(p):
    h = p["title"]; m = re.match(r"^(\w+) #(\d+) \((.*)\)$", h)
    n = p["meta"]["group_size"]
    return join([f"Mix3 고정조합 {n}인 #{m.group(2)}" if m else head2(h), m.group(3).replace("+", " / ") if m else ""])


OLD = re.compile(r"^(Core|Mixed|Pregnant|Irezumi|UV Neon|Uvneon|Stained Glass|Stainedglass|Gold Leaf|Goldleaf|Botanical|Wax|Obsidian|Crystal|Scale) (Solo|Duo|Trio|Quartet|Quintet|Sextet|Septet|Octet|Nonet|Decet|\d+-Woman) #\d+( \(.*\))?$")
def pick(p):
    t = p.get("title", ""); m = p.get("meta") or {}
    if not isinstance(m, dict) or not OLD.match(t) or " · " in t: return None
    head = t.split(" ")[0]
    if head == "Core" and m.get("composition"): return core
    if head == "Mixed" and m.get("composition"): return mixed
    if head == "Pregnant" and m.get("composition"): return preg
    if head in ("Irezumi", "UV", "Uvneon", "Stained", "Stainedglass", "Gold", "Goldleaf", "Botanical", "Wax", "Obsidian", "Crystal", "Scale") and "composition" not in m: return maxi
    return None

def main():
    dry = "--dry" in sys.argv
    here = os.path.dirname(os.path.abspath(__file__))
    pdir = os.path.join(here, "..", "presets"); bpath = os.path.join(here, "retitle2_old_titles_backup.json")
    old = json.load(open(bpath, encoding="utf-8")) if os.path.exists(bpath) else {}
    changed = skipped = 0; byhead = {}
    for path in sorted(glob.glob(os.path.join(pdir, "la_*.json"))):
        d = json.load(open(path, encoding="utf-8")); f = pick(d)
        if f is None: skipped += 1; continue
        new = f(d)
        if not new or new == d["title"]: skipped += 1; continue
        changed += 1; h = d["title"].split(" ")[0]; byhead[h] = byhead.get(h, 0) + 1
        if not dry:
            old.setdefault(os.path.basename(path)[:-5], d["title"]); d["title"] = new
            json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if not dry and changed: json.dump(old, open(bpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(("[DRY] " if dry else "") + f"제목 변경 {changed}개 / 건너뜀 {skipped}개")
    for h in sorted(byhead): print(f"  {h}: {byhead[h]}개")

if __name__ == "__main__":
    main()
