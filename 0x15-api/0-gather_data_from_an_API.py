#!/usr/bin/python3

import requests
import sys

if __name__ == '__main__':
    employeeId = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com/user"
    url = base_url + "/" + employeeId

    response = requests.get(url)
    employee_name = response.json().get('name')

    todo_url = url + "/todos"
    response = requests.get(todo_url)
    tasks = response.json()
    done = 0
    done_task = []

    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done = done + 1

    print(f"{employee_name} has {done} done tasks".format(employee_name, done, len(tasks)))

    for task in done_task:
        print("\t {}".format(task.get('title')))