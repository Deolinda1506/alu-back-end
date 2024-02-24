#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the JSON format.

Requirements:

~ Records all tasks that are owned by
this employee
~ Format must be: { "USER_ID":
[{"task": "TASK_TITLE", "completed":
~ TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS, "username":
"USERNAME"}, ... ]} File name must be:
USER_ID.json
"""
if __name__ == "__main__":
    import csv
    import json
    import requests
    import sys
    # using this url https://jsonplaceholder.typicode.com/todos/
    # add a query string of userId = 2 using the requests module
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = f"https://jsonplaceholder.typicode.com/users/{sys.argv[1]}"
    payload = {"userId": sys.argv[1]}
    # a sinle variable used to accept the response
    # after request is made using the module
    req_rep1 = requests.get(url1, params=payload)
    req_rep2 = requests.get(url2)
    req_rep1 = req_rep1.json()
    req_rep2 = req_rep2.json()
    # file name depends on id
    filename2 = f"{sys.argv[1]}.json"
    # create a dictionary having the key "userid" and
    # the value should be an  empty list
    user_data = {f'{req_rep2["id"]}': []}
    # now get the keys of the user
    user_keys = list(req_rep1[0].keys())
    # now iterate over req_rep1 and req_rep2 to get
    # to get a dictionary of task/title, completeted, username
    # key value pairs
    for data in req_rep1:
        new_dict = {}
        for key in user_keys:
            if key != "title" and key != "completed":
                continue
            if key == "title":
                new_dict["task"] = data[key]
            else:
                new_dict[key] = data[key]
        new_dict["username"] = req_rep2["username"]
        user_data.get(f"{sys.argv[1]}").append(new_dict)
    with open(filename2, 'w', encoding='utf-8') as jsonfile:
        json.dump(user_data, jsonfile)
