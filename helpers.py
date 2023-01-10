from tmdbv3api import TMDb
from tmdbv3api import Movie
import requests, json, os


def find_similar(movie_title):
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True
    movie = Movie()
    search = movie.search(movie_title)

    return search

def get_trending():
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    popular = movie.popular()

    return popular

def get_upcoming():
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    upcoming = movie.upcoming()

    return upcoming
    
def get_toprated():
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    toprated = movie.top_rated()

    return toprated

def get_nowplaying():
    tmdb = TMDb()
    tmdb.api_key = "fb30a4fbe49546ed501bce99179c0fdd"
    tmdb.language = 'en'
    tmdb.debug = True

    movie = Movie()
    nowplaying = movie.now_playing()

    return nowplaying

def get_data(Movie_ID):
    API_key = "fb30a4fbe49546ed501bce99179c0fdd"
    query = 'https://api.themoviedb.org/3/movie/'+str(Movie_ID)+'?api_key='+API_key+'&language=en-US'
    response =  requests.get(query)
    if response.status_code==200: 
    #status code ==200 indicates the API query was successful
        array = response.json()
        return (array)
    else:
        return ("error")