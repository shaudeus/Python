# Polymorphism: OOP coursework
# Programmer: Rashaun Forrest
# Date: 06/03/2016

# Purpose: To explore the principle of Polymorphism in OOP


class Animal(object):  # Parent class
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} is eating {}.".format(self.name, food))


class Dog(Animal):  # Child class from Animal Parent Class
    def fetch(self, thing):
        print("{} runs after the {}. ".format(self.name, thing))

    def show_affection(self):  # Duplicate interface called to produce differnt results
        print("{} wags tail.".format(self.name))


class Cat(Animal):  # Child class from Animal Parent Class
    def swatstring(self):
        print("{} shreds the string!".format(self.name))

    def show_affection(self):  # Duplicate interface called to produce differnt results
        print("{} purrs.".format(self.name))


# Called show_affection which produced different results for each class
for a in (Dog("Rubble"), Cat("Fluffy"), Cat("Skittles"), Dog("Chase")):
    a.show_affection()
