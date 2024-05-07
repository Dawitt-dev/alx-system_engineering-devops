#!/usr/bin/python3
"""A recursive function that queries the Reddit API
   and returns a list containing the titles of all hot
   articles for a given subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of the titles of hot articles for a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        'User-Agent': 'chrome/124.0.0.0'
    }
    params = {
        'after': after
    }
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)

    if response.status_code != 200:
        return None

    data = response.json().get('data').get('children')
    for post in data:
        hot_list.append(post.get('data').get('title'))

    after = response.json().get('data').get('after')
    if after is None:
        return hot_list
    return recurse(subreddit, hot_list, after)
