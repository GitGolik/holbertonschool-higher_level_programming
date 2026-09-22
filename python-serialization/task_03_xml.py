import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): Dictionary to serialize.
        filename (str): Path to the output XML file.
    """
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)


def deserialize_from_xml(filename):
    """
    Deserialize an XML file into a Python dictionary.

    Args:
        filename (str): Path to the input XML file.

    Returns:
        dict: Dictionary reconstructed from XML data.
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}
    for element in root:
        data[element.tag] = element.text

    return data

