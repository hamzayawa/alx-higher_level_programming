#!/usr/bin/python3
"""Script that lists all cities by state"""

import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    con = conn.cursor()
    con.execute("SELECT cities.id, cities.name, states.name FROM cities" +
                " INNER JOIN states ON cities.state_id = states.id ORDER BY" +
                " cities.id ASC")
    query_rows = con.fetchall()
    for row in query_rows:
        print(row)
    con.close()
    conn.close()
