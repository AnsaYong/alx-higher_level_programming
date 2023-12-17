#!/usr/bin/python3

"""This module provides a function that lists
all cities from a database.
"""
import sys
import MySQLdb


def list_cities_with_states(username, password, db_name):
    """Uses `JOIN` to join the cities and states tables,
    and then lists all cities from a database.

    Arguments:
            username: mysql username
            password: mysql password
            db_name: database name
    """
    # Create connection to the database
    db_connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=db_name,
            charset="utf8"
            )

    # Generate the cursor
    cursor = db_connection.cursor()

    # Execute the query to fetch data from the database
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the connection and the cursor
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    list_cities_with_states(sys.argv[1], sys.argv[2], sys.argv[3])
