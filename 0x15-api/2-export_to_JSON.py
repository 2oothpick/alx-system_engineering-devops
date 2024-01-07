#!/usr/bin/python3
"""
Script uses a given employee ID, and  returns
information about his/her TODO list progress
and exports data in the JSON format.
"""


if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    tasks_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"

    user_info = requests.get(user_url)
    all_tasks = requests.get(tasks_url)

    user_info_json = json.loads(user_info.text)
    all_tasks_json = json.loads(all_tasks.text)

    task_titles = []
    filename = f"{argv[1]}.json"
    task_list = []
    json_dict = {f"{argv[1]}": task_list}
    with open(filename, 'w', newline='') as file:
        for tasks in all_tasks_json:
            task_list.append({"task": tasks['title'],
                              "completed": tasks.get('completed'),
                              "username": user_info_json["username"]
                              })
        json.dump(json_dict, file)
