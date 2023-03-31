from datetime import datetime
from os import system

def resultsForUser():
    print("output")


def calculateDeadline():
    print("deadline")



def validateInput(data):
    system('clear' or 'cls')
    if len(data.split(":")) == 2:
        user_list = data.split(":")
        global goal, deadline
        goal = user_list[0]
        deadline = user_list[1]
        calculateDeadline()
    else:
        print("Stick to the input format")


def deadlineInput():
    try:
        ctrl = 0
        print("Type exit or CTRL+C to stop the program.")
        while ctrl == 0:
            user_data = input("What's your project and it's deadline? (project:dd/mm/yy)\n")
            if user_data != 'exit':
                validateInput(user_data)
            else:
                print ("\nBye Bye")
                ctrl += 1
    except KeyboardInterrupt:
        print ("\n\nBye Bye")


def main():
    deadlineInput()
main()