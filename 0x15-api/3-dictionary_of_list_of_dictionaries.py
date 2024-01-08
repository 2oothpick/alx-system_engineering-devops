#!/usr/bin/python3
"""
Script returns all information about users
TODO list progress
and exports data in the json format.
"""

if __name__ == "__main__":
    import json
    import requests

    tasks_url = f"https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users"

    user_info_json = json.loads(requests.get(user_url).text)
    all_tasks_json = json.loads(requests.get(tasks_url).text)

    filename = "todo_all_employees.json"
    json_dict = {}

    with open(filename, 'w', newline='') as file:
        for user in user_info_json:
            task_list = []
            json_dict.update({user['id']: task_list})
            for tasks in all_tasks_json:
                if user['id'] == tasks['userId']:
                    task_list.append({"username": user["username"],
                                      "task": tasks['title'],
                                      "completed": tasks.get('completed')
                                      })
        json.dump(json_dict, file)
