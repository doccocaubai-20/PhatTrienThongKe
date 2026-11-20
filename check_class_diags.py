import xml.etree.ElementTree as ET

tree = ET.parse(r"C:\Users\admin\Documents\flashcard\GaraMan-De26\chuan-hoa-final-xml\project.xml")
root = tree.getroot()
diagrams = root.find("Diagrams")

for i, d in enumerate(diagrams):
    if d.tag == "ClassDiagram":
        name = d.get("Name")
        shapes = d.find("Shapes")
        print(f"\n--- Diagram: {name} (Shapes: {len(shapes)}) ---")
        for s in list(shapes)[:5]:
            mid = s.get("Model")
            # find model element name
            model_elem = root.find(f".//Models//*[@Id='{mid}']") if mid else None
            elem_name = model_elem.get("Name") if model_elem is not None else "NoModel"
            print(f"   Shape: {s.tag}, ModelId: {mid}, ElemName: {elem_name}, X={s.get('X')}, Y={s.get('Y')}, W={s.get('Width')}, H={s.get('Height')}")
