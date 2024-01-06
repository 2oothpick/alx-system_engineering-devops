#!/usr/bin/python3
"""
Script uses a given employee ID, and  returns
information about his/her TODO list progress
"""

if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    tasks_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    # response = requests.get(todos_url)
    username = requests.get(user_url)
    username_json = json.loads(username.text)
    all_tasks = requests.get(tasks_url)
    all_tasks_json = json.loads(all_tasks.text)
    task_counter = 0
    completed_counter = 0
    task_titles = []
    for tasks in all_tasks_json:
        task_counter += 1

        if tasks["completed"]:
            completed_counter += 1
            task_titles.append(tasks["title"])

    print(
        f"Employee {username_json['name']} is done with tasks\
        ({completed_counter}/{task_counter}):")
    for item in task_titles:
        print(f"\t {item}")
