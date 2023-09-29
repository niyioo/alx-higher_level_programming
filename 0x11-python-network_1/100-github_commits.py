#!/usr/bin/python3
"""
This script uses the GitHub API to list the 10 most
recent commits from a repository by an owner.
"""
import requests
import sys


def list_recent_commits(owner, repo):
    """
    Sends a GET request to the GitHub API to retrieve
    recent commits and prints the commit details.

    Args:
        owner (str): The owner (username or organization) of the repository.
        repo (str): The name of the repository.

    Returns:
        None: Prints commit details in the format <sha>: <author name>.

    Raises:
        requests.exceptions.RequestException: If an
        error occurs during the request.
    """
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {"per_page": 10}  # Get the most recent 10 commits

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()

        commits = response.json()
        for commit in commits:
            sha = commit["sha"]
            author_name = commit["commit"]["author"]["name"]
            print(f"{sha}: {author_name}")
    except requests.exceptions.RequestException as e:
        print("Error:", e)


if __name__ == "__main__":
    owner = sys.argv[2]
    repo = sys.argv[1]
    list_recent_commits(owner, repo)
