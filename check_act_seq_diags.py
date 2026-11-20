import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\PTTK\xml_export_GaraMan-De26-Activity-Sequence\project.xml")
root = tree.getroot()
ns = {"vp": "http://www.visual-paradigm.com/product/vpuml/modelexporter"}
diagrams = root.find("vp:Diagrams", ns)

print(f"Total diagrams: {len(diagrams)}")
for i, d in enumerate(diagrams):
    tag = d.tag.split("}")[-1]
    name = d.get("Name") or "(No Name)"
    shapes = d.find("vp:Shapes", ns)
    connectors = d.find("vp:Connectors", ns)
    s_cnt = len(shapes) if shapes is not None else 0
    c_cnt = len(connectors) if connectors is not None else 0
    dtype = d.get("DiagramType") or ""
    print(f"{i+1:2d}. [{dtype:20s}] {name:40s}: {s_cnt:3d} shapes, {c_cnt:3d} connectors")
