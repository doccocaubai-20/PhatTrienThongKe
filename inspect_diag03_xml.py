import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\PTTK\xml_export_GaraMan-De26-Activity-Sequence\project.xml")
root = tree.getroot()
ns = {"vp": "http://www.visual-paradigm.com/product/vpuml/modelexporter"}
diagrams = root.find("vp:Diagrams", ns)

for d in diagrams:
    if d.get("name") == "03 - Lop chi tiet - Tim thong tin":
        print("Diagram tag:", d.tag)
        print("Diagram attribs:", d.attrib)
        shapes = d.find("vp:Shapes", ns)
        print("Shapes count:", len(shapes) if shapes is not None else 0)
        for s in list(shapes)[:3]:
            print("  Shape:", s.tag, s.attrib)
            for ch in s:
                print("    Child:", ch.tag.split("}")[-1], ch.attrib, ch.text)
        break
