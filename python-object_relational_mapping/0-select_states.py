#!/usr/bin/python3
"""This script lists all states from the database."""

import MySQLdb
import sys
"""import library"""


def main():
    """Connect to MySQL and print all states ordered by id."""
    if len(sys.argv) != 4:
        return
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            password=password,
            db=database
        )
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

if __name__ == "__main__":
    main()
