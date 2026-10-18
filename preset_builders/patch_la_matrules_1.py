# -*- coding: utf-8 -*-
r"""
소재 몸(몸 자체가 석재·목재·신소재) 번들에 새 소재 규칙을 '제자리'로 적용한다.
  - 몸에 금 1곳 + 깨진 곳 1~2곳(가슴 제외, 상·하체 분산, 속 소재 노출)
  - 얼굴·귀·목만 실제 피부, 나머지(어깨·가슴·배꼽 있는 배·팔·손·다리·발목)는 재질
  - 신발은 실제 가죽(펌프스·샌들), 손이 낮은 포즈, 배꼽 장식(펜던트 벨리 체인) 제거
  - 몸을 덮는 문장은 긍정형으로, 그룹은 인물 줄을 나눔
대상(presets/): la_wood2_* la_stone2_* la_wsmix_* la_mixedstone_* la_mixedwood_*  (이미 Cracks 줄이 있으면 건너뜀)
기존 파일의 현재 프롬프트를 읽어 바꾸므로 이후에 적용된 다른 패치(신발 C 등)는 그대로 유지된다. 번들 JSON은 필요 없다.

사용법 (PowerShell, 레포 루트에서):
  $env:PYTHONUTF8="1"
  python preset_builders\patch_la_matrules_1.py
"""
import glob, json, os, sys, zlib
import re, random
UP = ["her left shoulder", "her right shoulder", "her left upper arm", "her right upper arm", "her belly", "her left forearm", "her right forearm"]
LOW = ["her left hip", "her right hip", "her left thigh", "her right thigh", "her left calf", "her right calf"]
INN = [("porcelain", "raw unglazed pale-grey clay with a dull chalky surface"),
       ("cobalt", "rough frosted milky-white glass with a dull sandblasted surface"),
       ("bronze", "raw reddish-orange cast metal with a rough surface"),
       ("tiger's eye", "dull raw golden-brown stone with a rough splintered fibrous grain, much duller than the polished outside"),
       ("larimar", "dull raw pale grey-blue stone with a rough chalky surface, much duller than the polished outside"),
       ("chrysoprase", "dull raw pale grey-green stone with a rough chalky surface, much duller than the polished outside"),
       ("moonstone", "dull raw milky grey-white stone with a rough chalky surface, much duller than the polished outside"),
       ("unakite", "dull raw grey-green stone with a rough chalky surface, much duller than the polished outside"),
       ("rhodochrosite", "dull raw pale pink-grey stone with a rough chalky surface, much duller than the polished outside"),
       ("agate", "dull raw pale grey stone with a rough chalky surface, much duller than the polished outside"),
       ("travertine", "raw rough beige porous stone with a coarse pitted surface and no polish"),
       ("azurite", "dull raw grey-blue stone with a rough chalky surface, much duller than the polished outside"),
       ("lava", "raw dull grey-brown rock with a rough pitted surface"),
       ("amber", "dull raw dark-brown resin with a rough unpolished surface"),
       ("ice", "rough cloudy white ice with a dull frosted surface"),
       ("sodalite", "dull raw grey-blue stone with a rough chalky surface, much duller than the polished outside"),
       ("marble", "raw rough grey-white stone with a coarse crystalline grain and no polish"),
       ("granite", "raw rough dull grey stone with a coarse speckled grain and no polish"),
       ("jade", "dull raw grey-green stone with a rough waxy surface, much duller than the polished jade outside"),
       ("lapis", "dull raw grey-blue stone with a rough chalky surface, much duller than the polished outside"),
       ("malachite", "dull raw dark-green stone with a rough chalky surface, much duller than the polished outside"),
       ("rhodonite", "dull raw pale pink-grey stone with a rough chalky surface, much duller than the polished outside"),
       ("onyx", "dull raw dark grey stone with a rough chalky surface, much duller than the polished outside"),
       ("labradorite", "dull raw grey stone with a rough chalky surface, much duller than the polished outside"),
       ("turquoise", "dull raw pale chalky blue-grey stone with a rough surface, much duller than the polished outside"),
       ("carnelian", "dull raw pale orange-brown stone with a rough chalky surface, much duller than the polished outside"),
       ("wood", "pale raw fresh wood with a rough splintered grain, much lighter than the dark polished outside")]
