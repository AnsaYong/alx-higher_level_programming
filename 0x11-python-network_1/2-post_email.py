#!/usr/bin/python3
"""Takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8).
"""


import urllib.request
from urllib import parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare data for the POST request
    data = parse.urlencode({'email': email}).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        content = response.read().decode('utf-8')
        print(content)
