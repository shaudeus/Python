# OOP Assignment
# Programmer: Rashaun Forrest
# Purpose: Using inherited classes create a class that has to write to a file
# then using a child class create a method to write a log entry that is Date/Time
# stamped

# Import datetime module to get the date and time
from datetime import datetime
import abc


class WriteFile(object):
    # Create a class to handle the ability to write to a file
    __meta__ = abc.ABCMeta  # Makes WriteFile a metafile

    @abc.abstractmethod
    # Sets code below as an abstractmethod and requires WriteFile
    def __init__(self, filename):  # Initialize object and pass the filename
        self.filename = filename  # Get filename and set it to instance vairable filename

    def write_info(self, text_input):
        # Method to write text information(text_input) into a file
        # Args: text_input (string): Text information for the log entry
        fh = open(self.filename, "a")  # Open a file with filename
        fh.write(text_input + "\n")  # Write the passed in text into the file
        fh.close()  # Close file


class LogFile(WriteFile):
    # This method writes a date and time stamped file to a log
    def write(self, new_line):
        dt_stamp = datetime.now()  # Get current date and time saved into dt_stamp
        dt_string = dt_stamp.strftime("%Y-%m-%d %H:%M")
        self.write_info("{0}    {1}".format(dt_string, new_line))
        # Run inherited method(write_info) to write a new line and pass information in
        # dt_string and info passed in from new_line


# Create a new log file
log = LogFile(input("Please name your log file with no spaces: "))
# Write a new line to the log file
log.write(input("Enter your log message: "))
