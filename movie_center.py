# import required modules
import media
import fresh_tomatoes

# create toy story movie instance
toy_story = media.Movie(
    "Toy story",
    "toy Story Line",
    "http://www.rotoscopers.com/wp-content/uploads/2013/10/Toy-Story-Poster.jpg",
    "https://www.youtube.com/watch?v=Jh5FVdxOj3Q",
    "November 22, 1995"
    )

# create matrix movie instance
matrix = media.Movie(
    "Matrix",
    "Matrix - Neo vs Morpheus",
    "http://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",
    "https://www.youtube.com/watch?v=12u1nA7bXzc",
    "March 31, 1999"
    )

# create hacker movie instance
hackers = media.Movie(
    "Hackers",
    "Hackers - The Movie",
    "http://images.moviepostershop.com/hackers-movie-poster-1995-1020190474.jpg",
    "https://www.youtube.com/watch?v=Ql1uLyuWra8",
    "September 15, 1995"
    )

# create naruto movie instance
naruto = media.Movie(
    "Naruto",
    "Naruto - Final Battle",
    "http://upload.wikimedia.org/wikipedia/en/c/ca/Naruto_Shippuden_the_Movie_-_The_Will_of_Fire.jpg",
    "https://www.youtube.com/watch?v=gSuqygIVN9Q",
    "March 4, 2010"
    )	

# create cinderella movie instance
cinderella = media.Movie(
    "Cinderella",
    "Cinderella - A Fairy Tale",
    "http://ia.media-imdb.com/images/M/MV5BMjMxODYyODEzN15BMl5BanBnXkFtZTgwMDk4OTU0MzE@._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=20DF6U1HcGQ",
    "March 13, 2015"
    )	

# create home movie instance
home = media.Movie(
    "Home",
    "Home - Worlds Collide",
    "http://ia.media-imdb.com/images/M/MV5BMTg1NTk3MDQ4Ml5BMl5BanBnXkFtZTgwMDMyMzE1MzE@._V1_SX214_AL_.jpg",
    "https://www.youtube.com/watch?v=W6Bd3TWpeig",
    "March 27, 2015"
    )	


# create list of movies
movies = [toy_story, matrix, hackers, naruto, cinderella, home]

# open the movies from a list
fresh_tomatoes.open_movies_page(movies)

