# -*- coding: utf-8 -*-
import re

with open('PHAN2_PHAN_TICH_YEU_CAU.md', 'r', encoding='utf-8') as f:
    md_text = f.read()

sec6_text = md_text[md_text.find('## 6. TỔNG HỢP MÃ NGUỒN PLANTUML'):]
pattern = re.compile(r'### (6\.[1-7].*?)\n```plantuml\n(.*?)\n```', re.DOTALL)
matches = pattern.findall(sec6_text)
print('Found blocks in MD Section 6:', len(matches))

with open('PLANTUML_SUBMISSION.puml', 'r', encoding='utf-8') as f:
    orig_puml = f.read()

cutoff_target = "' PHẦN 2: GIAI ĐOẠN PHÂN TÍCH YÊU CẦU"
cutoff_idx = orig_puml.find(cutoff_target)
if cutoff_idx == -1:
    cutoff_target = "PHẦN 2: GIAI ĐOẠN PHÂN TÍCH YÊU CẦU"
    cutoff_idx = orig_puml.find(cutoff_target)

# Find start of comment block before cutoff_idx
hash_line_idx = orig_puml.rfind("'", 0, cutoff_idx)
line_start = orig_puml.rfind("\n", 0, hash_line_idx)
header_part1 = orig_puml[:line_start].strip() + "\n\n"

new_puml = header_part1
new_puml += "' " + "="*86 + "\n"
new_puml += "' PHẦN 2: GIAI ĐOẠN PHÂN TÍCH YÊU CẦU (NỘP FORM 2)\n"
new_puml += "' Link Google Form 2: https://forms.gle/ciKQDmZntpPKuH4H7\n"
new_puml += "' " + "="*86 + "\n\n"

for title, code in matches:
    new_puml += "' " + "-"*86 + "\n"
    new_puml += f"' {title}\n"
    new_puml += "' " + "-"*86 + "\n"
    new_puml += code.strip() + "\n\n"

with open('PLANTUML_SUBMISSION.puml', 'w', encoding='utf-8') as f:
    f.write(new_puml)

print('Updated PLANTUML_SUBMISSION.puml successfully!')
