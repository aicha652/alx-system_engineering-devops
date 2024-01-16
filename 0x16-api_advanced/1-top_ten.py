#!/usr/bin/python3
"""function that queriesthe Reddit
API and prints the titles"""
import requests


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit"""

    if subreddit is None:
        return None

    url = "http://www.reddit.com/r/{}/hot".format(subreddit)
    response = requests.get(url)

    if response.status_code == 200:
        response = response.json()
    else:
        return None

    return response.get("data", {}).get("subscribers", None)
