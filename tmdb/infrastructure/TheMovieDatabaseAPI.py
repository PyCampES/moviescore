import os
import requests

from tmdb.domain.Movie import Movie

BASE_URL = "https://api.themoviedb.org/3/"
API_KEY = os.getenv("MOVIEDB_KEY")

class TheMovieDatabaseAPI:

    def __init__(self) -> None:
        pass

    def search_movies(self, query):
        url = f"{BASE_URL}search/movie?api_key={API_KEY}&language=en-US&query={query}&page=1&include_adult=false"
        json_response = requests.get(url).json()
        return Movie().build_from_json(json_response)

    def get_movie(movie_id) -> Movie:
        url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
        json_response = requests.get(url).json()
        return Movie(
            json_response["id"],
            json_response["title"],
            json_response["original_title"],
            json_response["release_date"],
            json_response["overview"],
            json_response["vote_average"],
            json_response["backdrop_path"]
        )
