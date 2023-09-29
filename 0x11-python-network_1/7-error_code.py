#!/usr/bin/python3
"""
This script sends a request to a specified URL and
displays the body of the response.
If the HTTP status code is greater than or
equal to 400, it prints an error message.
"""
import requests
import sys


def fetch_and_display_response(url):
    """
    Sends a GET request to the provided URL and
    displays the response body.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None: The response body is printed. If the status code
        is >= 400, an error message is printed.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()

        print(response.text)

        if response.status_code >= 400:
            print("Error code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display_response(url)
