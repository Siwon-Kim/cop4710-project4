from commons import *

import sqlite3

database = sqlite3.connect("moviesCGV.db")
databaseCursor = database.cursor()

def uniqueUsername(username):
    lookup = databaseCursor.execute(
        "SELECT COUNT(*) FROM users where u_username IS ?", (username,))
    return lookup.fetchone()[0] == 0


def initAcct(username, password, firstname, lastname, email, isEmployee):
    databaseCursor.execute("""
                    INSERT INTO users (u_username, u_password, u_firstname, u_lastname, u_email, u_isEmployee) VALUES
                        (?, ?, ?, ?, ?, ?)
                    """, (username, password, firstname, lastname, email, isEmployee))

    newId = databaseCursor.lastrowid

    database.commit()

    return newId


def checkExistingAccts(username, password):
    databaseCursor.execute("SELECT * FROM users WHERE u_username= ? and u_password= ?",
                            (username, password))
    found = databaseCursor.fetchone()
    if found:
        return found[0]
    else:
        return -1


def checkisEmployee(username, password):
    databaseCursor.execute("SELECT * FROM users WHERE u_username= ? and u_password= ?",
                            (username, password))
    found = databaseCursor.fetchone()
    print(found)
    if found:
        return found[0]
    else:
        return -1


def checkExistingUsername(username):
    databaseCursor.execute("SELECT * FROM users WHERE u_username= ?",
                            (username,))
    found = databaseCursor.fetchone()
    if found:
        return found[0]
    else:
        return -1
