#!/usr/bin/python3
"""recursive function that queries the Reddit API"""
import requests


def count_words(subreddit, word_list, hot_dict={}, after=""):
    """recursive function that queries the Reddit API"""
    if subreddit is None:
        return None
    url = "http://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    user_agent = {"User-Agent": "ALX project about advanced api"}

    response = requests.get(url, params={"after": after}, headers=user_agent)

    if response.status_code == 200:
        after = response.json().get("data").get("after")
        if not after:
            hot_dict = sorted(hot_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, occurence in hot_dict:
                print('{}: {}'.format(word, occurence))
            return
        for post in response.json().get("data").get("children"):
            title = post.get("data").get("title").lower()
            for word in word_list:
                word = word.lower()
                if word in title:
                    hot_dict[word] = hot_dict.get(word, 0) + 1
        return count_words(subreddit, word_list, hot_dict, after)
