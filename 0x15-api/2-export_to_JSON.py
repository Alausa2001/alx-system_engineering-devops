#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.

Requirements:

    Records all tasks that are owned by this employee
    Format must be: { "USER_ID": [{"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS,
    "username": "USERNAME"}, {"task": "TASK_TITLE",
    "completed": TASK_COMPLETED_STATUS, "username": "USERNAME"}, ... ]}
    File name must be: USER_ID.json
"""
from json import dump
import requests as req
from sys import argv as av


def getInfo():
    """gets information about an employees' TODO list progress."""
    base = 'https://jsonplaceholder.typicode.com/'
    # get employees personal info
    info = req.get(base + 'users/{}'.format(av[1])).json()
    todos = req.get(base + 'users/{}/todos'.format(av[1])).json()
    _file = '{}.json'.format(info.get('id'))
    _id = info.get('id')
    username = info.get('username')
    tasks = []
    for todo in todos:
        task_info = {}
        # print(todo)
        task_info['task'] = todo.get('title')
        task_info['completed'] = todo.get('completed')
        task_info['username'] = username
        tasks.append(task_info)
    id_tasks = {_id: tasks}
    with open(_file, 'w') as jsonfile:
        dump(id_tasks, jsonfile)


if __name__ == '__main__':
    getInfo()
