#!/usr/bin/python3
"""
This script sends a POST request to a given URL
with an email as a parameter and displays the
body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.parse
import sys


def send_post_request(url, email):
    try:
        data = urllib.parse.urlencode({'email': email}).encode()
        req = urllib.request.Request(url, data, method='POST')
        
        with urllib.request.urlopen(req) as response:
            response_data = response.read()
            decoded_data = response_data.decode('utf-8')
            print(decoded_data)
    except urllib.error.URLError as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <EMAIL>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
    print("Your email is:", email)
