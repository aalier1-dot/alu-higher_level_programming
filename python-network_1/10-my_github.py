#!/usr/bin/python3
"""Takes a GitHub username and personal access token, uses Basic
Authentication to query the GitHub API, and displays the user's id.
Prints None if authentication fails."""
import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    response = requests.get(
    response = requests.get(
        "https://api.github.com/user",
        auth=(username, password)
    )
    print(response.json().get("id"))
