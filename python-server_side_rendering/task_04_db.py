#!/usr/bin/env python3
"""Display products from JSON, CSV, or SQLite in Flask."""

import csv
import json
import sqlite3

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


def read_products_sql():
    """Read products from the Products table in products.db."""
    connection = sqlite3.connect("products.db")
    connection.row_factory = sqlite3.Row

    try:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT id, name, category, price FROM Products"
        )

        return [dict(row) for row in cursor.fetchall()]
    finally:
        connection.close()


@app.route("/products")
def products():
    """Display products from the selected data source."""
    source = request.args.get("source")

    if source not in ("json", "csv", "sql"):
        return render_template(
            "product_display.html",
            error="Wrong source"
        )

    try:
        if source == "json":
            products = read_products_json()
        elif source == "csv":
            products = read_products_csv()
        else:
            products = read_products_sql()
    except (sqlite3.Error, OSError) as error:
        return render_template(
            "product_display.html",
            error="Database error"
        )

    return render_template(
        "product_display.html",
        products=products
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
