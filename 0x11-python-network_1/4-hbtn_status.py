#!/usr/bin/python3
"""This module uses `requests` to fetch
`https://alx-intranet.hbtn.io/status`.
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)

    content = response.text                  # Retrieve the content

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
