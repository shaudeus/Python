# Student mark keeping application

# Programmer: Rashaun Forrest
# Date written: 06/19/2016
# Email: Rashaun.forrest@gmail.com

# Purpose: Create an app that allows user to input student names and marks
# then have the program give you an average mark based on the marks it has
# stored


# Create a student list to begin with
student_list = []

# Create a method to add a student name to the list


def create_student():
    name = input("Please enter the new student's name: ")
    student_data = {
        'name': name,
        'marks': []
    }

    return student_data

# Create a method to add a grade to the list


def add_mark(student, mark):
    student['marks'].append(mark)

# Create a method to calucate a average grade


def calculate_average_mark(student):
    number = len(student['marks'])
    if number == 0:
        return 0

    total = sum(student['marks'])
    return total / number

# Create a method to print student name and avg grade


def print_student_details(student):
    print("{}, average mark: {}.".format(student['name'],
                                         calculate_average_mark(student)))

# Create a method to print out all student details


def print_student_list(students):
    # User index number for student ID
    for i, student in enumerate(students):
        print("ID: {}".format(i))
        print_student_details(student)

# Create a method that allows the user to interact and call the above methods


def menu():
    # Ask user what they want to do and save this into a variable
    selection = input("Enter 'p' to print the student list, "
                      "'s' to add a new student, "
                      "'a' to add a mark to a student, "
                      "or 'q' to quit. "
                      "Enter your selection: ")
    # Runs code as long as variable is NOT q
    while selection != 'q':
        # Prints list if selection variable is p
        if selection == 'p':
            print_student_list(student_list)
        # add student if variable is s
        elif selection == 's':
            student_list.append(create_student())
        # add a mark to the student
        elif selection == 'a':
            student_id = int(input("Enter the student ID to add a mark to: "))
            student = student_list[student_id]
            new_mark = int(input("Enter the new mark to be added: "))
            add_mark(student, new_mark)
        # Continue the process until you get q as the variable
        selection = input("Enter 'p' to print the student list, "
                          "'s' to add a new student, "
                          "'a' to add a mark to a student, "
                          "or 'q' to quit. "
                          "Enter your selection: ")


# Run the main method by starting with the menu
menu()
