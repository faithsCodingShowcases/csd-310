
import mysql.connector
from mysql.connector import Error

config = {
    "user": "root",
    "password": "sesame",
    "host": "localhost",
    "database": "movies",
    "raise_on_warnings": True,
    "port": 3308

}
db = mysql.connector.connect(**config)
# Create a cursor object
cursor = db.cursor()

# Query 1: Select all the fields for the studio table
print("------- Select all the fields for the studio table--------")
cursor.execute("SELECT * FROM studio")
studios = cursor.fetchall()
for studio in studios:
    print("Studio ID: {}\n Studio Name: {}\n".format(studio[0], studio[1]))


print("------- Select all the fields for the genre table----------")
cursor.execute("SELECT * FROM genre")
genres = cursor.fetchall()
for genre in genres:
    print("Genre ID: {}\n Genre Name: {}\n".format(genre[0], genre[1]))

# Query 3: Select the movie names for those movies that have a run time of less than two hours
print("-------- Select the movie names for those movies that have a run time of less than two hours--------")
cursor.execute("SELECT film_name FROM film WHERE film_runtime < 120")
movies = cursor.fetchall()
for movie in movies:
    print("Movie Name: {}\n".format(movie[0]))

# Query 4: Get a list of film names, and directors ordered by director
print("-------- Get a list of film names, and directors ordered by director----------")
cursor.execute("SELECT film_name, film_director FROM film ORDER BY film_director")
movies = cursor.fetchall()
for movie in movies:
    print("Movie Name: {}\n Director: {}\n".format(movie[0], movie[1]))

db.close()
