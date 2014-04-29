'''
Main movieinfo class constructs default parameters for each movie object
'''

import webbrowser

class MovieInformation():

    def __init__(self, movie_name, movie_description, movie_video):
        self.name = movie_name
        self.desc = movie_description
        self.url = "http://www." + movie_video + ".com"

    def play_trailer(self):
        webbrowser.open(self.url)

