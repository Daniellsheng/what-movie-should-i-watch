from flask import Flask, render_template, redirect, request
import requests
import json
import csv
import random
import config
import sqlite3 as sql

app = Flask(__name__)

endpoint = "http://www.omdbapi.com/?i="  #tt3896198
apikey = config.apikey


def getRandomIDSQL_genre(genre):
    con = sql.connect("movies.db")
    cur = con.cursor()
    cur.execute("select * from MoviesTable WHERE genres = ? ORDER BY RANDOM() LIMIT 1", [genre])
    data = cur.fetchall()
    print("sql", data[0][0])
    con.close()
    return data[0][0]           #returns the IMDB ID of a movie

def getRandomIDSQL():
    con = sql.connect("movies.db")
    cur = con.cursor()
    cur.execute("select * from MoviesTable ORDER BY RANDOM() LIMIT 1")
    data = cur.fetchall()
    print("sql", data[0][0])
    con.close()
    return data[0][0]   

@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/random/")
def randomMovie():
    genre_query = request.args.get("genre")
    print(genre_query)

    if genre_query is None:
        randID = getRandomIDSQL()
    else:
        randID = getRandomIDSQL_genre(genre_query)

    response = requests.get(url = endpoint + randID + apikey)
    data = response.json()
  
    print(data)
    if data['Response'] == 'False':
        print("Movie does not exist")
        redirect("/random")
        # randomMovie()
    else:
        title = data['Title']
        year = data['Year']
        genre = data['Genre']
        director = data['Director']
        poster = data['Poster']
        rating = data['imdbRating']
        rated = data['Rated']
        url = "https://imdb.com/title/" + data['imdbID']
        actors = data['Actors']
        lang = data['Language']

    return render_template("movie.html", title = title, 
                                         year = year, 
                                         genre = genre, 
                                         director = director, 
                                         poster = poster, 
                                         rating = rating, 
                                         rated = rated, 
                                         url = url, 
                                         actors = actors,
                                         lang = lang
                                         )       

@app.route("/")
def hello():
    return render_template("index.html")

if __name__ == "__main__":
    app.run()


