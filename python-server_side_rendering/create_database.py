#!/usr/bin/env python3
"""Create and populate the products.db SQLite database."""

import sqlite3


def create_database():
    """Create the Products table and insert the required products."""
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    """)

    products = [
        (1, "Laptop", "Electronics", 799.99),
        (2, "Coffee Mug", "Home Goods", 15.99),
        (24, "Tesla Coil", "Electronics", 249.99)
    ]

    cursor.executemany(
        """
        INSERT OR REPLACE INTO Products (id, name, category, price)
        VALUES (?, ?, ?, ?)
        """,
        products
    )

    connection.commit()
    connection.close()


if __name__ == "__main__":
    create_database()
