#!/usr/bin/python3
"""Create a fucntion that queries the Reddit API"""
import requests


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscribers"""
    if subreddit is None or type(subreddit) is not str:
        return 0

    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "advanced api project"}

    response = requests.get(url, headers=headers, , allow_redirects=False)

    if response.status_code == 200:
        response = response.json()
    else:
        return 0

    return response.get("data", {}).get("subscribers", 0)
