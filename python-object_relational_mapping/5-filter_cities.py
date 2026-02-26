#!/usr/bin/python3
"""lists"""

import MySQLdb
import sys


def main():
    if len(sys.argv) != 5:
        return
    username = sys.argv[1]
    password = sys.argv[2]
    database =sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cur = db.cursor()
    cur.execute("SELECT state_name FROM cities "
            "INNER JOIN states ON states.id = cities.state_id "
            "WHERE states.name = %s ORDER BY cities.id ASC",
            (state, )
               )
    for row in cur.fetchall():
        print(row, end=",")
    cur.close()
    db.close()


if __name__ == "__main__":
    main()
