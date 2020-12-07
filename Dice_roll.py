#importing modules for generating random numbers
import random
import time

value_min = 1
value_max = 6

roll_again = 'yes'

while roll_again == 'yes' or roll_again == 'y':
    print("\nRolling the dice...\n")
    print("The value is:")

    time.sleep(2)   #wait for 2 seconds after rolling the dice
    print(random.randint(value_min, value_max)) #print a random number between 1 to 6

    print("\nTo roll the dice again enter 'y' or 'quit' to exit\n")
    roll_again = input("Roll the dice again?...")   
