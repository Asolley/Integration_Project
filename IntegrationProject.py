
# Andrew Solley
# Integration Project Quiz game.

# Start of the game function.
def quizStart():
    print("This is a quiz game about you, tell me all the things!")
    global userName
    userName = input("Welcome! What is your name? : ")
    easterEgg()

# Random easter egg function, looked messy to have it in the quizStart function :)
def easterEgg():
    if userName == ("No"):
        easterEgg = input("Well, do you want to know my name?")
    elif userName == ("no"):
        easterEgg = input("Well, do you want to know my name?")
        if easterEgg == ("No"):
            print("Fine!")
        elif easterEgg == ("no"):
            print("Fine!")
        elif easterEgg == ("Yes"):
            print("I do not have a name :(")
        elif easterEgg == ("yes"):
            print("I do not have a name :(")
        else:
            print("Invalid response!")
    else:
        print("Your name is", userName + ", congrats you know your own name, and now so do I!")

def questions():
    print("random")


















# Calling the game functions here.
quizStart()
