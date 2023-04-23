from os.path import exists
import os.path

from source.accounts import checkExistingUsername, initAcct, clearUsers
from source.movies import initMovies, clearMovies
from source.authentication import passwordValidator


def employeeListAPI():
    clearUsers() # initialize Users table

    absPath = os.path.abspath(os.path.dirname(__file__))
    txtFilePath = os.path.join(absPath, "APIs", "employees.txt")
    fileExists = exists(txtFilePath)

    if fileExists:
        with open(txtFilePath) as f:
            lines = f.read()
            employees = lines.split('\n')

            for e in employees:
                if e == "":
                    break

                e = e.split(" ")

                username = e[0].lower()
                password = e[1]
                firstname = e[2]
                lastname = e[3]
                email = e[4].lower()

                if checkExistingUsername(username) and passwordValidator(password):
                    initAcct(username, password, firstname, lastname, email, 1)


def movieListAPI():
    clearMovies() # initialize Movies table

    absPath = os.path.abspath(os.path.dirname(__file__))
    txtFilePath = os.path.join(absPath, "APIs", "movies.txt")
    fileExists = exists(txtFilePath)

    if fileExists: 
        with open(txtFilePath) as f:
            lines = f.read()
            movies = lines.split('\n')

            for m in movies:
                if m == "":
                    break
                m = m.split("/")
                title = m[0].lower()
                director = m[1]
                starring = m[2]
                critics = m[3]
                genre = m[4].lower()
                year = m[5]

                initMovies(title, director, starring, critics, genre, year)