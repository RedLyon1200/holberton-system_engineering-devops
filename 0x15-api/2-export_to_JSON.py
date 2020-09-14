#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
from sys import argv
import json
import requests


def get_employee(id):
    """ Get employe by id from API """
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/', params={'id': id}
    ).json()

    username = user_data[0].get('username')

    """Records all tasks that are owned by this employee"""
    tasks_user = requests.get(
        'https://jsonplaceholder.typicode.com/todos/', params={'userId': id}
    ).json()

    """ Generate JSON data response """
    response = {str(id): []}
    for task in tasks_user:
        data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
        }
        response[str(id)].append(data)

    """ Save JSON data in a file """
    with open('{}.json'.format(id), 'w') as json_file:
        json.dump(response, json_file)


if __name__ == "__main__":
    """ Entry point """
    get_employee(int(argv[1]))
