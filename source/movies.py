from source.commons import *

import sqlite3

database = sqlite3.connect("moviesCGV.db")
databaseCursor = database.cursor()

def clearMovies():
	databaseCursor.execute('DELETE FROM movies')
	database.commit()

def initMovies(title, director, starring, critics, genre, year):
    databaseCursor.execute("""
                    INSERT INTO movies (m_title, m_director, m_starring, m_critics, m_genre, m_year) VALUES
                        (?, ?, ?, ?, ?, ?)
                    """, (title, director, starring, critics, genre, year))

    newId = databaseCursor.lastrowid

    database.commit()

    return newId

def uniqueMovieTitle(title):
    lookup = databaseCursor.execute("SELECT COUNT(*) FROM movies where m_title IS ?", (title,))
    return lookup.fetchone()[0] == 0

def addMovie(title, director, starring, critics, genre, year):
    databaseCursor.execute("""
                    INSERT INTO movies (m_title, m_director, m_starring, m_critics, m_genre, m_year) VALUES
                        (?, ?, ?, ?, ?, ?)
                    """, (title, director, starring, critics, genre, year))
    database.commit()

def deleteMovie(movieId):
    databaseCursor.execute("DELETE FROM movies WHERE m_movieId =?", (movieId, ))
    database.commit()

def editMovieCritics(movieId, critics):
    databaseCursor.execute("UPDATE movies SET m_critics =? WHERE m_movieId =?", (critics, movieId))
    database.commit()
