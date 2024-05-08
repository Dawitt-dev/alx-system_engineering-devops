#!/usr/bin/python3
"""A recursive function that queries the Reddit API,
   parses the title of all hot articles, and prints
   a sorted count of given keywords
"""
import requests


def count_words(subreddit, word_list, word_count={}, after=None):
    """Parses the title of all hot articles, and
       prints a sorted count of given keywords
    """
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
        return

    data = response.json().get('data').get('children')
    for post in data:
        title = post.get('data').get('title')
        for word in word_list:
            if word.lower() in title.lower():
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    after = response.json().get('data').get('after')
    if after is None:
        if not word_count:
            return
        for key in sorted(word_count.keys()):
            print("{}: {}".format(key, word_count[key]))
        return
    return count_words(subreddit, word_list, word_count, after)
