#!/usr/bin/python3
"""
This script sends an HTTP request to a given URL and
displays the value of the X-Request-Id variable
found in the response header.
"""

import urllib.request
import sys


def get_x_request_id(url):
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.getheader('X-Request-Id')
            if x_request_id:
                print(x_request_id)
    except urllib.error.URLError as e:
        print("Error: ", e)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    get_x_request_id(url)
