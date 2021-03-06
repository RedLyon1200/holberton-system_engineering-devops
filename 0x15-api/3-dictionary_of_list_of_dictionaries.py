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

    """ Generate data response in a list"""
    response = []
    for task in tasks_user:
        data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': username
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
