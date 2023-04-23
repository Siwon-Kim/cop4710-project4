from source.commons import *

import sqlite3

database = sqlite3.connect("moviesCGV.db")
databaseCursor = database.cursor()


databaseCursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            u_userId INTEGER PRIMARY KEY ASC, 
                            u_username TEXT, 
                            u_password TEXT,
                            u_firstname TEXT,
                            u_lastname TEXT,
                            u_email TEXT,
                            u_isEmployee INTEGER)''')
database.commit()


databaseCursor.execute('''Create TABLE IF NOT EXISTS movies (
                            m_movieId INTEGER PRIMARY KEY ASC,
                            m_title TEXT,
                            m_director TEXT,
                            m_starring TEXT,
                            m_critics TEXT,
                            m_genre TEXT,
                            m_year INTEGER)''')
database.commit()


databaseCursor.execute('''CREATE TABLE IF NOT EXISTS watched (
                            w_u_username TEXT,
                            w_m_movieId INTEGER,
                            w_date TEXT,
                            FOREIGN KEY(w_u_username) REFERENCES users(u_username),
                            FOREIGN KEY(w_m_movieId) REFERENCES movies(m_movieId))''')
database.commit()


# ----------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------


def tableEntriesCount(table):
    '''
    Generates a function that returns the number of rows in a given table
    param table: a case-sensitive string of the name of a table that is to have its rows counted
    return: A lambda f() = number of rows in table
    '''
    return lambda: (databaseCursor.execute("SELECT Count(*) FROM " + table).fetchone()[0])


userCount = tableEntriesCount("users")
movieCount = tableEntriesCount("movies")


def dbEmpty():
	if (userCount() == 0):
		return True
	else:
		return False