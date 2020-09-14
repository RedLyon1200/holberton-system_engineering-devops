#!/usr/bin/python3
""" -*- Coding UTF-8 -*- """
from sys import argv
import csv
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

    """ Creates a file with employedd id by file name """
    with open('{}.csv'.format(id), mode='w', encoding='UTF-8') as file:
        data = csv.writer(
            file,
            delimiter=',',
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        for task in tasks_user:
            data.writerow([id, username, task.get(
                'completed'), task.get('title')])


if __name__ == "__main__":
    """ Entry point """
    if argv[1].isdigit():
        get_employee(int(argv[1]))
