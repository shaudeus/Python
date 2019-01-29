# Movie tracking app
# Programmer: Rashaun Forrest
# Date: 06/20/2016
# Purpose This file creates a menu to interact with the program and modules

# Import Json
import json
import os
# import class from included files
from user_class import User

# Create a menu system to access methods from a list of option


def menu():
    # Ask for users name
    name = input("Enter your name: ")
    filename = "{}.txt".format(name)
    # Check if name exist
    if file_exists(filename):
        # open file in read mode
        with open(filename, 'r') as f:
            # Load Json data from file
            json_data = json.load(f)
        # Open user data from Json file
        user = User.from_json(json_data)
    # If name does not exist in file then create new user
    else:
        user = User(name)
    # Create a list of options to access methods w
    user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                       "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                       ", 'f' to save or 'q' to quit")
    while user_input != 'q':
        if user_input == 'a':
            movie_name = input("Enter the movie name: ")
            movie_genre = input("Enter the movie genre: ")
            user.add_movie(movie_name, movie_genre)
        elif user_input == 's':
            for movie in user.movies:
                print("Name: {} Genre: {} Watched: {}".format(
                    movie.name, movie.genre, movie.watched))
        elif user_input == 'w':
            movie_name = input("Enter the movie name to set as watched: ")
            user.set_watched(movie_name)
        elif user_input == 'd':
            movie_name = input("Enter the movie name to delete: ")
            user.delete_movie(movie_name)
        elif user_input == 'l':
            for movie in user.watched_movies():
                print("Name: {} Genre: {} Watched: {}".format(
                    movie.name, movie.genre, movie.watched))
        elif user_input == 'f':
            # Open file in write mode as variable f
            with open(filename, 'w') as f:
                # Save or dump users Json dictionary in this file
                json.dump(user.json(), f)

        # Reload menu after a selection
        user_input = input("Enter 'a' to add a movie, 's' to see the list of movies,"
                           "'w' to set a movie as watched, 'd' to delete a movie, 'l' to see the list of watched movies,"
                           ", 'f' to save or 'q' to quit")


def file_exists(filename):
    return os.path.isfile(filename)


menu()
