#Faith Siebert
#11/21/2023
#Module 8
# Program connects to a database then preforms a select, update, insert, and delete statement.
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
title = "DISPLAYING FILMS"

#shows records
def show_films(cursor, title):

    cursor.execute("select film_name as Name, film_director as Director, genre_name as Genre, studio_name as 'StudioName' from film INNER JOIN genre ON film.genre_id=genre.genre_id INNER JOIN studio ON film.studio_id=studio.studio_id")

    films = cursor.fetchall()

    print("\n  -- {} --".format(title))

    for film in films:
        print("Film Name: {}\nDirector: {}\nGenre Name ID: {}\nStudio Name: {}\n".format(film[0], film[1], film[2], film[3]))

show_films(cursor, title)

title = "DISPLAYING FILMS AFTER INSERT"

#inserts record
cursor.execute("INSERT INTO film(fiLm_name, film_releaseDate, fiLm_runtime, film_director,studio_id, genre_id) VALUES('The Purge','2013','85','James DeMonaco', 1,1)")

show_films(cursor, title)

title = "DISPLAYING FILMS AFTER UPDATE= CHanged Alien to Horror"

#updates record
cursor.execute("UPDATE film SET genre_id = '1' WHERE film_name = 'Alien'")

show_films(cursor, title)

title = "DISPLAYING FILMS AFTER DELETE"

#deletes record
cursor.execute("DELETE FROM film WHERE film_name ='Gladiator'")

show_films(cursor, title)