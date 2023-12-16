#!/usr/bin/python3

"""This module provides a function that uses the `MySQLdb`
module to connect to a specified database, get and list
all states from the database.
"""
import MySQLdb
import sys


def list_states(username, password, db_name):
    """Accepts input from the user and sets parameters for
    connecting to the specified database. It queries the
    database table (states) and returns all state records
    in ascending id.
    """
    # 1. Create a connection
    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
            )
    # 2. Get a cursor
    cur = db_connection.cursor()
    # 3. Execute MySQL query - Extract all state records in ascending order
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    # 4. Retrieve the data returned from 3 above
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)

    # 6. Close the cursor, then the connection
    cur.close()
    db_connection.close()


if __name__ == "__main__":
    list_states(sys.argv[1], sys.argv[2], sys.argv[3])
