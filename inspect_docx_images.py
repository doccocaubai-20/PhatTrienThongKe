import docx
import zipfile
import io
import re
from PIL import Image

doc_path = r'C:\Users\admin\Documents\PTTK\Bao_Cao_PTTK_GaraMan_De26.docx'
doc = docx.Document(doc_path)
with zipfile.ZipFile(doc_path) as z:
    for i in [315, 318, 321, 322, 325, 326]:
        p = doc.paragraphs[i]
        xml = p._element.xml
        m = re.search(r'r:embed="([^"]+)"', xml)
        if m:
            rid = m.group(1)
            target = doc.part.rels[rid].target_ref
            img_bytes = z.read('word/' + target)
            im = Image.open(io.BytesIO(img_bytes))
            print(f'Paragraph {i}: rel={rid}, target={target}, dimensions={im.size}, format={im.format}')
            # Save to disk to inspect if needed
            out_name = f"extracted_p{i}_{target.replace('/', '_')}"
            with open(out_name, 'wb') as f_out:
                f_out.write(img_bytes)
            print(f'   Saved to {out_name}')
