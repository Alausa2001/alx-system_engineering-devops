#!/usr/bin/python3
"""queries Reddit API to get the number of subscribers of a subreddit"""

import requests as req


def number_of_subscribers(subreddit):
    """get the number of subscribers of a subreddit"""
    base = 'https://www.reddit.com'
    header = {'User-agent': 'a_oluwaferanmi'}
    respons = req.get('{}/r/{}/about.json'.format(base, subreddit),
                      headers=header, allow_redirects=False)
    if respons.status_code != 200:
        return 0
    sub_count = respons.json().get('data').get('subscribers')
    return sub_count
