import json


def serialization_and_save_to_file(data, filename):
    """serialize a python dir in json and save it in file"""

    with open(filename, "w" encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_and_deserialize(filename):
    """load json file and deserialize a python dir"""

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
