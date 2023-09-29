#!/usr/bin/python3
"""
This script sends a POST request with a letter as a
parameter to http://0.0.0.0:5000/search_user.
It processes the JSON response and displays the id and
name or an error message.
"""
import requests
import sys


def search_user(letter):
    """
    Sends a POST request with the provided letter as the 'q'
    parameter and processes the JSON response.

    Args:
        letter (str): The letter to be used as
        the 'q' parameter in the request.

    Returns:
        None: Displays the id and name if found in the
        response, or an error message otherwise.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    try:
        url = "http://0.0.0.0:5000/search_user"
        data = {'q': letter}
        response = requests.post(url, data=data)
        response.raise_for_status()

        try:
            json_data = response.json()
            if json_data:
                print("[{}] {}".format(json_data.get('id'),
                      json_data.get('name')))
            else:
                print("No result")
        except ValueError:
            print("Not a valid JSON")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    search_user(letter)
