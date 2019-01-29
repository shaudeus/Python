# Movie tracking app
# Programmer: Rashaun Forrest
# Date: 06/20/2016
# Purpose This file creates a class for movies with the name of the movie,
# genre and if the user watched it or not.

# Create new class for movies


class Movie:
    # Set class attributes for movie name, genre, and if it has been watched
    def __init__(self, name, genre, watched):
        self.name = name
        self.genre = genre
        self.watched = watched
    # Use represent to format the data into a human readable string for debug

    def __repr__(self):
        return "<Movie {}>".format(self.name)
    # Create Json dictionary for attributes(keys) for name, genre, and watched

    def json(self):
        return {
            'name': self.name,
            'genre': self.genre,
            'watched': self.watched
        }
    #

    @classmethod
    def from_json(cls, json_data):
        # Use argument unpacking to get Json data from attributes in Movie
        return Movie(**json_data)
