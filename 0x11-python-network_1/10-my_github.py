#!/usr/bin/python3
"""
This script uses Basic Authentication with a personal
access token to access GitHub user information
and displays the user ID.
"""
import requests
import sys


def get_github_user_id(username, access_token):
    """
    Sends a GET request to the GitHub API to retrieve
    user information and display the user ID.

    Args:
        username (str): Your GitHub username.
        access_token (str): Your personal access token
        (used as a password).

    Returns:
        None: Displays the user ID.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    url = f"https://api.github.com/users/{username}"
    headers = {"Authorization": f"token {access_token}"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        user_data = response.json()
        user_id = user_data.get('id')
        
        if user_id is not None:
            print(f"GitHub User ID: {user_id}")
        else:
            print("User ID not found in the response.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    username = sys.argv[1]
    access_token = sys.argv[2]
    get_github_user_id(username, access_token)
