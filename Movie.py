'''
Main movieinfo class constructs default parameters for each movie object
'''

import webbrowser

class MovieInformation():

    def __init__(self, movie_name, movie_description, movie_picture, movie_video):
        self.title = movie_name
        self.desc = movie_description
        self.poster_image_url = movie_picture
        self.trailer_youtube_url = movie_video

    def play_trailer(self):
        webbrowser.open(self.url)

