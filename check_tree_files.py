import os
import xml.etree.ElementTree as ET

treestates_dir = r"C:\Users\admin\AppData\Roaming\VisualParadigm\ws\.vpprefdata\treestates"
for f in os.listdir(treestates_dir):
    p = os.path.join(treestates_dir, f)
    if f.endswith('.xml') and f != 'ProjectTreeStateIndexing.xml':
        print(f"File: {f}")
        try:
            tree = ET.parse(p)
            for el in tree.getroot():
                print(f"  {el.tag}: {el.attrib} | {el.text}")
        except Exception as e:
            print("  Error:", e)