POSES = ["one hand resting on her hip, the other hanging relaxed at her side, weight on one leg",
 "both hands resting on her thighs, leaning slightly forward, one knee bent",
 "one hand lightly holding the opposite wrist low in front of her hips, standing tall with her chin lifted",
 "walking mid-stride toward the camera, both arms swinging naturally at her sides",
 "standing with both arms relaxed at her sides, palms turned slightly forward, head tilted a little",
 "one hand trailing along her thigh, the other behind her back, hip tilted",
 "both hands clasped behind her lower back, shoulders back, one foot crossed in front of the other",
 "one hand on her hip, the other extended low to the side with the fingers spread",
 "one leg crossed in front of the other, both hands hanging loosely at her sides",
 "turned away from the camera, looking back over her shoulder, one hand brushing her hip, the other hanging down",
 "wide power stance, both fists lightly closed at her sides, chin up",
 "both hands on her waist, elbows flared out to the sides, chin lifted",
 "classical contrapposto stance, weight on one leg, one hand holding the other forearm low in front of her hips",
 "both arms slightly open away from her body, palms turned up, relaxed shoulders",
 "one hand resting on her lower back, the other hanging down, back gently arched"]
SHOES = ["ankle-strap platform stiletto pumps in glossy black patent leather", "strappy platform stiletto sandals in red leather",
         "pointed platform stiletto pumps in black leather", "peep-toe platform stiletto pumps in cream white leather",
         "strappy platform stiletto sandals in tan leather", "platform stiletto pumps in nude leather"]
POS = [
 (r"covering EVERY inch of skin from neck to ankle WITHOUT EXCEPTION, both legs FULLY covered to ankles, NO bare skin below neck ANYWHERE", "wrapping her whole body from the collarbones to the ankles, both legs carved all the way down to the ankles"),
 (r"this is not a garment, (?:not jewelry, )?not a printed pattern, this is", "this is"),
 (r", nothing lying flat", ", every section standing proud of the next"),
 (r"across the full torso both legs neck to ankle", "across the full torso and both legs down to the ankles"),
 (r", NO airbrush NO gradient wash, NO flat printed surface anywhere", ", with a deep three-dimensional carved surface"),
]
def fix(p, labs, rr, kinds, info=None):
    out = p
    for lab, kd in zip(labs, kinds):
        male = (kd == 'M'); pr = 'his' if male else 'her'; Pr = pr.capitalize(); bust = 'chest' if male else 'bust'
        m = re.search(rf"^{lab} Body Art: (full body (.*?) (?:fused directly|carved directly)[^\n]*)$", out, re.M)
        if not m: continue
        desc = m.group(2); sp = desc.replace("polished ", "")
        inner = next((v for k, v in INN if k in desc), None); assert inner, desc
        line = m.group(0)
        for pat, rep in POS:
            line, k = re.subn(pat, rep.replace('her whole', pr + ' whole'), line, count=1); assert k == 1, pat
        line, k = re.subn(r"(?:Her|His) face stays real living skin and the .*? ends cleanly at the neck\.",
            f"{Pr} face and ears are real living skin, and {pr} neck, from under the jaw down to the base of the neck, is bare real skin with visible pores and a soft natural sheen; the carved body starts exactly at the base of the neck, and {pr} shoulders, chest, belly with its navel, arms, hands, wrists, legs and ankles are all carved {sp}.", line); assert k == 1
        nu, nlow = rr.choice([(1, 1), (2, 1), (1, 2)]); nd = nu + nlow
        parts = rr.sample(UP, nu) + rr.sample(LOW, nd - nu); rr.shuffle(parts)
        if male: parts = [x.replace('her ', 'his ') for x in parts]
        if nd == 2: where = f"one bold, clearly visible crack running across {parts[0]}, and one chipped-off piece at {parts[1]}"; cnt = "two"
        else: where = f"one bold, clearly visible crack running across {parts[0]}, and two chipped-off pieces, one at {parts[1]} and one at {parts[2]}"; cnt = "three"
        fin = 'unbroken and whole' if 'lava' in desc else 'smooth, polished and whole'
        crack = (f"{lab} Cracks: the {sp} body shows weathering in only {cnt} places: {where}, where the broken edge reveals the {inner} inside. "
                 f"Everywhere else, including {pr} {bust}, the {sp} is {fin}, and {pr} face, ears and neck are living skin.")
        out = out.replace(m.group(0), line + "\n\n" + crack, 1)
        mp = re.search(rf"^{lab} Pose: .*$", out, re.M); out = out.replace(mp.group(0), f"{lab} Pose: " + (rr.choice(POSES).replace("her ", "his ") if male else rr.choice(POSES)) + ".", 1)
        mf = re.search(rf"^{lab} Footwear: .*$", out, re.M); assert "carved from the same" in mf.group(0)
        if "combat boots" in mf.group(0):
            ft = f"{lab} Footwear: Extreme platform combat boots in black leather, the thick platform soles rising far higher than {pr} ankle bone, at least three times the thickness of an ordinary sole, with {pr} legs and ankles staying solid carved {sp} right down to the boots."
        else:
            ft = f"{lab} Footwear: Extreme {rr.choice(SHOES)}, each with a razor-thin tapered heel a full forty inches tall and a twelve-inch hidden front platform, with {pr} legs and ankles staying solid carved {sp} right down to the shoes."
        out = out.replace(mf.group(0), ft, 1)
        out = out.replace("the soles of the boots", "the soles of the shoes")
        meta = (lab, sp, nd, [x.replace('her ', '').replace('his ', '') for x in parts])
        if info is not None: info.append(meta)
    return out

