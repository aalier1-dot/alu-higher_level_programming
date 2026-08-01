#!/usr/bin/python3
"""Takes a URL and an email, sends a POST request with the email
as a parameter, and displays the response body decoded in utf-8."""
import sys
import urllib.parse
import urllib.request
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    with urllib.request.urlopen(url, data=data) as response:
        body = response.read()
        print(body.decode('utf-8'))
