
import random
import math

guess_count = 0
print("Hello!")
play = input("Would you like to play the number guessing game? ")

if (play.lower() == 'y' or play.lower() == "ye" or play_lower == "yes"):
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
    print("Ok... \nI've got my number!")

    # start guessing
    while True:
        try:
            inputs = int(input("Try to guess what it is! "))
            break
        except:
            print("That's not a number...")

    while True:
        # if user gets the answer
        if (inputs == rand_int):
            guess_count += 1

            bound_range = upper_bound - lower_bound
            # result depending on whether user used binary serach method
            if (math.log(bound_range) <= guess_count):
                print("Great! You got it in " + str(guess_count) + " tries!")
            else:
                print("Took you long enough. It took you " + str(guess_count) + " tries")
            quit()
        # if input is bigger than the answer
        elif (int(inputs) > rand_int):
            try:
                inputs = int(input("Nope! Try lower: "))
                guess_count += 1
            except: 
                print("That's not a valid input...")
        # if input is smaller than the answer
        elif (int(inputs) < rand_int):
            try:
                inputs = int(input("Nope! Try higher: "))
                guess_count += 1
            except:
                print("That's not a valid input...")

else:
    print("Okay, see you next time!")
    quit()



