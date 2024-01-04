#!/usr/bin/python3
"""python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == '__main__':

    user_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com/'

    user_data = requests.get('{}/users/{}'.format(url, user_id))
    todos_data = requests.get('{}/todos?userId={}'.format(url, user_id))

    user = user_data.json()
    todos = todos_data.json()

    username = user.get('username')

    listTodos = []
    for todo in todos:
        listTodos.append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": username
            })

    with open('{}.json'.format(user_id), "w") as file:
        json_data = {user_id: listTodos}
        file.write(json.dumps(json_data))
