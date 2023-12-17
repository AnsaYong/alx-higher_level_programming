#!/usr/bin/python3

"""This module provides a function that takes an argument
and displays records from a database table that match the
argument.
"""
import sys
import MySQLdb


def states_user_input(username, password, db_name, search_name):
    """Searches recods based on a user provided argument.

    Arguments:
            username: mysql username
            password: mysql password
            db_name: database name
            search_name: state name searched
    """
    # Establish connection
    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
            )

    # Create cursor object
    cursor = db_connection.cursor()

    # Set query to execute
    query = "SELECT * FROM states WHERE BINARY name = '{}' ORDER BY id ASC"

    # Execute query
    cursor.execute(query.format(search_name))

    # Fetch and print the result
    result = cursor.fetchall()
    for row in result:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    states_user_input(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
