import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a Python dictionary to JSON and save it to the specified file.

    Args:
        data (dict): Python dictionary to serialize.
        filename (str): Path to the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load a JSON file and deserialize it into a Python dictionary.

    Args:
        filename (str): Path to the input JSON file.

    Returns:
        dict: Python dictionary with deserialized data.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

