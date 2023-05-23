#!/usr/bin/python3

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    todos = requests.get(url + "todos", params={"userId: sys.argv[1]"}).json()

    complete = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"), len(completed), len(todos)))
    [print("\t {}".format(c)) for c in completed]



    # employeeId = sys.argv[1]
    # base_url = "https://jsonplaceholder.typicode.com/user"
    # url = base_url + "/" + employeeId

    # response = requests.get(url)
    # employee_name = response.json().get('name')

    # todo_url = url + "/todos"
    # response = requests.get(todo_url)
    # tasks = response.json()
    # done = 0
    # done_task = []

    # for task in tasks:
    #     if task.get('completed'):
    #         done_tasks.append(task)
    #         done = done + 1

    # print(f"{employee_name} has {done} done tasks".format(employee_name, done, len(tasks)))

    # for task in done_task:
    #     print("\t {}".format(task.get('title')))