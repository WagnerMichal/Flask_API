from db import connect_db
import sqlite3
from flask import Response


def get_movies():
    movies = []
    try:
        connect = connect_db()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()

        for row in rows:
            movie = {}
            movie["id"] = row["id"]
            movie["title"] = row["title"]
            movie["description"] = row["description"]
            movie["release_year"] = row["release_year"]
            movies.append(movie)

    except sqlite3.Error as error:
        Response(error)
    finally:
        connect.close()

    return movies


def get_by_id(id):
    movie = {}
    try:
        connect = connect_db()
        cursor = connect.cursor()
        cursor.execute("SELECT * FROM movies WHERE id = ?", [id])
        row = cursor.fetchone()

        movie["id"] = row["id"]
        movie["title"] = row["title"]
        movie["description"] = row["description"]
        movie["release_year"] = row["release_year"]

    except:
        movie = {}

    finally:
        connect.close()

    return movie


def insert_movie(movie):
    inserted_movie = {}
    try:
        connect = connect_db()
        cursor = connect.cursor()
        statement = "INSERT INTO movies (title, description, release_year) VALUES (?, ?, ?)"
        cursor.execute(
            statement, (movie['title'], movie['description'], movie['release_year']))
        connect.commit()
        inserted_movie = get_by_id(cursor.lastrowid)
    except:
        connect().rollback()

    finally:
        connect.close()

    return inserted_movie


def update_movie_by_id(movie, id):
    updated_movie = {}
    try:
        connect = connect_db()
        cursor = connect.cursor()
        statement = "UPDATE movies SET title = ?, description = ?, release_year = ? WHERE id = ?"
        cursor.execute(
            statement, (movie["title"], movie["description"], movie["release_year"], id))
        connect.commit()
        updated_movie = get_by_id(id)

    except:
        connect.rollback()

    finally:
        connect.close()

    return updated_movie
