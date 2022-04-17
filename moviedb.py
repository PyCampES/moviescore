import requests

BASE_URL = "https://api.themoviedb.org/3/"

API_KEY = os.getenv("MOVIEDB_KEY")


def search_movies(query):
    url = f"{BASE_URL}search/movie?api_key={API_KEY}&language=en-US&query={query}&page=1&include_adult=false"
    response = requests.get(url)
    return response.json()


def get_movie(movie_id):
    url = f"{BASE_URL}/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    return response.json()


def format_movie(movie):
    genres = [genre["name"] for genre in movie["genres"]]
    release_year = movie["release_date"][:4]
    return f"""\
*{movie["original_title"]} \({release_year} \)*
_{", ".join(genres)} \- {movie["runtime"]} \- {movie["vote_average"]}/10_
{movie["overview"]}"""


def format_movie_by_id(movie_id):
    movie = get_movie(movie_id)
    return format_movie(movie)
