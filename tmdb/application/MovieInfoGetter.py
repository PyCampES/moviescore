from tmdb.domain.Movie import Movie
from tmdb.infrastructure.TheMovieDatabaseAPI import TheMovieDatabaseAPI


class MovieInfoGetter:

    def __init__(self) -> None:
        pass

    def get_movie_by_id(id) -> Movie:
        movie = TheMovieDatabaseAPI.get_movie(id)
        return movie