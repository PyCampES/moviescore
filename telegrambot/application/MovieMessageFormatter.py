class MovieMessageFormatter:

    def __init__(self, movie) -> None:
        self.movie = movie

    def format(self) -> str:
        return (
            f'<b>{self.movie.title} ({self.movie.release_year})</b>'
            f'\n\n'
            f'<i>{self.movie.overview}</i>'
            f'\n'
            f'⭐️ {self.movie.vote_percentage}%'
            f'\n'
            f'🌐 <a href="https://www.themoviedb.org/movie/{self.movie.id}">TheMovieDatabase</a>'
        )
