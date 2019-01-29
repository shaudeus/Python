# Movie tracking app
# Programmer: Rashaun Forrest
# Date: 06/20/2016
# Purpose This file creates a class for users with the name of the user,
# and any movies they have, sets default watched to false or not watched

# Import Movie class from included files
from movie_class import Movie

# Create a class for all users with attributes name and movies they have


class User:
    def __init__(self, name):
        self.name = name
        self.movies = []
    # Use represent to format the data into a human readable string

    def __repr__(self):
        return "<User {}>".format(self.name)
    # Add a movie name and genre and set watched default to False

    def add_movie(self, name, genre):
        movie = Movie(name, genre, False)
        self.movies.append(movie)
    # Delete a movie using filter to remove the name of the movie from the list

    def delete_movie(self, name):
        self.movies = list(filter(lambda movie: movie.name != name, self.movies))
    # Return a list of movies that have been watched using filter

    def watched_movies(self):
        return list(filter(lambda movie: movie.watched, self.movies))
    # Change watched status of a movie to True

    def set_watched(self, name):
        for movie in self.movies:
            if movie.name == name:
                movie.watched = True
    # Return Json dictionary to create a list of movies from this dictionary

    def json(self):
        return {
            'name': self.name,
            'movies': [
                # Create a list for each of the movies in movie
                movie.json() for movie in self.movies
            ]
        }
    # get Json data

    @classmethod
    def from_json(cls, json_data):
        # Access user name
        user = User(json_data['name'])
        movies = []
        # Get movie data from Json dictionary
        for movie_data in json_data['movies']:
            movies.append(Movie.from_json(movie_data))
        user.movies = movies

        return user
