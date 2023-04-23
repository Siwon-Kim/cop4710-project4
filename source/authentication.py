from source.commons import *
from source.database import *


def passwordValidator(password):
    c, d, s = 0, 0, 0
    length = len(password)
    if length > 7 and length < 13:
        for i in password:
            if i.isupper():
                c += 1
            if i.isdigit():
                d += 1
            if i == '!' or i == '@' or i == '#' or i == '$' or i == '%' or i == '^' or i == '&' or i == '*':
                s += 1

    if c > 0 and d > 0 and s > 0:
        return True
    else:
        return False
