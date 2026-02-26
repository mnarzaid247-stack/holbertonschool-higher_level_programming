#!/usr/bin/python3
"""lists all ceties"""

import sys
import MySQLdb


def main():
    """main functhion"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()
    cur.execute(
        "SELECT states.id, cities.name, states.name FROM cities INNIR JOIN states"
        "ON states.id = cities.state_id ORDER BY cities.id ASC;")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
