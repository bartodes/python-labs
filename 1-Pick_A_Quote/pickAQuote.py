from os import system
from time import sleep


def waveToUser():
    try:
        count = 0
        while count == 0:
            print("--> Input Options\n\n'suits: 1, 2, or 3' \n'naruto: 1, 2 or 3' \n'random: 1, 2 or 3' \nor just type 'exit'.\n")
            print("--> Input Example: 'random:1' \n#it will print the first random quote for you.")
            message_value = input("\nHello! Do you watn to hear one quote?: ")
            if message_value != "exit":
                validateInput(message_value)
            else:
                count += 1
                print ("\nBye bye")
    except KeyboardInterrupt:
        print("\n\nBye bye")


def validateInput(arg):
    if len(arg.split(":")) == 2:
        system('clear' or 'cls')
        mssg=arg.split(":")
        mssg={"src":mssg[0],"quote":mssg[1]}
        findQuote(mssg)
    else:
        system('clear' or 'cls')
        print("READ THE OPTIONS AND TRY AGAIN\n")


def findQuote(source):
    if source["src"] == "suits":
        quotesSuits(source["quote"])
    elif source["src"] =="naruto":
        quotesNaruto(source["quote"])
    elif source["src"] =="random":
        quotesRandom(source["quote"])
    else:
        print("READ THE OPTIONS AND TRY AGAIN\n")  


def printQuotes(quotes, position):
    system('clear' or 'cls')
    for char in quotes[position]:
        sleep(0.05)
        print (char, end= "", flush=True)
    sleep(3)
    system('clear' or 'cls')

def quotesSuits(value):
    
    try:
        value=int(value)
        quotes = {
            1: "\nTrue power isn't prettending to be what yoy are not, it's admiting the truth of who you are.",
            2: "\nWork until you no longer have to introduce yourself.",
            3: "\nDon't raise your voice, improve your argument."
        }
        printQuotes(quotes, value)
    except ValueError:
        print("Enter a valid number: 1, 2 or 3\n")   


def quotesNaruto(value):
    try:
        value=int(value)
        quotes = {
            1: "\nThe most important rules are the ones that we impose on ourselves.",
            2: "\nGrowth occurs when one goes beyond ones limits.",
            3: "\nNo matter who you are, you don't know what kind of human you are until the very end."
        }
        printQuotes(quotes, value)
    except ValueError:
        print("Enter a valid number: 1, 2 or 3\n")


def quotesRandom(value):
    try:
        value=int(value)
        quotes = {
            1: "\nThe things you own end up owing you. \n~ Fight Club",
            2: "\nHe who has a why to live for can bear almost any how. \n~ Friedrich Nietzsche",
            3: "\nUntil you make the unconscious conscious, it will direct your life and you will call it fate. \n~ Carl Jung"
        }
        printQuotes(quotes, value)
    except ValueError:
        print("Enter a valid number: 1, 2 or 3\n")


def main():
    waveToUser()
main()