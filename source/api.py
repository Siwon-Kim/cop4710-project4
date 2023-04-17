from os.path import exists
import os.path

from commons import *
from database import checkExistingUsername, initAcct
from authentication import passwordValidator

def employeeListAPI():
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

                username = e[0]
                password = e[1]
                firstname = e[2]
                lastname = e[3]
                email = e[4]

                if checkExistingUsername(username) and passwordValidator(password):
                    initAcct(username, password, firstname, lastname, email, 1)