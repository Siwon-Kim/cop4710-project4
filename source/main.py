from commons import *
from database import *
from movies import *
from authentication import *
from account import *


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
            "Selection: "
    sel = int(gatherInput(prompt, "Invalid input. Please try again.\n",
                    menuValidatorBuilder('12')))
    
    if sel == 1:
        clear()
        return login, None

    elif sel == 2:
        clear()
        return newAcct, None


def employeeMainInterface(asId):
#   usersAPI()
    prompt = "Please select an option below:\n"\
            "\t1. View movie list\n"\
            "\t2. Add movie to database \n"\
            "\t3. Edit movies\n"\
            "\t4. Delete movies\n"\
            "\t5. Manage customer information\n"\
            "\t6. My profile\n"\
            "\t7. Log out\n"\
            "Selection: "
    sel = int(
            gatherInput(prompt, "Invalid input. Please try again.\n",
                        menuValidatorBuilder('1234567')))
    
    if sel == 1:
        clear()
        return jobInterface, (asId,)

    elif sel == 2:
        clear()
        return findFriendsbyType, (asId,)

    elif sel == 3:
        clear()
        return friendsList, (asId,)

    elif sel == 4:
        clear()
        return listSkills, (asId,)

    elif sel == 5:
        clear()
        return inCollegeGroups, (asId,)
        
    elif sel == 6:
        clear()
        return myProfile, (asId,)

    elif sel == 7:
        clear()
        return messagesInterface, (asId,)


def customerMainInterface(asId):
#   usersAPI()
    prompt = "Please select an option below:\n"\
            "\t1. View all movies\n"\
            "\t2. View movies available on theater\n"\
            "\t3. Search movies\n"\
            "\t4. View your watched movie list\n"\
            "\t5. View your saved movie list\n"\
            "\t6. My profile\n"\
            "\t7. Log out\n"\
            "Selection: "
    sel = int(
            gatherInput(prompt, "Invalid input. Please try again.\n",
                        menuValidatorBuilder('1234567')))

    if sel == 1:
        clear()
        return jobInterface, (asId,)

    elif sel == 2:
        clear()
        return findFriendsbyType, (asId,)

    elif sel == 3:
        clear()
        return friendsList, (asId,)

    elif sel == 4:
        clear()
        return listSkills, (asId,)

    elif sel == 5:
        clear()
        return inCollegeGroups, (asId,)
        
    elif sel == 6:
        clear()
        return myProfile, (asId,)

    elif sel == 7:
        clear()
        return messagesInterface, (asId,)







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