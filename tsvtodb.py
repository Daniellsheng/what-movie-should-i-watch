import sqlite3 as sql
import csv

con = sql.connect("movies.db")
cur = con.cursor()
cur.execute("CREATE TABLE MoviesTable (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres);")

with open('movies.tsv', 'r', encoding ='utf8') as movies:
    dr = csv.DictReader(movies, delimiter="\t")
    to_db = to_db = [(i['tconst'], i['titleType'], i['primaryTitle'], i['originalTitle'], i['isAdult'], i['startYear'], i['endYear'], i['runtimeMinutes'], i['genres']) for i in dr]


cur.executemany("INSERT INTO  MoviesTable (tconst, titleType, primaryTitle, originalTitle, isAdult, startYear, endYear, runtimeMinutes, genres) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);", to_db)
con.commit()
con.close()