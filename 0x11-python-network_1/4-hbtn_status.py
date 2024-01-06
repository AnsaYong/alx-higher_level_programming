#!/usr/bin/python3
"""This module uses `requests` to fetch
`https://alx-intranet.hbtn.io/status`.
"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    response = requests.get(url)

    content = response.content                  # Retrieve the content
    utf8_content = content.decode('utf-8')      # Convert content to utf-8

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)
