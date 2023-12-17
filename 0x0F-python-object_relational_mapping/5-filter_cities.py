#!/usr/bin/python3
"""This module provides a SQL injection free function that lists cities
from a database table, based on their state.
"""
import sys
import MySQLdb


def filter_cities(username, password, db_name, state):
    """Filters cities by state and displays the city
    names.

    Arguments:
            username: mysql username
            password: mysql password
            db_name: database name containing the required tables
            state: state name to filter cities by
    """
    try:
        # Establish a connection to the database
        db_connection = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                db=db_name,
                charset="utf8"
                )
    except MySQLdb.Error as e:
        print()
        return

    # Generate the cursor
    cursor = db_connection.cursor()

    # Execute query to fetch data from the databse
    query = """
    SELECT GROUP_CONCAT(cities.name) AS city_list
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    """

    cursor.execute(query, (state,))

    # Fetch the results
    results = cursor.fetchone()

    # Display reults
    if results and results[0]:
        city_list = results[0]
        cities = city_list.split(',')
        for city in cities:
            print(city.strip(), end=", " if city != cities[-1] else "\n")
    else:
        print()

    # Close connection and cursor
    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    filter_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
