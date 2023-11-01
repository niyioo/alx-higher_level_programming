#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
and displays information about the response body.
"""

import urllib.request


def fetch_and_display_status():
    url = "https://alx-intranet.hbtn.io/status"

    with urllib.request.urlopen(url) as response:
        body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))


if __name__ == "__main__":
    fetch_and_display_status()
