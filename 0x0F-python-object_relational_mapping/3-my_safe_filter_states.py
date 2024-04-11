#!/usr/bin/python3


"""
safe from SQL injections
script arg & displays all values in the states table where name matches the arg
script takes 4 arguments: username, password, db name and state name searched
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
    sql_cmd = """SELECT *
                 FROM states
                 WHERE name=%s
                 ORDER BY id ASC"""
    cur.execute(sql_cmd, (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
