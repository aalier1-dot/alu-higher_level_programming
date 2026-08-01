#!/usr/bin/python3
"""Takes a URL, sends a request, and displays the body of the
response decoded in utf-8. If an HTTPError occurs, prints the
error code instead."""
import sys
import urllib.error
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            body = response.read()
            print(body.decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
