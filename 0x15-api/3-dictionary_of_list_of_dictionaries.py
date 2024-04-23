#!/usr/bin/python3
"""
Gathers data from an API and exports TODO list progress for all employees in
JSON format
"""
import json
import requests
import sys


def gather_data():
    """
    Retrieves and exports TODO list data for all employees in JSON format
    """
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    user_response = requests.get(users_url)
    users_data = user_response.json()

    dictionary = {}
    tasks_data = {}
    for user in users_data:
        user_id = str(user['id'])
        user_todos_response = requests.get(todos_url + "?userId=" + user_id)
        user_todos_data = user_todos_response.json()

        dictionary[user_id] = []
        for todo in user_todos_data:
            dictionary[user_id].append({
                "username": user['username'],
                "task": todo['title'],
                "completed": todo['completed']
            })

    file_name = "todo_all_employees.json"
    with open(file_name, mode='w') as json_file:
        json.dump(dictionary, json_file)


if __name__ == "__main__":
    gather_data()
