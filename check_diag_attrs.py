import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\PTTK\xml_export_GaraMan-De26-Activity-Sequence\project.xml")
root = tree.getroot()
ns = {"vp": "http://www.visual-paradigm.com/product/vpuml/modelexporter"}
diagrams = root.find("vp:Diagrams", ns)

d = diagrams[0]
print("Diagram 0 tag:", d.tag)
print("Diagram 0 attribs:", d.attrib)
for child in d:
    tag = child.tag.split("}")[-1]
    print("  Child:", tag, child.attrib, child.text[:50] if child.text else "")
