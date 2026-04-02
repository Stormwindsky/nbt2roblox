import nbtlib
import xml.etree.ElementTree as ET
import sys
import uuid

def create_part(parent, name, x, y, z):
    part = ET.SubElement(parent, "Item",  attrib={"class": "Part", "referent": f"RBX{uuid.uuid4().hex.upper()}"})
    props = ET.SubElement(part, "Properties")
    ET.SubElement(props, "string", name="Name").text = name
    ET.SubElement(props, "bool", name="Anchored").text = "true"
    cframe = ET.SubElement(props, "CoordinateFrame", name="CFrame")
    ET.SubElement(cframe, "X").text = str(x * 4)
    ET.SubElement(cframe, "Y").text = str(y * 4)
    ET.SubElement(cframe, "Z").text = str(z * 4)
    for i in range(3):
        for j in range(3):
            ET.SubElement(cframe, f"R{i}{j}").text = "1" if i == j else "0"
    size = ET.SubElement(props, "Vector3", name="Size")
    ET.SubElement(size, "X").text = "4"
    ET.SubElement(size, "Y").text = "4"
    ET.SubElement(size, "Z").text = "4"

def convert(nbt_path, rbxmx_path):
    try:
        nbt_file = nbtlib.load(nbt_path)
        data = nbt_file.get("", nbt_file)
        roblox = ET.Element("roblox", {"version": "4"})
        model = ET.SubElement(roblox, "Item", attrib={"class": "Model"})
        ET.SubElement(ET.SubElement(model, "Properties"), "string", name="Name").text = "ImportMC"
        palette = data.get('palette', [])
        for b in data.get('blocks', []):
            full_name = palette[int(b['state'])]['Name']
            if "air" not in full_name.lower():
                create_part(model, full_name.split(':')[-1], b['pos'][0], b['pos'][1], b['pos'][2])
        tree = ET.ElementTree(roblox)
        ET.indent(tree, space="\t")
        tree.write(rbxmx_path, encoding="utf-8", xml_declaration=True)
        print(f"DONE: {rbxmx_path}")
    except Exception as e:
        print(f"ERROR: {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        convert(sys.argv[1], sys.argv[1].replace(".nbt", ".rbxmx"))
