#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to export
data in the CSV format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
    File name must be: USER_ID.csv
"""
import csv
import requests as req
from sys import argv as av


def getInfo():
    """gets information about an employees' TODO list progress."""
    base = 'https://jsonplaceholder.typicode.com/'
    # get employees personal info
    info = req.get(base + 'users/{}'.format(av[1])).json()
    todos = req.get(base + 'users/{}/todos'.format(av[1])).json()
    _file = '.'.join([str(info.get('id')), 'csv'])

    with open(_file, 'w') as csvfile:
        username = info.get('name')
        for todo in todos:
            _id = info.get('id')
            taskStatus = todo.get('completed')
            title = todo.get('title')
            _write = csv.writer(csvfile, delimiter=',', quoting=csv.QUOTE_ALL)
            _write.writerow([_id, username, taskStatus, title])


if __name__ == '__main__':
    getInfo()
