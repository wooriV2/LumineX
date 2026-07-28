import ast, json, re, shutil, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

RENAME = {
 "ksf_bp_001": "ksf_void_superbbw_side_gold",
 "ksf_bp_002": "ksf_mideast_muscular_kneel_copper",
 "ksf_bp_003": "ksf_nordic_runway_botanical_goldpink",
 "ksf_bp_004": "ksf_brazilian_bubblebutt_rear_rosegold",
 "ksf_bp_005": "ksf_void_hourglass_frontal_cobalt",
 "ksf_bp_006": "ksf_russian_muscular_eagle_silver",
 "ksf_bp_007": "ksf_hungarian_hourglass_side_violet",
 "ksf_bp_009": "ksf_void_superbbw_globe_crimson",
 "ksf_bp_010": "ksf_void_superbbw_sumosquat_turquoise",
 "ksf_bp_016": "ksf_westafrican_hourglass_frontal_violet",
 "ksf_bp_018": "ksf_lebanese_runway_calligraphy_scarlet",
 "ksf_bp_021": "ksf_mongolian_bubblebutt_rear_turquoise",
 "ksf_bp_022": "ksf_ukrainian_superbbw_sunflower_sapphire",
 "ksf_bp_024": "ksf_iraqi_hourglass_ishtar_lapis",
 "ksf_bp_025": "ksf_serbian_muscular_serpent_neongreen",
 "ksf_bp_026": "ksf_void_superbbw_dragon_gold",
 "ksf_bp_028": "ksf_brazilian_superbbw_sumosquat_violet",
 "ksf_bp_029": "ksf_nigerian_superbbw_twist_cobalt",
 "ksf_bp_031": "ksf_void_superbbw_phoenix_crimson",
 "ksf_bp_032": "ksf_void_superbbw_serpent_emerald",
 "ksf_bp_033": "ksf_void_superbbw_mandala_rosegold",
 "ksf_bp_034": "ksf_void_superbbw_mohawk_cobalt",
 "ksf_bp_035": "ksf_void_superbbw_lotus_violet",
}
DELETE = ["ksf_bp_008"]

FAIL, LOG = [], []

# ── 1. 사전 점검
for old, new in RENAME.items():
    if not (ROOT / "presets" / f"{old}.json").exists():
        FAIL.append(f"원본 없음: {old}.json")
    if (ROOT / "presets" / f"{new}.json").exists():
        FAIL.append(f"대상 이미 존재: {new}.json")
if len(set(RENAME.values())) != len(RENAME):
    FAIL.append("새 이름 중복 있음")
if FAIL:
    print("[중단]"); [print("  " + f) for f in FAIL]; sys.exit(1)

# ── 2. JSON 리네임 + key 필드 갱신
for old, new in RENAME.items():
    src = ROOT / "presets" / f"{old}.json"
    d = json.loads(src.read_text(encoding="utf-8-sig"))
    if d.get("key") == old:
        d["key"] = new
    (ROOT / "presets" / f"{new}.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=2), encoding="utf-8")
    src.unlink()
    LOG.append(f"  {old} -> {new}")

# ── 3. 코드 3파일 갱신
for fname in ("core/hof_tier.py", "core/sss_tier.py", "core/presets_meta.py"):
    p = ROOT / fname
    if not p.exists(): continue
    raw = p.read_bytes()
    BOM = raw.startswith(b"\xef\xbb\xbf")
    src = raw.decode("utf-8-sig")
    orig = src

    for old, new in RENAME.items():
        src = src.replace(f'"{old}"', f'"{new}"').replace(f"'{old}'", f"'{new}'")

    for dead in DELETE:
        src = "\n".join(l for l in src.split("\n") if dead not in l)

    if src == orig:
        LOG.append(f"  [{fname}] 변경 없음"); continue

    try:
        ast.parse(src)
    except SyntaxError as e:
        FAIL.append(f"[{fname}] AST 실패: {e}"); continue

    shutil.copy2(p, p.with_suffix(".py.bak"))
    p.write_bytes((b"\xef\xbb\xbf" if BOM else b"") + src.encode("utf-8"))
    LOG.append(f"  [{fname}] 갱신")

print("\n".join(LOG))
if FAIL:
    print("\n[실패]"); [print("  " + f) for f in FAIL]
else:
    print(f"\nOK — {len(RENAME)}개 리네임, {len(DELETE)}개 키 제거")
