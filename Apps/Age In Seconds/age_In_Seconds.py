# Simple practice program designed  to take user input of age in years and
# display that age in seconds##
# This variable allows user to input a number for thier age
age_Input = input("Enter your age in number of years old: ")
# Using the format command to include math and variables into a string
print("You have lived for {} seconds. Which is {} years.".format(
    int(age_Input) * 365 * 24 * 60 * 60, age_Input))
