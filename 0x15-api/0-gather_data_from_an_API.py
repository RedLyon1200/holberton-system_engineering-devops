#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
from sys import argv
import requests


def get_employee(id):
    """ Get employe by id from API """
    user_data = requests.get(
        'https://jsonplaceholder.typicode.com/users/', params={'id': id}
    ).json()

    name = user_data[0].get('name')

    """Records all tasks that are owned and have completed by this employee"""
    tasks_done = requests.get(
        'https://jsonplaceholder.typicode.com/todos/', params={
            'userId': id, 'completed': 'true'}
    ).json()

    tasks_user = requests.get(
        'https://jsonplaceholder.typicode.com/todos/', params={
            'userId': id}
    ).json()

    response = 'Employee {} is done with tasks({}/{}):'.format(
        name, len(tasks_done), len(tasks_user)
    )

    print(response)
    for task in tasks_done:
        print('\t {}'.format(task.get('title')))


if __name__ == "__main__":
    if argv[1].isdigit():
        get_employee(int(argv[1]))
