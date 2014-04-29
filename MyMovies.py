'''
Ryan Schachte
Favorite Movies
Add list of favorite movies and play trailer of desired movie.
Tests OOP skills and foundations
'''
import Movie

#Test Movie
#pulp = Movie.MovieInformation("name", "desc", "http://www.google.com")

#List to contain all movies added
movies = []


#Displays Current Added Movies
def print_movies():
    for each_movie in movies:
        pretty_format = '''
        Name: %s
        Description: %s
        Link: %s
        ''' %(each_movie.name, each_movie.desc, each_movie.url)
        print pretty_format

#Adds movie to list based off 3 req. arguments
def add_movie():
    print 'Enter Movie Name'
    movie_name = raw_input(">>")

    print 'Enter Movie Description'
    movie_description = raw_input(">>")

    print 'Enter Movie URL'
    movie_link = raw_input(">>")

    movie_name = Movie.MovieInformation(movie_name, movie_description, movie_link)
    movies.append(movie_name)

#Plays movie trailer of specified movie
def play_trailer(movie_name):
    for each_movie in movies:
        #print each_movie.name
        if movie_name == each_movie.name:
            each_movie.play_trailer()
            break

answer = raw_input("Add Movie? y/n")

#Adds movie until otherwise specified
while (answer == "y"):
    add_movie()
    answer = raw_input("Continue? y/n")

#Displays Movies
print_movies()

#Play trailer of choice
print 'Play Movie Trailer'
movie = raw_input(">>")
play_trailer(movie)
