#!/usr/bin/python3
"""
A Python script, using this REST API,
https://jsonplaceholder.typicode.com/path/?query#fragments
for a given employee ID, returns information about his/her
TODO list progress.

Requirements:
~You  must use urllib or requests module
~The script must accept an integer as a parameter,
which is the employee ID
~The script must display on the standard output the
employee TODO list progress in this exact format:

First line: Employee EMPLOYEE_NAME is done with
tasks(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
EMPLOYEE_NAME: name of the employee
NUMBER_OF_DONE_TASKS: number of completed tasks
TOTAL_NUMBER_OF_TASKS: total number of tasks, which is
the sum of completed and non-completed tasks

Second and N next lines display the title of completed tasks:
TASK_TITLE (with 1 tabulation and 1 space before the TASK_TITLE)
"""
if __name__ == "__main__":
    import json
    import sys
    import urllib.request

    """
    Then format the employees id with the url
    https://jsonplaceholder.typicode.com/users/{employees_id}
    after getting it from the command line using the sys module
    """
    employee_id = sys.argv[1]
    url1 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{employee_id}/"
    # create a request objects at first using urllib.request.Request()
    req_object1 = urllib.request.Request(url1, method="GET")
    req_object2 = urllib.request.Request(url2, method="GET")
    # fetch the resources using the request objects and the function
    # urllib.request.urlopen
    with urllib.request.urlopen(req_object1) as response_object1:
        response1 = json.load(response_object1)
    with urllib.request.urlopen(req_object2) as response_object2:
        response2 = json.load(response_object2)
    # create an empty list to store completed tasks
    completed_tasks = []
    # iterate through all task to get task with boolean value true
    for task in response1:
        if task['completed'] is not True:
            continue
        completed_tasks.append(task)
    # get length for completed task and all task (complete and incomplete)
    no_of_comptasks = len(completed_tasks)
    totalno_of_task = len(response1)
    # get the employee name
    employee_name = response2["name"]
    # display the required format in the docs
    print(f"Employee {employee_name} is done with tasks({no_of_comptasks}/\
{totalno_of_task}):")
    for comp_tasks in completed_tasks:
        print(f"\t {comp_tasks['title']}")
