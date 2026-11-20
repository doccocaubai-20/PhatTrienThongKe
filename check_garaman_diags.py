import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\PTTK\xml_export_GaraMan-De26\project.xml")
root = tree.getroot()
ns = {"vp": "http://www.visual-paradigm.com/product/vpuml/modelexporter"}
diagrams = root.find("vp:Diagrams", ns)

for i, d in enumerate(diagrams):
    name = d.get("name")
    dtype = d.get("diagramType")
    shapes = d.find("vp:Shapes", ns)
    s_cnt = len(shapes) if shapes is not None else 0
    print(f"{i+1:2d}. [{dtype:20s}] {name:35s}: {s_cnt:3d} shapes")
