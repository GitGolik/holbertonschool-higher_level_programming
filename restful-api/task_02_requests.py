#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    """fetch all posts from Jsonplaceholder and print titles"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    # display status
    print(f"Status Code: {response.status_code}")

    # if request granted
    if response.status_code == 200:
        posts = response.json()
        
        for post in posts:
            print(post["title"])

def fetch_and_save_posts():
    """fetch all posts and save id , body and title in a csv file"""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()

        #create a list of dict of id, title, body
        data = [
            {
                "id": post["id"],
                "title": post["title"],
                "body": post["body"],
            }
            for post in posts
        ]

        # write the file
        filename = "posts.csv"
        with open(filename, "w", newline="", encoding="utf-8") as f:
            fieldnames = ["id", "title", "body"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerows(data)