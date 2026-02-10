#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    if req.status_code == 200:
        print(req.status_code)
    res = req.json()
    for i in res:
        print(i["title"])

def fetch_and_save_posts():
    req = requests.get("https://jsonplaceholder.typicode.com/posts")
    res = req.json()
    with open("posts.csv", "W", newline="") as file:
        names= ["id", "title", "body"]
        my_file = csv.DictWriter(file, fieldnames=names)
        writer.writeheader()
        for post in res:
            writer.writeheader({"id": post["id"],
                "title": post["title"],
                "body": post["body"]})
