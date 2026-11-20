import docx, zipfile, io, re

doc_path = r'C:\Users\admin\Documents\PTTK\Bao_Cao_PTTK_GaraMan_De26.docx'
doc = docx.Document(doc_path)
p = doc.paragraphs[329]
xml = p._element.xml
m = re.search(r'r:embed="([^"]+)"', xml)
if m:
    rid = m.group(1)
    target = doc.part.rels[rid].target_ref
    with zipfile.ZipFile(doc_path) as z:
        img_bytes = z.read('word/' + target)
    with open('extracted_p329_activity.png', 'wb') as f:
        f.write(img_bytes)
    print('Saved extracted_p329_activity.png, size:', len(img_bytes))
