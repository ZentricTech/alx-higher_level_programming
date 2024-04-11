#!/usr/bin/python3


"""
lists all cities from the database hbtn_0e_4_usa
script takes 3 arguments: username, password, db name
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    # connect to a database
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3])

    # create a cursor to exec queries using SQL
    cur = conn.cursor()
    sql_cmd = """SELECT cities.id, cities.name, states.name
                 FROM cities
                 LEFT JOIN states ON cities.state_id = states.id
                 ORDER BY cities.id ASC"""
    cur.execute(sql_cmd)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
