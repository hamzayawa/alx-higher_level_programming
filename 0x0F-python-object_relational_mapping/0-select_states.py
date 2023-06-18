#!/usr/bin/python3
# Lists all states from the database of hbtn_0e_0_usa.
# Usage: ./0-select_states.py <mysql username> \
#                             <mysql password> \
#                             <database name>
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    con = db.cursor()
    con.execute("SELECT * FROM `states`")
    [print(state) for state in con.fetchall()]
