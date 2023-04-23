from source.states import stateLoop, applicationEntry
from source.api import *

if (__name__ == "__main__"):
    # employeeListAPI()
    # movieListAPI()

    stateLoop(applicationEntry)
