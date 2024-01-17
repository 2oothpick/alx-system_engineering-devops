#!/usr/bin/python3
"""
Function queries the Redit API and 
returns the number of subscribers
for a given subredit
"""

import requests


def number_of_subscriber(subreddit):
    """
    Queries Redit api
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    req = requests.get(url, headers={"User-Agent": "Custom"})
    if req.status_code == 200:
        return req.json().get("data").get("subscibers")
    else:
        return 0
