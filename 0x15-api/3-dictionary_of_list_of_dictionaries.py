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

    """ Generate data response in a list"""
    response = []
    for task in tasks_user:
        data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        }
        response.append(data)

    return response


if __name__ == "__main__":
    """ Entry point """
    total_users = len(
        requests.get('https://jsonplaceholder.typicode.com/users/').json()
    ) + 1

    response = {}
    for i in range(1, total_users):
        response[str(i)] = get_employee(i)

    with open('todo_all_employees.json', 'w') as json_file:
        json.dump(response, json_file)
