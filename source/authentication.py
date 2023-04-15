from commons import *
from database import *
from main import *

def login():
    if dbEmpty():
        print("\n\nNo existing accounts. Please create a new account.\n")
        return applicationEntry, None

    else:
        username = input("Username: ")
        password = input("Password: ")
    
        id = checkExistingAccts(username, password)

        if (id != -1):
            clear()
            print("\n\nYou have successfully logged in\n")
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
                "\nPassword must meet the following requirements:\n"\
                "\t-Length of 8-12 characters\n"\
                "\t-Contain one capital letter\n"\
                "\t-Contain one digit\n"\
                "\t-Contain one of the following special characters: !, @, #, $, %, ^, &, *\n"\
                "\nPassword: ",
                "Password does not meet security requirements",
                passwordValidator)

    firstname = gatherInput("\nEnter your first name:\n", "", True)
    lastname = gatherInput("\nEnter your last name: \n", "", True)
    university = gatherInput("\nEnter your university (if no, enter NONE): \n", "", True)
    major = gatherInput("\nEnter your major (if no, enter NONE): \n", "", True)
    membership =  gatherInput("\nChoose your membership (Standard or Plus): \n"\
                                "\n\tStandard can't send message to stranger."\
                                "\n\tPlus can send message to everyone."\
                                "\nEnter your membership choice (standard or plus): ", "", True)


    clear()

    return mainInterface, (initAcct(username, password, firstname, lastname, university, major, membership),)


def passwordValidator(password):
    c, d, s = 0, 0, 0
    length = len(password)
    if length > 7 and length < 13:
        for i in password:
            if i.isupper():
                c += 1
            if i.isdigit():
                d += 1
            if i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*':
                s += 1

    if c > 0 and d > 0 and s > 0:
        return True
    else:
        return False