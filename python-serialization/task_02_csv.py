import csv
import json

def convert_csv_to_json(csv_filename):
    """convert csv file to json file"""

    try:
        with open(csv_filename, "r", encoding="utf-8", newline="") as csv_file:
            reader = csv.DictReader(csv_file)
            date = list(reader)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4)

        return True

    except Exception:
        return False
