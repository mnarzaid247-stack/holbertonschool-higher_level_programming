#!/usr/bin/python3
"""Lists states matching the given name."""

import sys
import MySQLdb


def main():
    """the main function"""
    if len(sys.argv) != 5:
        return
        
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
        )
    cur = db.cursor()
    cur.execute(
            "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC;",
            (state,)
            )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
