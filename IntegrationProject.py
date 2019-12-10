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

    if userName in("No", "no"):
        easterEgg = input("Well, do you want to know my name?")
        if easterEgg in("No", "no"):
            print("Fine!")
            quizStart()
        elif easterEgg in("Yes", "yes"):
            print("I do not have a name :(")
            quizStart()
        else:
            print("Invalid response!")
            quizStart()
    else:
        print("Your name is", userName + ", congrats you know your own name, and now so do I!")


def questions():

    favNum = input("What is your favorite number? : ")
    favNum2 = input("What is your second favorite number? : ")
    try:
        val = int(favNum)
    except ValueError:
        print("Error, 1st input is not a number!")
        firstFav = False
        questions()
    else:
        firstFav = True
    try:
        val = int(favNum2)
    except ValueError:
        print("Error, 2nd input is not an number!")
        secondFav = False
        questions()
    else:
        secondFav = True

    if(firstFav == True and secondFav == True):
        intFav = int(favNum)
        intFav2 = int(favNum2)
        addFav = intFav + intFav2
        print("Add them together and that is:", addFav)
    else:
        questions()




















# Calling the game functions here.
quizStart()
questions()
