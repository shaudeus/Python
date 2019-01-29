# Simple program that asks the user to guess a random number

import random  # Imports the ability to generate random numbers

# Create a list with two random numbers—each random number is created by random.randint(0, 9)
magic_numbers = [random.randint(0, 9), random.randint(0, 9)]


def ask_user_and_check_number():
    # Ask the user for a random number, and convert it to an actual number using int()
    user_number = int(input("Enter a number between 0 and 9: "))
    if user_number in magic_numbers:  # If the user's number is one of the random numbers generated above...
        return "You got the number right!"
    if user_number not in magic_numbers:
        return "You didn't quite get it."


def run_program_x_times(chances):
    for attempt in range(chances):  # range(chances) is [0, 1, 2], so we're repeating this 3 times
        print("This is attempt {}".format(attempt))  # Print out that this is attempt x (0, 1, or 2)
        message = ask_user_and_check_number()  # Run the function above, and print the output
        print(message)


# Ask the user how many times to run the program
user_attempts = int(input("How many guessing attempts would you like: "))

run_program_x_times(user_attempts)
