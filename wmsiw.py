from flask import Flask, render_template, redirect
import requests
import json
import csv
import random
import config

app = Flask(__name__)

endpoint = "http://www.omdbapi.com/?i="  #tt3896198
apikey = config.apikey


#select * from MoviesTable WHERE genres = "Comedy" ORDER BY RANDOM() LIMIT 1;
def getrandomID():
    r = random.randint(0, 645997)
    with open('movies.tsv', encoding = 'utf8') as movies:
        reader = csv.reader(movies, delimiter='\t')
        rows = list(reader)
        return rows[r][0]

@app.route("/random")
def randomMovie():
    randID = getrandomID()
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


