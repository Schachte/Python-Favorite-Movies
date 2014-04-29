'''
Ryan Schachte
Favorite Movies
Add list of favorite movies and play trailer of desired movie.
Tests OOP skills and foundations
'''
import Movie
import fresh_tomatoes

#Some Test Movies
avatar = Movie.MovieInformation("Avatar", "Avatar Description", "http://www.arts-wallpapers.com/movie_posters/movie-posters-november-2009/images/Movie%20Posters%20November%202009_03.jpg", "http://www.youtube.com/watch?v=d1_JBMrrYw8")
hours = Movie.MovieInformation("127 Hours", "127 Hours Description", "http://gdj.gdj.netdna-cdn.com/wp-content/uploads/2011/03/127-hours-movie-poster.jpg", "http://www.youtube.com/watch?v=OlhLOWTnVoQ")
virgin = Movie.MovieInformation("40 Yearold Virgin", "Virgin Description", "http://blog.calindaniel.com/wp-content/uploads/2010/07/40-year-old-virgin-poster1.jpg", "http://www.youtube.com/watch?v=Vn3IRHhPXMo")

#List to contain all movies added
movies = [avatar, hours, virgin]

fresh_tomatoes.open_movies_page(movies)