import random

print("Hello!")
play = input("Would you like to play the number guessing game? ")

if (play.lower() == "yes" or play.lower() == 'y'):
    while True:
        try:
            lower_bound = int(input("Please input the lower bound "))
            break
        except:
            print("That's not a number...")
        
    while True:
        try:
            upper_bound = int(input("Please input the upper bound "))
            if (upper_bound < lower_bound):
                print("That's not a valid input...")
                continue
            break
        except:
            print("That's not a number...")

else:
    quit()



