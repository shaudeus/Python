# Lucky Numbers Lottery Application

# Programmer: Rashaun Forrest
# Email: Rashaun.forrest@gmail.com
# Written 06/15/2016

# Purpose: Create an app where user can pick 6 numbers (between 1 and 25) and
# the program compares user numbers with randomly generated numbers and calculates
# the winnings based on correct numbers guessed.

# Import random module to generate random numbers
import random


# Main program method decribed below in steps:
def main():
    # Step 1: Ask player for thier lucky number_split
    user_numbers = input_user_numbers()

    # Step 2 generate random lottery numbers
    lottery_numbers = create_random_numbers()

    # Step 3 Determine winnings based on intersection
    # Create set of numbers that overlap
    matched_numbers = user_numbers.intersection(lottery_numbers)
    # Create a score based on how many elements in matched_numbers
    print("You matched numbers {}"" You have won ${}!!!".format(
        matched_numbers, 100 ** len(matched_numbers)))


# When this method is called program will recieve a integer set
def input_user_numbers():

    # Create user input of 6 numberssaved in varaiable player_numbers
    player_numbers = input("Enter your 6 lucky numbers between 1-25. Please seperate by comma: ")

    # Create a list from player_numbers variable
    number_split = player_numbers.split(",")

    # Create integer set from the list, the set will eliminate duplicate numbers
    # This uses set comprehension to iterate the strings into integers.
    # It can be read as: for each number in the list number_split, iterate each
    # element as an integer.
    integer_set = {int(number) for number in number_split}
    return integer_set

# Create a method to return a set of 6 random numbers.


def create_random_numbers():
    set_holder = set()  # reate an empty set saved in variable set_holder

    while len(set_holder) < 6:  # Run loop until you get 6 elements in set_holder
        # Add 6 random numbers into set_holder variable.
        set_holder.add(random.randint(1, 25))  # Adds random numbers between 1-25
    return set_holder


# Call main method to run program
main()