import zlib as _zl
AXFIX_INFO = []
def axis_fix(p, kinds):
    labs = re.findall(r"^([A-Z]+(?: [A-Z]+)*): ONE real adult", p, re.M)
    assert len(labs) == len(kinds), (labs, kinds)
    info = []
    q = fix(p, labs, random.Random(_zl.crc32(p.encode())), kinds, info)
    assert not re.search(r"[가-힣]", q) and not re.search(r"\b(\w+) \1\b", q), re.findall(r"\b(\w+) \1\b", q)
    AXFIX_INFO.append(info)
    return q

JREP = ["thick polished gold bangles stacked on both wrists", "sculpted gold armbands high on both upper arms", "a fine gold chain looped around her thigh above the knee", "heavy gold rings on every finger"]
NV = "a gold belly chain with a small pendant at her navel"
def legacy_fix(p):
    lines = p.split("\n"); info = []
    rr_seed = zlib.crc32(p.encode())
    pfs = []
    for i, l in enumerate(lines):
        m = re.match(r"^(#\d+: )?.*?full body (.*?) (?:fused|carved) directly", l)
        if m and "Pose:" in l: pfs.append((m.group(1) or "", i, m.group(2)))
    assert pfs, "no material person"
    for pf, bi, desc in pfs:
        rr = random.Random(rr_seed + len(pf) * 7 + bi)
        sp = desc.replace("polished ", "")
        inner = next((v for k, v in INN if k in desc), None); assert inner, desc
        line = lines[bi]
        for pat, rep in POS:
            line, k = re.subn(pat, rep, line, count=1); assert k == 1, pat
        mp = re.search(r"Pose: (.*?)( — most extreme [^\n]*)?$", line); assert mp
        line = line.replace(mp.group(0), f"Pose: {rr.choice(POSES)}{mp.group(2) or ''}", 1)
        lines[bi] = line
        nu, nlow = rr.choice([(1, 1), (2, 1), (1, 2)]); nd = nu + nlow
        parts = rr.sample(UP, nu) + rr.sample(LOW, nd - nu); rr.shuffle(parts)
        if nd == 2: where = f"one bold, clearly visible crack running across {parts[0]}, and one chipped-off piece at {parts[1]}"; cnt = "two"
        else: where = f"one bold, clearly visible crack running across {parts[0]}, and two chipped-off pieces, one at {parts[1]} and one at {parts[2]}"; cnt = "three"
        fin = 'unbroken and whole' if 'lava' in desc else 'smooth, polished and whole'
        crack = (f"{pf}Cracks: the {sp} body shows weathering in only {cnt} places: {where}, where the broken edge reveals the {inner} inside. "
                 f"Everywhere else, including her bust, the {sp} is {fin}, and her face, ears and neck are living skin.")
        for j, l in enumerate(lines):
            if l.startswith(pf + "Footwear:") and (pf or not l.startswith("#")):
                m_ = re.match(r"^(#\d+: )?Footwear: (heels of the most absurdly extreme height imaginable, )(.+?) carved from the same [^,]+(, each with .*)$", l); assert m_, l[:160]
                lines[j] = crack + "\n" + f"{pf}Footwear: {m_.group(2)}{rr.choice(SHOES)}{m_.group(4)[:-1]}, with her legs and ankles staying solid carved {sp} right down to the shoes."
                break
        else: raise AssertionError("footwear")
        for j, l in enumerate(lines):
            if l.startswith(pf + "Face:") and (pf or not l.startswith("#")):
                assert "her face and ears are NOT carved — they are real living flesh" in l
                l = l.replace("her face and ears are NOT carved — they are real living flesh", "her face, ears and entire neck are real living flesh", 1)
                NK = f"Her neck, from under the jaw down to the base of the neck, is bare real skin with visible pores and a soft natural sheen; the carved body starts exactly at the base of the neck, and her shoulders, chest, belly with its navel, arms, hands, wrists, legs and ankles are all carved {sp}."
                if pf:
                    lines[j] = l
                    bl = lines[bi]; k_ = bl.index(" Pose:"); lines[bi] = bl[:k_] + " " + NK + bl[k_:]
                else:
                    lines[j] = l.rstrip() + " " + NK
                break
        else: raise AssertionError("face")
        for j, l in enumerate(lines):
            if l.startswith(pf + "Jewelry:") and (pf or not l.startswith("#")) and NV in l:
                rep = next(x for x in JREP if x not in l)
                lines[j] = l.replace(NV, rep, 1); break
        info.append((pf, sp, nd, [x.replace("her ", "") for x in parts]))
    q = "\n".join(lines)
    q = q.replace("the soles of the boots", "the soles of the shoes")
    q = q.replace("zero bare skin anywhere from neck to ankle", "carved material everywhere from the collarbones to the ankles")
    q = q.replace("with NO bare untattooed skin visible anywhere, every element standing in true relief, nothing flat", "with the carved material covering every body from the collarbones to the shoes, shoulders, chest, arms and hands included, every element standing in true relief")
    assert NV not in q
    return q, info

