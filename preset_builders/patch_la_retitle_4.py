# -*- coding: utf-8 -*-
r"""
Face Sculpt 5종 1,202개의 제목을 얼굴 컷용 틀로 교체합니다. 프롬프트·키·카테고리·메타는 건드리지 않습니다.
  틀(1인): 시리즈 #번호 · 국가 나이 · 표정 · 눈·입술 대표 축 · 턱 · 메이크업 · 피어싱 · 귀 · 배경
  틀(그룹): 시리즈 N인 #번호 · 대표 축들 · 귀 · 배경
제목에서 빠지는 항목(프롬프트·메타에는 그대로 있음): 코, 정면/각도, 눈썹 대용, 헤나, 스티커, 렌즈, 테마·슬롯·치아·피부톤, 메이크업 꼬리표
이미 새 제목이면 건너뜁니다. (여러 번 실행해도 안전)

대상: la_facesculpt_ (기본 300 / Group 140 / Mixed-Age 300 / Same-Type 162 / Silverfox 300 = 1,202개)

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_retitle_4.py --dry     # 수정 없이 개수와 예시 확인
  python preset_builders\patch_la_retitle_4.py           # 실제 수정 (옛 제목은 preset_builders\retitle4_old_titles_backup.json 에 저장)
  python preset_builders\patch_la_retitle_4.py --undo    # 되돌리기 (백업 기준)
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

OLD4 = re.compile(r"^Face Sculpt( Silverfox| Mixed-Age| Group| Same-Type)? #\d+ \(")
AGE_POS = {"early": "초", "mid": "중", "late": "후"}
def age_ko(s):
    m = re.match(r"^(.*?)\((early|mid|late) (\d+)s\)$", s)
    if m:
        base, pos, n = m.groups()
        if re.search(r"\d+대", base): return base.strip()
        return f"{base.strip()} {n}대 {AGE_POS[pos]}"
    s2 = strip_par(s) or s
    return "원래 나이" if s2 == "유형" else s2
def ear_short(x):
    if x.startswith("대형 귀걸이 "): return x[len("대형 귀걸이 "):]
    if x.startswith("귀걸이+"): return "귀걸이+추 " + re.sub(r"^귀걸이\+혼합 금속 추 \d+개\s*", "", x)
    if x.startswith("혼합 금속 추"): return "귀 금속 추"
    if x.startswith("귀 추"): return "귀 철 추"
    return x
def ear_label(forms):
    has_w = any("추" in x for x in forms); has_e = any("추" not in x for x in forms)
    return "추+귀걸이" if (has_w and has_e) else ("추" if has_w else "귀걸이")
def stars_txt(stars, n):
    parts = [s.strip() for s in stars]
    if len(set(parts)) == 1 and n >= 2 and "(" not in parts[0]: return ""
    pre = {p.split("(")[0].strip() for p in parts}
    if len(pre) == 1 and all("(" in p for p in parts): parts = [re.search(r"\((.*)\)", p).group(1) for p in parts]
    return " + ".join(parts) if len(parts) <= 3 else " + ".join(parts[:3]) + f" 외 {len(parts)-3}"
def retitle4(d):
    t = d["title"]; m = d["meta"]; fmt = m.get("format")
    head, items = parse(t)
    if fmt == "face-sculpt":
        series = head.split(" #")[0]; num = head.split(" #")[1]
        nat, age, expr, star = items[0], age_ko(items[1]), items[2], items[3]
        jaw = next((x for x in items[4:] if re.search(r"턱$|^V라인$|베이비 페이스$", x)), "")
        mk = next((("메이크업 없음" if x == "메이크업 없음" else mk_clean(x[5:])) for x in items if x.startswith("메이크업 ")), "")
        if not mk and any(x == "유형 고유 메이크업" for x in items): mk = "유형 고유 메이크업"
        pc = next((x for x in items if re.match(r"^P\d+$", x)), "")
        ear = next((ear_short(x) for x in items if re.match(r"^(대형 귀걸이 |혼합 금속 추|귀 추|귀걸이\+)", x)), "")
        bg = next((bg_clean(x[3:]) for x in items if x.startswith("배경 ")), "")
        return join([f"{series} #{num}", f"{nat} {age}", expr, star, jaw, mk, pc, ear, bg])
    series, num = head.split(" #")
    bg = next((bg_clean(x[3:]) for x in items if x.startswith("배경 ")), "")
    ears = next((x[2:] for x in items if x.startswith("귀 ")), "")
    forms = [re.sub(r"\(.*?\)", "", e).strip() for e in ears.split(" / ")] if ears else []
    el = ("귀 " + ear_label(forms)) if forms else ""
    if fmt == "face-sculpt-group":
        n = items[0]; stars = items[1]
        sp = [x.strip() for x in stars.split(" + ")]
        return join([f"{series} {n} #{num}", stars_txt(sp, len(sp)), el, bg])
    gt = items[0]; mm = re.match(r"^(.*?)\s*(\d+인)$", gt); gname, n = mm.group(1), mm.group(2)
    sp = [x.strip() for x in items[1].split(" + ")]
    return join([f"{series.replace('Same-Type', '동종')} {n} #{num}", gname, stars_txt(sp, len(sp)), el, bg])

PREFIXES = ("la_facesculpt_",); OLD = OLD4; RETITLE = retitle4; BACKUP_NAME = "retitle4_old_titles_backup.json"

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
