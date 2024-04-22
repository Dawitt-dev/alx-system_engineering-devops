#!/usr/bin/python3
"""
Gathers data from API and displays TODO list progress for a given employee ID
"""
import requests
from sys import argv


def gather_data(employee_id):
	"""
	Retrieves TODO list data for a given employee ID
	"""	
    u_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    t_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)

    user_response = requests.get(u_url)
    todo_response = requests.get(t_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    total_tasks = len(todo_data)
    done_tasks = [task for task in todo_data if task['completed']]

    print("Employee {} is done with tasks({}/{}):".format(user_data['name'], len(done_tasks), total_tasks))
    for task in done_tasks:
        print("\t {}".format(task['title']))


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./0-gather_data_from_an_API.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    gather_data(employee_id)
