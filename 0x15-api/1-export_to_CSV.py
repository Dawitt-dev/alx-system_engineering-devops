#!/usr/bin/python3
"""
Gathers data from an API and exports TODO list progress for a given
employee ID in CSV format
"""
from sys import argv
import requests
import csv


def gather_data(employee_id):
    """
    Retrieves and exports TODO list data for a given employee ID in CSV format
    """
    user_url = ("https://jsonplaceholder.typicode.com/users/{}"
                .format(employee_id))
    todo_url = ("https://jsonplaceholder.typicode.com/todos?userId={}"
                .format(employee_id))

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    # Create a CSV file for the user
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME",
                             "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write tasks data
        for task in todo_data:
            csv_writer.writerow([user_data['id'], user_data['username'],
                                 str(task['completed']), task['title']])

    print(f"Tasks exported to {csv_filename}")


if __name__ == "__main__":
    if len(argv) != 2 or not argv[1].isdigit():
        print("Usage: ./1-export_to_CSV.py <employee_id>")
        exit(1)

    employee_id = int(argv[1])
    gather_data(employee_id)
