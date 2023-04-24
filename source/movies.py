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

def allMovieList():
    databaseCursor.execute("SELECT * FROM movies;")
    return databaseCursor

def searchTitle(title):
    databaseCursor.execute("SELECT * FROM movies WHERE m_title=?", (title, ))
    return databaseCursor

def searchDirector(director):
    databaseCursor.execute("SELECT * FROM movies WHERE m_director=?", (director, ))
    return databaseCursor

def searchGenre(genre):
    databaseCursor.execute("SELECT * FROM movies WHERE m_genre=?", (genre, ))
    return databaseCursor

def searchYear(year):
    databaseCursor.execute("SELECT * FROM movies WHERE m_year=?", (year, ))
    return databaseCursor

def printSearchResult(cursor):
    search_result = 0
    for row in cursor:
        print("------------------------------")
        print("MovieID:", row[0])
        print("Title:", row[1])
        print("Director:", row[2])
        print("Starring:", row[3])
        print("Critics:", row[4])
        print("Genre:", row[5])
        print("Year:", row[6])
        print("------------------------------")
        search_result += 1
    
    return search_result

def printWatchedMovie(asId):
    search_result = 0
    databaseCursor.execute("SELECT m.m_movieId, m.m_title, w.w_date FROM movies AS m JOIN watched AS w ON m.m_movieId = w.w_m_movieId WHERE w.w_u_username = ?", (asId, ))
    for row in databaseCursor:
        print("------------------------------")
        print("MovieID:", row[0])
        print("Title:", row[1])
        print("Watched Date:", row[2])
        print("------------------------------")
        search_result += 1
    
    return search_result

def addWatchedMovie(asId):
    movieId = gatherInput("\nEnter the movieID you want to add: ", "", vacuouslyTrue)
    date = gatherInput("\nEnter the watched date (YYYY-MM-DD): ", "", vacuouslyTrue)
    databaseCursor.execute("INSERT INTO watched (w_u_username, w_m_movieId, w_date) VALUES (?, ?, ?)", (asId, movieId, date))
    database.commit()