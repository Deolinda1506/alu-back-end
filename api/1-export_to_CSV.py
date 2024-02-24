#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export
data in the CSV format.

Requirements:

~ Records all tasks that are owned by this employee
~ Format must be:
"USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
~ File name must be: USER_ID.csv
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
    # a single variable used to accept the response
    # after request is made using the module
    req_rep1 = requests.get(url1, params=payload)
    req_rep2 = requests.get(url2)
    req_rep1 = req_rep1.json()
    req_rep2 = req_rep2.json()
    # file name depends on id
    filename = f"{sys.argv[1]}.csv"
    with open(filename, 'w', newline='') as csvfile:
        # create a csv writer object
        data_writer = csv.writer(csvfile, delimiter=",", quotechar='"',
                                 quoting=csv.QUOTE_ALL)
        # iterate through the first request only and use the value of some key
        # and use the username of the second request for every iteration
        for data in req_rep1:
            data_writer.writerow([data["userId"], req_rep2["username"],
                                 data["completed"], data["title"]])
