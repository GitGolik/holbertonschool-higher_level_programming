@app.route("/products")
def products():
    """Display products from the selected data source, optionally filtered by id."""
    source = request.args.get("source")
    product_id = request.args.get("id")

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
