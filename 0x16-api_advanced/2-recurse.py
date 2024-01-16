#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """recursive function that queries the Reddit API
    and returns a list containing the titles of all
    hot articles for a given subreddit"""
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/120.0.0.0 Safari/537.36'}

    response = requests.get(url, params={"after": after}, headers=user_agent)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            return hot_list
        for post in response.json().get("data").get("children"):
            hot_list.append(post.get("data").get("title"))
        return recurse(subreddit, hot_list, after)
