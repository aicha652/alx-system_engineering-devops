#!/usr/bin/python3
"""Python script to export data in the CSV format."""
import csv
import requests
import sys


if __name__ == '__main__':

    employee_id = sys.argv[1]
    url = 'https://jsonplaceholder.typicode.com'

    user_data = requests.get('{}/users/{}'.format(url, employee_id))
    todo_data = requests.get('{}/todos?userId={}'.format(url, employee_id))

    # Create a CSV file
    csv_filename = "{}.csv".format(employee_id)
    user = user_data.json()
    todos = todo_data.json()

    username = user.get("name")

    with open(csv_filename, "w") as f:
        for todo in todos:
            TASK_COMPLETED_STATUS = todo["completed"]
            TASK_TITLE = todo["title"]
            csv_data = (
                    f'"{employee_id}",'
                    f'"{username}",'
                    f'"{TASK_COMPLETED_STATUS}",'
                    f'"{TASK_TITLE}"\n'
                    )
            f.write(csv_data)
