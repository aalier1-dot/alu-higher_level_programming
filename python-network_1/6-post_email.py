#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request using requests
with the email as a parameter, and displays the response body."""
import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    response = requests.post(url, data={'email': email})
    print(response.text)
