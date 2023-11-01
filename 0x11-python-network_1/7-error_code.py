#!/usr/bin/python3
"""
This script sends a request to a URL and displays the
response body. If the HTTP status code is
greater than or equal to 400, it prints an error message.
"""
import requests
import sys


def fetch_and_display_response(url):
    """
    Sends a request to the provided URL, checks the
    HTTP status code, and displays the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None: Displays the response body or an error
        message based on the status code.
    """
    try:
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display_response(url)
