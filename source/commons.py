import os
from functools import lru_cache

clear = lambda: os.system('cls') 

def enterToContinue():
    input("\nPress ENTER to continue.\n")
    clear()


def enterToGoBack():
    input("\nPress ENTER to go back.\n")
    clear()


def numberValidator(number):
    try:
        float(number)
        return True
    except ValueError:
        return False


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


#####################################
###    For Developer functions    ###
#####################################

@lru_cache
def menuValidatorBuilder(validOptions):
    '''
    Generates a validator from a list of valid options
    :param validOptions: A string or tuple consisting of every valid input from a menu
    :return a function f(x) that returns if x is in validOptions
    '''

    optionsList = list(validOptions)
    return lambda menuInput: (menuInput in optionsList and menuInput != '')


@lru_cache
def rangedMenuValidatorBuilder(start, end):
    '''
    Generates a validator from a range of acceptable integer options
    
    :param start: Begining of acceptable range (inclusive)
    :param end: End of acceptable range (inclusive)
    :returns a function f(x) that returns if x is in the range of start to end (inclusive)
    '''

    optionsRange = range(start, end + 1)
    return lambda menuInput: (int(menuInput) in optionsRange and menuInput != '')


@lru_cache
def binaryOptionValidatorBuilder(firstOption, secondOption):
    '''
    Generates a validator that excepts a case-insensitive version of a binary choise
    :param firstOption: A string that represent one of the two options
    :param secondOption: A string that represent one of the two options
    :return a function f(x) that returns if lower(x) == lower(firstOption) or lower(secondOption)
    '''

    firstOption = firstOption.lower()
    secondOption = secondOption.lower()
    return lambda textInput: (textInput == firstOption or textInput == secondOption)


def optionsOrEnterBuilder(options):
    '''
    Gemerates a validator that excepts any option in the provided area or an empty string (i.e. hitting enter immediately)
    :param options: a list of strings that are valid inputs
    :return a function f(x) that returns if x is in option or is nothing
    '''

    options.append('') 

    return lambda textInput: (textInput.strip() in options)


def gatherInput(prompt, failResponse, validator):
    '''
    Continuously prompts the user for input, validates the input it gets are returns it if its fine or gives an error message if its bad
    :param prompt: A string the user receives when being prompted for input, used in an "input(prompt)" call
    :param failResponse: A message the user receives if they give bad input
    :param validator: A function f(x) = (x is a valid string for a given prompt)
    :return validated user input
    '''
    userInput = input(prompt)
    while True:
        if len(userInput) == 0:
            clear()
            print("Please input a response.\n")
            userInput = input(prompt)
        elif not validator(userInput):
            clear()
            print(failResponse)
            userInput = input(prompt)
        else:
            return userInput
        


