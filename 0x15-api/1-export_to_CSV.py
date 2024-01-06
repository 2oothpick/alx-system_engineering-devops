#!/usr/bin/python3
"""
Script uses a given employee ID, and exports
information about his/her TODO list progress
CSV format.
"""

if __name__ == "__main__":
    import csv
    import json
    import requests
    from sys import argv

    tasks_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{argv[1]}"
    # response = requests.get(todos_url)
    user_info = requests.get(user_url)
    user_info_json = json.loads(user_info.text)
    all_tasks = requests.get(tasks_url)
    all_tasks_json = json.loads(all_tasks.text)
    task_counter = 0
    completed_counter = 0
    task_titles = []
    filename = f"{argv[1]}.csv"
    with open(filename, 'w', newline='') as file:
        for tasks in all_tasks_json:
            task_counter += 1

            csv_list = [argv[1], user_info_json['username'],
                        tasks["completed"], tasks['title']]
            # print(csv_list)
            csv_file = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
            csv_file.writerow(csv_list)
