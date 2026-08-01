#!/usr/bin/python3
import requests
import sys
repo = sys.argv[1]
owner = sys.argv[2]
url = "https://api.github.com/repos/{}/{}/commits".format(owner, repo)
response = requests.get(url, params={"per_page": 10})
commits = response.json()
for commit in commits:
    sha = commit.get("sha")
    name = commit.get("commit", {}).get("author", {}).get("name")
    print("{}: {}".format(sha, name))
