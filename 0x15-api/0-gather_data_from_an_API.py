#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.

Requirements:

    You must use urllib or requests module
    The script must accept an integer as a parameter, which is the employee ID
    The script must display on the standard output the employee TODO list
    progress in this exact format:
        First line: Employee EMPLOYEE_NAME is done with
        tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
            EMPLOYEE_NAME: name of the employee
            NUMBER_OF_DONE_TASKS: number of completed tasks
            TOTAL_NUMBER_OF_TASKS: total number of tasks,
            which is the sum of completed and non-completed tasks
    Second and N next lines display the title of completed tasks:
    TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
from sys import argv as av
import requests as req


def getInfo():
    """gets information about an employees' TODO list progress."""
    base = 'https://jsonplaceholder.typicode.com/'
    # get employees personal info
    info = req.get(base + 'users/{}'.format(av[1])).json()
    todos = req.get(base + 'users/{}/todos'.format(av[1])).json()
    allTodo = len(todos)
    completedTasks = []
    count = 0
    for todo in todos:
        if todo['completed'] is True:
            count += 1
            completedTasks.append(todo['title'])
    print('Employee {} is done with tasks({}/{}):'
          .format(info['name'], count, allTodo))
    for task in completedTasks:
        print('\t' + task)


if __name__ == '__main__':
    getInfo()
