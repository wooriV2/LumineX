import re

content = open('dashboard.py', encoding='utf-8').read()

# SS_TIER (SSS 제외)
ss = re.search(r'(?<!S)(SS_TIER\s*=\s*\{)([^}]+)(\})', content, re.DOTALL)
block = ss.group(2) if ss else ''

targets = ['uyuni_wet_silk', 'aurora_bare', 'antelope_light_sheer', 'lava_field_latex']
for p in targets:
    print(f"SS {p}: {p in block}")

# SSS_TIER
sss = re.search(r'SSS_TIER\s*=\s*\{([^}]+)\}', content, re.DOTALL)
sss_block = sss.group(1) if sss else ''
print(f"SSS body_paint_nude: {'body_paint_nude' in sss_block}")

count = len(re.findall(r'"[\w_]+"', block))
print(f"SS 총합: {count}개")
sss_count = len(re.findall(r'"[\w_]+"', sss_block))
print(f"SSS 총합: {sss_count}개")
