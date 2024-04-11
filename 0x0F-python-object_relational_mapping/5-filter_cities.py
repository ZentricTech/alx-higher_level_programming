#!/usr/bin/python3


"""
script takes name of state as arg & lists cities of state, db hbtn_0e_4_usa
script takes 4 args: username, mysql, db name and state name
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
    sql_cmd = """SELECT cities.name
                 FROM cities
                 LEFT JOIN states ON cities.state_id = states.id
                 WHERE states.name LIKE %s
                 ORDER BY cities.id ASC"""
    cur.execute(sql_cmd, (argv[4], ))
    query_rows = cur.fetchall()
    print(', '.join(["{:s}".format(row[0]) for row in query_rows]))
    cur.close()
    conn.close()
