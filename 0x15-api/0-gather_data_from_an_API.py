#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee
ID, returns information about his/her TODO list progress"""
import requests
import sys


if __name__ == '__main__':
    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user_data = requests.get("{}/users/{}".format(url, employee_id))
    todo_data = requests.get("{}/todos/{}".format(url, employee_id))

    user = user_data.json()
    todos = todo_data.json()

    employee_name = user.get('name')

    completed_tasks = []
    for task in todos:
        if task["completed"] is True:
            completed_tasks.append(task["title"])

    number_tasks = len(todos)

    print('Employee {} is done with tasks({}/{}):'.format(employee_name,
                                                          len(completed_tasks),
                                                          number_tasks))

    for task in completed_tasks:
        print("\t {}".format(task))
