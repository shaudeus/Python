
class Animal(object):  # Parent class
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} is eating {}.".format(self.name, food))


class Dog(Animal):  # Child class from Animal Parent Class
    def fetch(self, thing):
        print("{} runs after the {}. ".format(self.name, thing))


class Cat(Animal):  # Child class from Animal Parent Class
    def swatstring(self):
        print("{} shreds the string!".format(self.name))


r = Dog("Rover")  # Create Dog object
f = Cat("Fluffy")  # Create Cat object

r.fetch("paper")  # name is available to both classes while fetch is only available to Dog
f.swatstring()  # name is available to both classes but swatstring is only available to Cat
r.eat("Bone")  # .eat is an attribute of the Parent available to all child classes
f.eat("catnip")  # .eat is an attribute of the Parent available to all child classes
r.swatstring()  # Error Inheritance not set between these classes
