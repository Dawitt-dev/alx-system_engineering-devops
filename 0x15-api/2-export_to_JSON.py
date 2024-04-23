#!/usr/bin/python3
"""
Gathers data from an API and exports TODO list progress for a given employee ID
in JSON format
"""
import json
import requests
from sys import argv


def gather_data(employee_id):
    """
    Retrieves and exports TODO list data for a given employee ID in JSON format
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todo_url = "{}/todos?userId={}".format(base_url, employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    dictionary = {employee_id: []}
    for task in todo_data:
        dictionary[employee_id].append({
                "task": task['title'],
                "completed": task['completed'],
                "username": user_data['username']
            })
    json_filename = "{}.json".format(employee_id)
    with open(json_filename, mode='w') as json_file:
        json.dump(dictionary, json_file)


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./2-export_to_JSON.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    gather_data(employee_id)
