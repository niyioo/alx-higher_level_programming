#!/usr/bin/python3
"""
This script sends a POST request to a specified URL
with an email as a parameter
and displays the response body.
"""
import requests
import sys


def send_post_request(url, email):
    """
    Sends a POST request to the provided URL with the
    email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to include in the request.

    Returns:
        None: The response body is printed.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    try:
        data = {'email': email}
        response = requests.post(url, data=data)
        response.raise_for_status()
        print(response.text)
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <EMAIL>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    send_post_request(url, email)
