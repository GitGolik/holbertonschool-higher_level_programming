#!/usr/bin/python3
"""Safely list states matching a user-provided name."""

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
    query = (
        "SELECT * FROM states "
        "WHERE BINARY name = %s "
        "ORDER BY id ASC"
    )
    cursor.execute(query, (sys.argv[4],))

    for state in cursor.fetchall():
        print(state)

    cursor.close()
    connection.close()
