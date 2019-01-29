# Inheritance Example in OOP
# Programmer: Rashaun Forrest
# Date: 06/02/2016

# Purpose: Show how classes can inherit data from other classes
# Create a Parent Class called Date


class Date(object):  # Inherit from object class built into python
    def get_date(self):
        return "2016-06-02"

# Create a child class of Date called Time


class Time(Date):  # Inherit from Date class
    def get_time(self):
        return "06:30:06"


dt = Date()  # Date obkect created from Date class
print(dt.get_date())

tm = Time()  # Time object created from Time class
print(tm.get_time())  # Initiate attribute lookup from instance
print(tm.get_date())  # got this method from inherited class Date from Time object
