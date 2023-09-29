#!/usr/bin/python3
"""
This script sends a GET request to a URL, checks the HTTP status code,
and prints the response body or an error message.
"""
import requests
import sys


def fetch_and_display_response(url):
    """
    Sends a GET request to the provided URL, checks
    the HTTP status code, and displays the response.

    Args:
        url (str): The URL to send the GET request to.

    Returns:
        None: Prints the response body or an error
        message based on the status code.
    """
    try:
        response = requests.get(url)

        if response.status_code >= 400:
            print("Error code: {}".format(response.status_code))
        else:
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    url = sys.argv[1]
    fetch_and_display_response(url)
