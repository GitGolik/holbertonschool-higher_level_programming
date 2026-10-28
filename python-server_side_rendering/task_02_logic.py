#!/usr/bin/env python3
"""Flask application rendering items from a JSON file."""

import json

from flask import Flask, render_template

app = Flask(__name__)


@app.route("/items")
def items():
    """Render the items page using data from items.json."""
    with open("items.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    return render_template("items.html", items=data["items"])


if __name__ == "__main__":
    app.run(debug=True, port=5000)
