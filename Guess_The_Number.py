import random

print("Hello!")
play = input("Would you like to play the number guessing game? ")

if (play.lower() == "yes" or play.lower() == 'y'):

    # get lower bound
    while True:
        try:
            lower_bound = int(input("Please input the lower bound "))
            break
        except:
            print("That's not a number...")

    # get upper bound
    while True:
        try:
            upper_bound = int(input("Please input the upper bound "))
            if (upper_bound < lower_bound):
                print("That's not a valid input...")
            else:
                break
        except:
            print("That's not a number...")

    rand_int = random.randint(lower_bound, upper_bound + 1)
    print("Ok... \n I've got my number!")

    # start guessing
    while True:
        try:
            inputs = int(input("Try to guess what it is! "))
            break
        except:
            print("That's not a number...")

    while True:
        if (inputs == rand_int):
            print("You got it :)")
            quit()
        elif (int(inputs) > rand_int):
            try:
                inputs = int(input("Nope! Try lower: "))
            except: 
                print("That's not a valid input...")

        elif (int(inputs) < rand_int):
            try:
                inputs = int(input("Nope! Try higher: "))
            except:
                print("That's not a valid input...")

else:
    quit()