def restructure_groups(q):
    out = q
    for m in list(re.finditer(r"^(#\d+: )(.*?) — (full body [^\n]*?)( Pose: [^\n]*)$", q, re.M)):
        pf, ident, body, pose = m.group(1), m.group(2), m.group(3), m.group(4).strip()
        cm = re.search(rf"^{re.escape(pf)}Cracks: [^\n]*\n", out, re.M); assert cm
        crack = cm.group(0).rstrip("\n"); out = out.replace(cm.group(0), "", 1)
        new = f"{pf}{ident}\n{pf}Body Art: {body}\n{crack}\n{pf}{pose}"
        assert m.group(0) in out
        out = out.replace(m.group(0), new, 1)
    return out
_legacy_fix_inner = legacy_fix
def legacy_fix(p):
    q, info = _legacy_fix_inner(p)
    if re.search(r"^#1: ", q, re.M): q = restructure_groups(q)
    return q, info


PRESETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "presets")
LEGACY = ("la_wood2_", "la_stone2_", "la_wsmix_")
AXIS = ("la_mixedstone_", "la_mixedwood_")
done = skipped = 0; fails = []
for path in sorted(glob.glob(os.path.join(PRESETS, "*.json"))):
    key = os.path.basename(path)[:-5]
    if not key.startswith(LEGACY + AXIS): continue
    with open(path, "r", encoding="utf-8-sig") as f: d = json.load(f)
    p = d["prompt"]
    if "Cracks:" in p: skipped += 1; continue
    try:
        q = legacy_fix(p)[0] if key.startswith(LEGACY) else axis_fix(p, d["meta"]["kinds"])
        assert not re.search(r"[가-힣]", q)
    except (AssertionError, KeyError, StopIteration) as e:
        fails.append((key, str(e)[:60])); continue
    d["prompt"] = q
    with open(path, "w", encoding="utf-8") as f: json.dump(d, f, ensure_ascii=False, indent=2)
    done += 1
print(f"변경 {done}개, 이미 적용됨 {skipped}개, 실패 {len(fails)}개")
for k, e in fails[:10]: print("  실패:", k, e)
