import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\flashcard\GaraMan-De26\chuan-hoa-final-xml\project.xml")
root = tree.getroot()
diagrams = root.find("Diagrams")
print(f"Total diagrams: {len(diagrams)}")
for i, d in enumerate(diagrams):
    name = d.get("Name")
    shapes = d.find("Shapes")
    connectors = d.find("Connectors")
    s_cnt = len(shapes) if shapes is not None else 0
    c_cnt = len(connectors) if connectors is not None else 0
    print(f"{i+1}. [{d.tag}] {name}: {s_cnt} shapes, {c_cnt} connectors")
