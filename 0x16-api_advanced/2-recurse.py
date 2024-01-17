#!/usr/bin/python3

"""
Recursive function that queries Reddit api
returns a list containing the titles of all hot articles
for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[], after=""):
    """
    Returns a list of titles
    of hot articles for a subreddit
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    req = requests.get(
        url, headers={"User-Agent": "Custom"}, params={"after": after})
    if req.status_code == 200:
        for get_data in req.json().get("data").get("children"):
            dat = get_data.get("data")
            title = dat.get("title")
            hot_list.append(title)
        after = req.json().get("data").get("after")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
