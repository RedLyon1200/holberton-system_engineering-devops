#!/usr/bin/python3
"""
queries the Reddit API and prints the titles of the
first 10 hot posts listed for a given subreddit.
"""

import requests


def top_ten(subreddit):
    """[summary]

    Args:
        subreddit ([str]): [subreddit]

    Returns:
        [int]: [the titles of the first 10 hot posts listed]
    """
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    user_agent = {'User-Agent': '1639-holbertonschool'}
    req = requests.get(url, headers=user_agent,
                       allow_redirects=False, params={'limit': 10})
    if req.status_code == 200:
        req = req.json()
        children = req.get('data').get('children')
        if children:
            for post in children:
                print(post.get('data').get('title'))
            return
    print(None)
