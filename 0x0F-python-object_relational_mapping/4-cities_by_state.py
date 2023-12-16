#!/usr/bin/python3
"""
lists all states with a name starting with N
"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        password=argv[2],
        database=argv[3]
    )

    cursor = conn.cursor()

    query = """SELECT cities.id, cities.name, states.name
    FROM states
    INNER JOIN cities ON states.id = cities.states_id 
    ORDER BY cities.id ASC"""

    cursor.execute(query)

    result = cursor.fetchall()

    for row in result:
        if row[1] == argv[4]:
            print(row)
    cursor.close()
    conn.close()
