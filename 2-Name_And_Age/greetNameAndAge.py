def sayHello(arg1, arg2):
    return print (f"\nHello {arg1}, are you {arg2} years old?")


def checkInt(name, age):
    if len(name) > 0 and age.isdigit():
        age=int(age)
        sayHello(name, age)
    elif len(name) < 1:
        print("\nTry with a valid name!\n")
    else:
        print("\nTry with a valid number!\n")


def askForInput():
    try:
        print("To exit: type 'exit'\n")
        cntrl = 0
        while cntrl == 0:
            name_input = input("What's your name?: ")
            if name_input != "exit":
                age_input = input("And your age?: ")
                if age_input != "exit":
                    for i,k in zip(name_input.split(", "), age_input.split(", ")):
                        checkInt(i,k)
                else:
                    cntrl=+1
            else:
                cntrl=+1
        print("\nBye bye!")
    except KeyboardInterrupt:
        print("")
        print("\nBye bye!")


def main():
    askForInput()
main()