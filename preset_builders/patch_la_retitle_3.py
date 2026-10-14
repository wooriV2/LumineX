# -*- coding: utf-8 -*-
r"""
제목 규칙(시리즈 인원 #번호 · 체형 · 재질 · (솔로만 포즈) · 배경 · 메이크업)을 빠뜨린 새 번들 390개의 제목만 교체합니다.
프롬프트·키·카테고리·메타는 건드리지 않습니다. 이미 새 제목이면 건너뜁니다. (여러 번 실행해도 안전)

대상: la_automaton_ / la_edible_ / la_dolljoint_(솔로 60 + 듀오 30) / la_nebula_ / la_lava_ / la_brick_  (합계 390개)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_retitle_3.py --dry     # 수정 없이 개수와 예시 확인
  python preset_builders\patch_la_retitle_3.py           # 실제 수정 (옛 제목은 preset_builders\retitle3_old_titles_backup.json 에 저장)
  python preset_builders\patch_la_retitle_3.py --undo    # 되돌리기 (백업 기준)
"""
import glob, json, os, sys, re
import re
CNT = {"Solo": "솔로", "Duo": "듀오"}
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
def parse(title):
    head, _, rest = title.partition(" (")
    rest = rest.rstrip(")")
    return head, [x.strip() for x in re.split(r" · | ‖ ", rest) if x.strip()]
def strip_par(s): return re.sub(r"\(.*?\)", "", s).strip()
def bg_clean(s):
    s = strip_par(s)
    return re.sub(r"^(실내|실외) ", "", s)
def join(parts): return " · ".join(x for x in parts if x)

PREFIX3 = ("la_automaton_", "la_edible_", "la_dolljoint_", "la_nebula_", "la_lava_", "la_brick_")
OLD3 = re.compile(r"^(Automaton|Edible|DollJoint|Nebula|Lava|Brick) (Solo|Duo) #\d+ \(")
def retitle3(d):
    t = d["title"]; m = d["meta"]
    head, items = parse(t)
    for k, v in CNT.items(): head = re.sub(rf"\b{k}\b", v, head)
    body = agg(m.get("physiques") or [])
    if m.get("variants"): mat = " + ".join(v.split(" · ")[0] for v in m["variants"])
    else: mat = (m.get("variant") or "").replace(" · ", " ")
    pose = ""
    if (m.get("group_size") or 1) == 1:
        ps = re.findall(r"Pose: ([^.\n—]*)", d["prompt"])
        pose = pose_ko(ps[0]) if ps else ""
    bg = next((strip_par(x[3:]) for x in items if x.startswith("배경 ")), "")
    mk = agg([mk_clean(x[5:]) for x in items if x.startswith("메이크업 ")])
    return join([head, body, mat, pose, bg, mk])

PREFIXES = PREFIX3; OLD = OLD3; RETITLE = retitle3; BACKUP_NAME = "retitle3_old_titles_backup.json"

def main():
    dry = "--dry" in sys.argv; undo = "--undo" in sys.argv
    here = os.path.dirname(os.path.abspath(__file__))
    pdir = os.path.join(here, "..", "presets"); bpath = os.path.join(here, BACKUP_NAME)
    old = json.load(open(bpath, encoding="utf-8")) if os.path.exists(bpath) else {}
    if undo:
        n = 0
        for key, title in old.items():
            path = os.path.join(pdir, key + ".json")
            if not os.path.exists(path): continue
            d = json.load(open(path, encoding="utf-8"))
            if d.get("title") != title:
                d["title"] = title; json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2); n += 1
        print(f"되돌림 {n}개 (백업 {len(old)}개 기준)"); return
    changed = skipped = failed = 0; byhead = {}; lens = []; samples = []; fails = []
    for path in sorted(glob.glob(os.path.join(pdir, "la_*.json"))):
        key = os.path.basename(path)[:-5]
        if not key.startswith(PREFIXES): continue
        d = json.load(open(path, encoding="utf-8")); t = d.get("title", "")
        if not OLD.match(t): skipped += 1; continue
        try: new = RETITLE(d)
        except Exception as e: failed += 1; fails.append(f"{key}: {e!r}"); continue
        if not new or new == t: skipped += 1; continue
        changed += 1; lens.append(len(new)); h = t.split(" #")[0]; byhead[h] = byhead.get(h, 0) + 1
        if len(samples) < 4 and (changed % 97 == 1 or changed == 1): samples.append((t, new))
        if not dry:
            old.setdefault(key, t); d["title"] = new
            json.dump(d, open(path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    if not dry and changed: json.dump(old, open(bpath, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(("[DRY] " if dry else "") + f"제목 변경 {changed}개 / 건너뜀 {skipped}개 / 해석 실패 {failed}개")
    for h in sorted(byhead): print(f"  {h}: {byhead[h]}개")
    if lens: print(f"  새 제목 길이: 평균 {sum(lens)//len(lens)}자 / 최대 {max(lens)}자")
    for a, b in samples[:3]: print("  전:", a, "\n  후:", b)
    for f in fails[:5]: print("  실패:", f)

if __name__ == "__main__":
    main()
