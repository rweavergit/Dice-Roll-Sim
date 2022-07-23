import random

# Range of values for dice
min_val = 1
max_val = 6
#loop rolling from user
roll_again = "yes"
#loop
while roll_again == "yes" or roll_again == "y":
    print("Rolling the Dice")
    print("The Values are :")

    # Generating and printing 1st random interger from 1-6
    print(random.randint(min_val, max_val))

    # Asking user to roll again
    roll_again = input("Roll the Dice Again?")