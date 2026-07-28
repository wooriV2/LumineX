import json, glob
for f in sorted(glob.glob("presets/ksf_bp_*.json")):
    d = json.loads(open(f, encoding="utf-8-sig").read())
    key = f.split("\\")[-1][:-5]
    txt = d.get("outfit") or d.get("prompt") or ""
    env = d.get("environment", "")
    print(f"=== {key}  [{','.join(sorted(d))}]")
    print(f"  TAG : {d.get('tag') or d.get('name') or '-'}")
    print(f"  OUT : {txt[:220]}")
    print(f"  ENV : {env[:100]}")
    print()
