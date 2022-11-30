#!/usr/bin/python3
"""queries Reddit API to get the number of top 10 posts of a subreddit"""

import requests as req


def top_ten(subreddit):
    """get the top 10 posts of a subreddit"""
    base = 'https://www.reddit.com'
    header = {'User-agent': 'a_oluwaferanmi'}
    respons = req.get('{}/r/{}/hot.json'
                      .format(base, subreddit),
                      headers=header, allow_redirects=False)
    if respons.status_code != 200:
        print(None)
    posts = respons.json().get('data').get('children')
    count = 0
    for post in posts:
        if count <= 9:
            print(post.get('data').get('title'))
            count += 1
