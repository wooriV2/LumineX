# diagnose_sss.py
FILE = "core/sss_tier.py"

with open(FILE, encoding="utf-8-sig") as f:
    lines = f.readlines()

total = len(lines)
print(f"총 줄 수: {total}")

# 905~920번 줄 확인 (SyntaxError 913번 근처)
print("\n[910~920줄]")
for i, l in enumerate(lines[909:920], start=910):
    print(f"{i}: {repr(l)}")

# 마지막 25줄
print("\n[마지막 25줄]")
for i, l in enumerate(lines[-25:], start=total-24):
    print(f"{i}: {repr(l)}")

# { } 개수
opens = sum(l.count("{") for l in lines)
closes = sum(l.count("}") for l in lines)
print(f"\n{{ 개수: {opens}, }} 개수: {closes}, 차이: {opens - closes}")
