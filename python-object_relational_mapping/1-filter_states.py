#!/usr/bin/python3
"""Lists all states with names starting with N."""

import MySQLdb
import sys


def main():
    """Connects to MySQL and prints states starting with upper N."""
    if len(sys.argv) != 4:
        return
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
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
