#!/usr/bin/python3
"""Displays the states table"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = conn.cursor()
    con.execute(
        "SELECT * FROM states WHERE Name LIKE BINARY '{}' ORDER BY id ASC"
        .format(sys.argv[4]))
    query_rows = con.fetchall()
    for row in query_rows:
        print(row)
    con.close()
    conn.close()
