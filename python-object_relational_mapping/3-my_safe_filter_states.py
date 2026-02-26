#!/usr/bin/python3
"""Lists states matching the given name."""

import sys
import MySQLdb


def main():
    if len(sys.argv) != 4:
        return
    username = sys.argv[1]
    paswword = sys.argv[2]
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
            "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC;"
            .format(state)
            )
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
