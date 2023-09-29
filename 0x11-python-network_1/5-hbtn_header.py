#!/usr/bin/python3
"""
This script takes a URL as input, sends a GET request
to the URL, and displays the value of the 'X-Request-Id'
variable from the response header.
"""
import requests
import sys


def get_x_request_id(url):
    """
    Sends a GET request to the specified URL and retrieves
    the 'X-Request-Id' variable from the response header.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None: The 'X-Request-Id' value is printed if
        it exists in the response header.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    get_x_request_id(url)
