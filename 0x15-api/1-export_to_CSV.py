#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
import requests
from sys import argv
import csv


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

    """ Creates a file with employedd id by file name """
    with open('{}.csv'.format(id), mode='w') as file:
        data = csv.writer(
            file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        for task in tasks_user:
            data.writerow([id, name, task.get('completed'), task.get('title')])


if __name__ == "__main__":
    """ Entry point """
    get_employee(int(argv[1]))
