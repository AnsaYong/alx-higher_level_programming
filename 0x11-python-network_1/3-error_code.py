#!/usr/bin/python3
"""Takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8).
Handles urllib.error.HTTPError exceptions and prints the
HTTP status code in case of an error.
"""
import urllib.request
from urllib import error
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            print(content)
    except error.HTTPError as e:
        print("Error code:", e.code)
