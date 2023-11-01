#!/usr/bin/python3
"""
This script authenticates with the GitHub API using
Basic Authentication and retrieves the user's ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, access_token):
    """
    Sends a GET request to the GitHub API to retrieve
    user information and displays the user ID.

    Args:
        username (str): GitHub username.
        access_token (str): Personal access token used as a password.

    Returns:
        None: Displays the user's GitHub ID or appropriate error messages.

    Raises:
        requests.exceptions.RequestException: If
        an error occurs during the request.
    """
    auth = HTTPBasicAuth(username, access_token)
    response = requests.get("https://api.github.com/user", auth=auth)

    try:
        user_data = response.json()
        user_id = user_data.get("id")
        if user_id is not None:
            print(user_id)
        else:
            print("User ID not found in the response.")
    except ValueError:
        print("Not a valid JSON response.")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script_name.py <GitHub Username> "
              "<Personal Access Token>")
        sys.exit(1)

    username = sys.argv[1]
    access_token = sys.argv[2]
    get_github_user_id(username, access_token)
