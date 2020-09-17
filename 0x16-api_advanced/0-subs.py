#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """[summary]

    Args:
        subreddit ([str]): [subreddit]

    Returns:
        [int]: [the number of subscribers to a specified subreddit]
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': '1639-holbertonschool'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        subscribers = data.get('subscribers')
        if data and subscribers:
            return subscribers
    return 0
