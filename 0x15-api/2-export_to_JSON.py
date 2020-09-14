#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
from sys import argv
import json
import requests


def get_employee(id):
    """ Get employe by id from API """
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    ).json()

    name = user_data.get('name')
    if not name:
        return

    """Get all the tasks -*- TODOS"""
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/'
    ).json()

    """Records all tasks that are owned by this employee"""
    tasks_user = [task for task in all_tasks if task.get('userId') == id]

    """ Generate JSON data response """
    response = {str(id): []}
    for task in tasks_user:
        data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        }
        response[str(id)].append(data)

    """ Save JSON data in a file """
    with open('{}.json'.format(id), 'w') as json_file:
        json.dump(response, json_file)


if __name__ == "__main__":
    """ Entry point """
    get_employee(int(argv[1]))
