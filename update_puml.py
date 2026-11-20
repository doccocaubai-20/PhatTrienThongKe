with open('PHAN2_PHAN_TICH_YEU_CAU.md', 'r', encoding='utf-8') as f:
    md_content = f.read()

puml_section = md_content.split('## 6. TỔNG HỢP MÃ NGUỒN PLANTUML GIAI ĐOẠN 2 (NỘP FORM 2)')[1]

with open('PLANTUML_SUBMISSION.puml', 'r', encoding='utf-8') as f:
    full_puml = f.read()

p1_marker = "' ======================================================================================\n' PHẦN 2: GIAI ĐOẠN PHÂN TÍCH YÊU CẦU"
p1_part = full_puml.split(p1_marker)[0]

new_puml = p1_part + "' ======================================================================================\n' PHẦN 2: GIAI ĐOẠN PHÂN TÍCH YÊU CẦU (NỘP FORM 2)\n' Link Google Form 2: https://forms.gle/ciKQDmZntpPKuH4H7\n' ======================================================================================\n\n"

lines = puml_section.split('\n')
clean_lines = []
for line in lines:
    if line.startswith('### '):
        clean_lines.append("' --------------------------------------------------------------------------------------\n' " + line.replace('### ', '') + "\n' --------------------------------------------------------------------------------------")
    elif line.startswith('```'):
        continue
    else:
        clean_lines.append(line)

new_puml += '\n'.join(clean_lines).strip() + '\n'

with open('PLANTUML_SUBMISSION.puml', 'w', encoding='utf-8') as f:
    f.write(new_puml)

print('Updated PLANTUML_SUBMISSION.puml successfully!')
