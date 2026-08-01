#!/usr/bin/python3
"""Takes a letter and sends a POST request to search_user with the
letter as the 'q' parameter. Displays [id] name if valid JSON with
content, 'No result' if empty JSON, or 'Not a valid JSON' if invalid."""
import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    else:
        letter = ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': letter})
    try:
        data = response.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
