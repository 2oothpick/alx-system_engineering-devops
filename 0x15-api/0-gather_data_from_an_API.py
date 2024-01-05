#!/usr/bin/python3
"""
Script uses a given employee ID, and  returns
information about his/her TODO list progress
"""

import requests
from sys import argv


if __name__ == "__main__":
    sessrequest = requests.Session()
    idEmp = argv[1]
    idURL = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(idEmp)
    nameURL = 'https://jsonplaceholder.typicode.com/users/{}'.format(idEmp)

    emp = sessrequest.get(idURL)
    empName = sessrequest.get(nameURL)

    json_req = emp.json()
    name = empName.json()['name']

    tasks = 0
    for done_tasks in json_req:
        if done_tasks['completed']:
            tasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, tasks, len(json_req)))

    for done_tasks in json_req:
        if done_tasks['completed']:
            print("\t " + done_tasks.get('title'))
