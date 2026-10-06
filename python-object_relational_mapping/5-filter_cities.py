#!/usr/bin/python3
"""list all cities belonging to a given state"""

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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC",
        (sys.argv[4],)
    )

    cities = [city[0] for city in cursor.fetchall()]
    print(", ".join(cities))

    cursor.close()
    connection.close()
