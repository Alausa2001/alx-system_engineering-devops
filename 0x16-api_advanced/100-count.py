#!/usr/bin/python3
"""recursive function that queries the Reddit API, parses the title of all hot
articles, and prints a sorted count of given keywords (case-insensitive,
delimited by spaces. Javascript should count as javascript, but java should'nt


Requirement
If word_list contains the same word (case-insensitive),
the final count should be the sum of each duplicate (example below with java)

Results should be printed in descending order, by the count, and
if the count is the same for separate keywords, they should then be sorted
alphabetically (ascending, from A to Z). Words with no matches should be
skipped and not printed. Words must be printed in lowercase.

Results are based on the number of times a keyword appears,
not titles it appears in. java java java counts as 3 separate occurrences of
java.

To make life easier, java. or java! or java_ should not count as java

If no posts match or the subreddit is invalid, print nothing.
"""

import requests as req


def count_words(subreddit, word_list, kw_dict={}, after=''):
    """recursive function that queries the Reddit API"""
    base = 'https://www.reddit.com'
    header = {'User-agent': 'a_oluwaferanmi'}
    respons = req.get('{}/r/{}/hot.json?after={}&limit=100'
                      .format(base, subreddit, after),
                      headers=header, allow_redirects=False)
    if respons.status_code != 200:
        return None

    keywords = []
    for word in word_list:
        word = word.lower()
        keywords.append(word)
    for keyword in keywords:
        if keyword not in kw_dict:
            kw_dict[keyword] = 0
        else:
            kw_dict[keyword] += 1

    posts = respons.json().get('data').get('children')
    _next = respons.json().get('data').get('after')

    for post in posts:
        title = post.get('data').get('title')
        title_words = title.lower().split(' ')
        for key, value in kw_dict.items():
            if key in title_words:
                kw_dict[key] = value + 1

    if _next is None:
        sort = []

        print(kw_dict)
    if _next is not None:
        count_words(subreddit, word_list, kw_dict, _next)
