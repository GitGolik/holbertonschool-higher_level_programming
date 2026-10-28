#!/usr/bin/env python3
"""Display products from JSON or CSV files in Flask."""

import csv
import json

from flask import Flask, render_template, request

app = Flask(__name__)


def read_products_json():
    """Read products from products.json."""
    with open("products.json", "r", encoding="utf-8") as json_file:
        return json.load(json_file)


def read_products_csv():
    """Read products from products.csv."""
    products = []

    with open("products.csv", "r", newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })

    return products


@app.route("/products")
def products():
    """Display products from the selected source, optionally filtered by id."""
    source = request.args.get("source")
    product_id = request.args.get("id")

    if source not in ("json", "csv"):
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    if source == "json":
        products = read_products_json()
    else:
        products = read_products_csv()

    if product_id is not None:
        try:
            product_id = int(product_id)
        except ValueError:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

        products = [
            product for product in products
            if product["id"] == product_id
        ]

        if not products:
            return render_template(
                "product_display.html",
                error="Product not found"
            )

    return render_template(
        "product_display.html",
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
