# Instance counter app
# Programmer: Rashaun Forrest
# Date 06/01/2016

# Purpose: To understand data in classes and where to use class data vs
# where to use instance data.


class InstanceCounter(object):  # All classes written in CamelCase
    count = 0   # Set class data

    def __init__(self, val):  # Initialize construct, Pass val
        self.val = val  # Set instance attribute
        InstanceCounter.count += 1   # Get count data from Class usint dot notation and add 1

    # Setter Instance
    def set_val(self, newval):  # Pass newval
        self.val = newval  # Setter instance set as instance variable newval

    # Getter Instance
    def get_val(self):
        return self.val  # Get instance data val

    # Run count method to increase count by 1
    def get_count(self):
        return InstanceCounter.count

    # End of class notated by change of indentation


# Set Global variables using Class
a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print("val of obj: {}".format(obj.get_val()))  # Get intialized value
    print("count: {}".format(obj.get_count()))  # Count should be 3 instances
