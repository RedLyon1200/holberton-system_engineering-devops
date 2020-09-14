#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
import requests
from sys import argv


def get_employee(id):
    """ Get employe by id from API """
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    ).json()

    if not user_data.get('name'):
        return

    """Get all the tasks -*- TODOS"""
    all_tasks = requests.get(
        'https://jsonplaceholder.typicode.com/todos/'
    ).json()

    """Records all tasks that are owned by this employee"""
    tasks_user = [task for task in all_tasks if task.get('userId') == id]

    """Records all tasks this employee has completed"""
    tasks_done = [task for task in tasks_user if task.get('completed')]

    response = 'Employee {} is done with tasks({}/{}):'.format(
        user_data.get('name'), len(tasks_done), len(tasks_user)
    )

    print(response)
    for task in tasks_done:
        print(task.get('title'))


if __name__ == "__main__":
    get_employee(int(argv[1]))
