#!/usr/bin/python3
"""
this module contains a function that queries the Reddit API and prints the
titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    function queries the Reddit API and prints the titles of the first 10 hot
    posts listed for a given subreddit
    """

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    h = {'User-agent': 'ad-egg'}
    r = requests.get(
            url, headers=h, allow_redirects=False, params={'limit': 10})

    if r.status_code == 200:
        req = r.json()
        data = req.get('data')
        children = data.get('children')
        if data is None or children is None:
            print('None')
        else:
            for post in children:
                post_data = post.get('data')
                title = post_data.get('title')
                print(title)
    else:
        print('None')
