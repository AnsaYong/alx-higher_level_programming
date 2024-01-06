#!/usr/bin/python3
"""This module uses `urllib` to fetch
`https://alx-intranet.hbtn.io/status`.
"""
import urllib.request


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:   # Open url & get response
        content = response.read()                   # Retrieve the content
        utf8_content = content.decode('utf-8')      # Convert content to utf-8

        print("Body response:")
        print("\t- type:", type(content))
        print("\t- content:", content)
        print("\t- utf8 content:", utf8_content)
