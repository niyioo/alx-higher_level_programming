#!/usr/bin/python3
"""
This script fetches the status from a specific
URL and displays the response.
"""
import requests


def fetch_and_display_status():
    """
    Fetches the status from a specific URL and displays the response.

    This function sends a GET request to a specified URL,
    checks for HTTP errors,
    and displays the response content.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.

    Returns:
        None
    """
    url = "https://alx-intranet.hbtn.io/status"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        body = response.text

        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    fetch_and_display_status()
