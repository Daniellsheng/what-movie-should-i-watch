from flask import Flask, render_template, redirect
import requests
import json
import csv
import random

app = Flask(__name__)

endpoint = "http://www.omdbapi.com/?i="  #tt3896198
apikey = ""

def getrandomID():
    r = random.randint(0, 645997)
    with open('movies.tsv', encoding = 'utf8') as movies:
        reader = csv.reader(movies, delimiter='\t')
        rows = list(reader)
        print(rows[r][0])
        return rows[r][0]


@app.route("/")
def hello():
    randID = getrandomID()
    response = requests.get(url = endpoint + randID + apikey)

    data = response.json()
    print(data)
    print(data['Title'])
    return "helo"

if __name__ == "__main__":
    app.run()


