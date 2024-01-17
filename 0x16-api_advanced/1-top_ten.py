#!/usr/bin/python3
"""
Function queries the Redit api
and prints the titles of the first 
ten hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Queries Redit API
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(
        url, header={"User-Agent": "Custom"}, params={"limit": 10})
    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            Data = get_data("data")
            title = Data.get("title")
            print(title)
        else:
            print(None)
