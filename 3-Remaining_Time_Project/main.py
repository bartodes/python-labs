from datetime import datetime
from time import sleep
from os import system

def timeResults(output, unit):
    print(f"\nTime for '{goal}' left: {output} {str(unit)}.\n")
    sleep(3.5)


def calculateDeadline():
    remaining_time = datetime.strptime(deadline,"%d/%m/%Y") - datetime.today()

    in_days = remaining_time.days
    in_hours = int(remaining_time.total_seconds() / 60 / 60)
    
    if in_days >= 1:
        timeResults(in_days, "day/s")
    elif in_hours >= 1:
        timeResults(in_hours, "hour/s")
    else:
        print("Error: Passed an invalid date.\n Please try again!\n")


def validateInput(data):
    system('clear' or 'cls')
    
    try:
        if len(data.split(":")) == 2:
            user_list = data.split(":")
            
            global goal, deadline
            goal = user_list[0]
            deadline = user_list[1]
            
            calculateDeadline()
    except ValueError:
        print("Stick to the input format\n")


def deadlineInput():
    system("clear" or "cls")
    print("Type 'exit' or CTRL+C to stop the program.\n")

    ctrl = 0

    while ctrl == 0:
        user_data = input("What's your project and it's deadline? project:dd/mm/yyyy\n")

        if user_data != 'exit':
            validateInput(user_data)
        else:
            print ("\nBye Bye")
            ctrl += 1


def main():
    try:
        deadlineInput()
    except KeyboardInterrupt:
        print ("\n\nBye Bye")
main()