#!/usr/bin/python3
"""queries Reddit API to get all hot articles of a subreddit"""

import requests as req


def recurse(subreddit, hot_list=[], after=''):
    """get all the hot articles of a subreddit"""
    base = 'https://www.reddit.com'
    header = {'User-agent': 'a_oluwaferanmi'}
    respons = req.get('{}/r/{}/hot.json?after={}&limit=100'
                      .format(base, subreddit, after),
                      headers=header, allow_redirects=False)
    if respons.status_code != 200:
        return None
    else:
        posts = respons.json().get('data').get('children')
        for post in posts:
            hot_list.append(post.get('data').get('title'))

    if after is not None:
        _next = respons.json().get('data').get('after')
        recurse(subreddit, hot_list, _next)
    return hot_list
