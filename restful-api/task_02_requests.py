#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    if request.status_code == 200:
        print("Status Code: ",request.status_code)
    response = request.json()
    for i in response:
        print(i["title"])

def fetch_and_save_posts():
    request = requests.get("https://jsonplaceholder.typicode.com/posts")
    response = request.json()
    with open("posts.csv", "W", newline="") as file:
        names = ["id", "title", "body"]
        my_file = csv.DictWriter(file, fieldnames=names)
        writer.writeheader()
        for i in response:
            writer.writeheader({"id": i["id"],
                "title": i["title"],
                "body": i["body"]})
