from tmdbv3api import TMDb
from tmdbv3api import Movie


def find_similar(movie_title):
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    search = movie.search(movie_title)
    similar = movie.similar(search[0].id)
    
    return similar
