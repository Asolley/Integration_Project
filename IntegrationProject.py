# Andrew Solley
# Integration Project Quiz game.


# Start of the game function.
def quizStart():

    print("This is a quiz game about you, tell me all the things!")
    global userName
    userName = input("Welcome! What is your name? : ")
    easterEggFn()


# ummmm no?
def easterEggFn():

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


# This function asks the user for their favorite number and adds them together.
def favNumFn():

    # Asks for user to enter an integer
    favNum = input("What is your favorite number? : ")
    favNum2 = input("What is your second favorite number? : ")

    # Check if 1st input is int
    try:
        val = int(favNum)
    except ValueError:
        print("Error, 1st input is not a number!")
        firstFav = False
    else:
        firstFav = True

    # Check if 2nd input is int
    try:
        val = int(favNum2)
    except ValueError:
        print("Error, 2nd input is not an number!")
        secondFav = False
    else:
        secondFav = True

    # Only works if both are true
    if firstFav == True and secondFav == True:
        intFav = int(favNum)
        intFav2 = int(favNum2)
        addFav = intFav + intFav2
        print("Add them together and that is:", addFav)
        print("Wow, that's my favorite number,", userName, "that's crazy!")
    else:
        # Restarts if bot were not ints
        favNumFn()


# This function determines which number is smaller
def getSmaller(num1, num2):

    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    return smaller


# This function asks for user input to get the smaller number
def getNums():

    # User input for integer.
    print("I can find which number is smaller!")
    userNum1 = input("Enter a number: ")
    userNum2 = input("Enter a second number: ")

    # Check if 1st input is int
    try:
        val = int(userNum1)
    except ValueError:
        print("Error, 1st input is not an number!")
        num1 = False
    else:
        num1 = True
    # Check if 2nd input is int
    try:
        val = int(userNum2)
    except ValueError:
        print("Error, 2nd input is not an number!")
        num2 = False
    else:
        num2 = True

    # Only works if both are true
    if num1 == True and num2 == True:
        smallerNumber = getSmaller(userNum1, userNum2)
        print("The smaller of the two number is", smallerNumber)
    else:
        # Restarts if bot were not ints
        getNums()


















# Calling the game functions here.
quizStart()
favNumFn()
getNums()
