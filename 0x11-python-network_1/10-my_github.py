#!/usr/bin/python3
"""Takes GitHub credentials (username and personal access token),
uses Basic Authentication with a personal access token as the password
to access GitHub API and displays your user ID.
"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    # URL for the authenticated user's information
    url = "https://api.github.com/user"

    # Set up Basic Authentication using personal access token
    auth = (username, token)

    # Send GET request to GitHub API
    response = requests.get(url, auth=auth)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        user_data = response.json()
        user_id = user_data['id']
        print("Your GitHub user ID:", user_id)
    else:
        print("Error:", response.text)
