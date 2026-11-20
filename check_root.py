import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\PTTK\xml_export_GaraMan-De26-Activity-Sequence_PreFix\project.xml")
root = tree.getroot()
print("Root tag:", root.tag)
for child in root:
    print("Child tag:", child.tag, len(child))
