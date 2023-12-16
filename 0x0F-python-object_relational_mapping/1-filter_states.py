#!/usr/bin/python3

"""This module provides a function that lists all states with a name
starting with N from a specific database.
"""
import sys
import MySQLdb


def filter_states(username, password, db_name):
    """Lists states with names starting with N.

    Arguments:
            username: mysql username
            password: mysql password
            db_name: database name
    """
    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
            )
    cur = db_connection.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    query_data = cur.fetchall()
    for row in query_data:
        print(row)

    cur.close()
    db_connection.close()


if __name__ == "__main__":
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
