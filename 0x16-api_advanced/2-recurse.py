#!/usr/bin/python3
"""queries Reddit API to get all hot articles of a subreddit"""

import requests as req


def recurse(subreddit, hot_list=[], after=''):
    """get all the hot articles of a subreddit"""
    li = []
    base = 'https://www.reddit.com'
    header = {'User-agent': 'a_oluwaferanmi'}
    respons = req.get('{}/r/{}/hot.json?after={}&limit=200'
                      .format(base, subreddit, after),
                      headers=header, allow_redirects=False)
    if respons.status_code != 200:
        return None
    posts = respons.json().get('data').get('children')
    _next = respons.json().get('data').get('after')
    for post in posts:
        hot_list.append(post.get('data').get('title'))

    if _next is not None:
        li.append(hot_list)
        recurse(subreddit, hot_list, _next)
    return hot_list
