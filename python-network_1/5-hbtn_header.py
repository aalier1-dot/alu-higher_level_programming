#!/usr/bin/python3
"""Takes a URL, sends a request using requests, and displays the
value of X-Request-Id found in the response header."""
value of X-Request-Id found in the response header."""
import requests
import sys
if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get('X-Request-Id'))
