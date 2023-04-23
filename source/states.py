from source.commons import *
from source.database import *
from source.accounts import *
from source.movies import *
from source.authentication import *
from source.api import *


#####################################
###          Main States          ###
#####################################


def applicationEntry():
    welcomeMessage = '''
    **********************************************************************
    ***                                                                ***
    ***                                                                ***
    ***       Welcome to the CGV - Movie List Management System        ***
    ***                                                                ***
    ***                                                                ***
    **********************************************************************
    '''
    print(welcomeMessage)

    prompt = "Please select an option below:\n"\
        "\t1. Log in to an existing account\n"\
        "\t2. Create a new account\n"\
        "\t3. Exit\n"\
        "Selection: "
    sel = int(gatherInput(prompt, "Invalid input. Please try again.\n",
                            menuValidatorBuilder('123')))

    if sel == 1:
        clear()
        return login, None

    elif sel == 2:
        clear()
        return newAcct, None

    elif sel == 3:
        clear()
        exit()


def employeeMainInterface(asId):
    prompt = "Please select an option below:\n"\
        "\t1. View movie list\n"\
        "\t2. Add movie to database \n"\
        "\t3. Edit movies\n"\
        "\t4. Delete movies\n"\
        "\t5. My profile\n"\
        "\t6. Log out\n"\
        "Selection: "
    sel = int(
        gatherInput(prompt, "Invalid input. Please try again.\n",
                    menuValidatorBuilder('1234567')))

    if sel == 1:
        clear()
        return movieListInterface, (asId,)

    elif sel == 2:
        clear()
        return addMovieInterface, (asId,)

    elif sel == 3:
        clear()
        return editMovieInterface, (asId,)

    elif sel == 4:
        clear()
        return deleteMovieInterface, (asId,)

    elif sel == 5:
        clear()
        return myProfile, (asId,)

    elif sel == 6:
        clear()
        return applicationEntry, None


def customerMainInterface(asId):
    prompt = "Please select an option below:\n"\
        "\t1. View all movies\n"\
        "\t2. Search movies\n"\
        "\t3. View your watched movie list\n"\
        "\t4. My profile\n"\
        "\t5. Log out\n"\
        "Selection: "
    sel = int(
        gatherInput(prompt, "Invalid input. Please try again.\n",
                    menuValidatorBuilder('1234567')))

    if sel == 1:
        clear()
        return movieListInterface, (asId,)

    elif sel == 2:
        clear()
        return searchMovieInterface, (asId,)

    elif sel == 3:
        clear()
        return watchedMovieInterface, (asId,)

    elif sel == 4:
        clear()
        return myProfile, (asId,)

    elif sel == 5:
        clear()
        return applicationEntry, None


#####################################
###    Account-related States     ###
#####################################


def login():
    if dbEmpty():
        print("\n\nNo existing accounts. Please create a new account.\n")
        return applicationEntry, None

    else:
        username = input("Username: ")
        password = input("Password: ")

        id, isEmployee = checkExistingAccts(username, password)

        if id != -1 and isEmployee:
            clear()
            print("\n\nYou have successfully logged in as an employee\n")
            return employeeMainInterface, (id,)

        if id != -1:
            clear()
            print("\n\nYou have successfully logged in as a client\n")
            return customerMainInterface, (id,)

        else:
            clear()
            print("\n\nIncorrect username/password. Please try again.\n")
            return applicationEntry, None


def newAcct():
    username = gatherInput(
        "Enter a username: ",
        "Username already exists. Please try again.",
        uniqueUsername)

    password = gatherInput(
        "\nPassword must meet the following requirements:\n"
        "\t-Length of 8-12 characters\n"
        "\t-Contain one capital letter\n"
        "\t-Contain one digit\n"
        "\t-Contain one of the following special characters: !, @, #, $, %, ^, &, *\n"
        "\nPassword: ",
        "Password does not meet security requirements",
        passwordValidator)

    firstname = gatherInput("\nEnter your first name:\n", "", vacuouslyTrue)
    lastname = gatherInput("\nEnter your last name: \n", "", vacuouslyTrue)
    email = gatherInput("\nEnter your email: \n", "", vacuouslyTrue)

    clear()
    return customerMainInterface, (initAcct(username, password, firstname, lastname, email, 0),)


def myProfile(asId):
    pass


#####################################
###      Movie-related States     ###
#####################################


def movieListInterface(asId):
    pass


def addMovieInterface(asId):
    title = gatherInput(
                "Enter a movie title: ",
                "Movie already exists on database.",
                uniqueMovieTitle).lower()
    director = gatherInput("\nEnter the director:\n", "", vacuouslyTrue)
    starring = gatherInput("\nEnter the starring: \n", "", vacuouslyTrue)
    critics = gatherInput("\nEnter the critics: \n", "", vacuouslyTrue)
    genre = gatherInput("\nEnter the genre: \n", "", vacuouslyTrue).lower()
    year = gatherInput("\nEnter the year: \n", "", vacuouslyTrue)

    addMovie(title, director, starring, critics, genre, year)

    clear()
    print("The movie is successfully added\n")

    return employeeMainInterface, (asId,)



def editMovieInterface(asId):
    movieId = gatherInput("\nEnter the movie ID you want to edit:\n", "", vacuouslyTrue)
    critics = gatherInput("\nEnter the critics: \n", "", vacuouslyTrue)

    editMovieCritics(movieId, critics)

    clear()
    print("The critics is successfully edited\n")

    return employeeMainInterface, (asId,)



def deleteMovieInterface(asId):
    movieId = gatherInput("\nEnter the movie ID you want to delete:\n", "", vacuouslyTrue)

    deleteMovie(movieId)

    clear()
    print("The movie is successfully deleted\n")

    return employeeMainInterface, (asId,)


def searchMovieInterface(asId):
    pass


def watchedMovieInterface(asId):
    pass


#####################################
###          Other States         ###
#####################################


def exitState(asId):
    clear()
    print("Goodbye")
    exit()


def stateLoop(state):
    data = None
    while (state is not exitState):
        if data is None:
            state, data = state()
        else:
            state, data = state(*data)


if (__name__ == "__main__"):
    stateLoop(applicationEntry)
