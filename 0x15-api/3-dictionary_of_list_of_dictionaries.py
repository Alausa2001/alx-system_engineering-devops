#!/usr/bin/python3
"""
Using what you did in the task #0, extend your Python script to
export data in the JSON format.
Records all tasks from all employees
Format must be:
File name must be: todo_all_employees.json
"""
from json import dump
import requests as req
from sys import argv as av


def getInfo():
    """gets information about an employees' TODO list progress."""
    base = 'https://jsonplaceholder.typicode.com/'
    id_tasks = dict()
    # get employees personal info # empees = employees
    empees = req.get(base + 'users').json()
    for employee in empees:
        todos = req.get(base + 'users/{}/todos'.format(employee['id'])).json()
        _file = 'todo_all_employees.json'
        _id = employee.get('id')
        username = employee.get('username')
        tasks = []
        for todo in todos:
            task_info = {}
            # print(todo)
            task_info['task'] = todo.get('title')
            task_info['completed'] = todo.get('completed')
            task_info['username'] = username
            tasks.append(task_info)
        id_tasks[_id] = tasks
    with open(_file, 'w') as jsonfile:
        dump(id_tasks, jsonfile)


if __name__ == '__main__':
    getInfo()
