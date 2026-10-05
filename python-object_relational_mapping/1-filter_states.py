#!/usr/bin/python3
"""List states whose name starts with an uppercase N."""

import MySQLdb
import sys


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC",
        ("N%",)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
