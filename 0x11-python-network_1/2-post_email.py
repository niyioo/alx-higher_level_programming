#!/usr/bin/python3

"""
This script sends a POST request to a URL with
an email as a parameter and displays the body
of the response (decoded in utf-8).
"""

import sys
import urllib.request
import urllib.parse


def send_post_request(url, email):
    """
    Sends a POST request to the specified URL with
    the given email parameter.

    Args:
        url (str): The URL to which the POST request is sent.
        email (str): The email to be sent as a parameter.

    Returns:
        str: The decoded response body as a UTF-8 encoded string.
    """
    value = {"email": email}
    data = urllib.parse.urlencode(value).encode("ascii")
    
    request = urllib.request.Request(url, data)

    with urllib.request.urlopen(request) as response:
        return response.read().decode("utf-8")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <EMAIL>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    response_body = send_post_request(url, email)
    print(response_body)
