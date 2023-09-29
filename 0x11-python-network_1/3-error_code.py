#!/usr/bin/python3

"""
This script sends a request to a URL, displays
the body of the response (decoded in utf-8),
and handles urllib.error.HTTPError exceptions
by printing the error code.
"""

import urllib.request
import urllib.error
import sys


def send_request_and_display_body(url):
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            decoded_data = data.decode('utf-8')
            print(decoded_data)
    except urllib.error.HTTPError as e:
        print("Error code:", e.code)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    send_request_and_display_body(url)
