
class Movie():

    def __init__(self,
        id,
        title,
        original_title,
        release_date,
        overview,
        vote_average,
        backdrop_path
    ) -> None:
        self.id = id
        self.title = title
        self.original_title = original_title
        self.release_date = release_date
        self.release_year = self.get_release_year()
        self.overview = overview
        self.vote_average = vote_average
        self.vote_percentage = self.get_vote_percentage()
        self.backdrop_path = backdrop_path
        self.backdrop_url = self.get_backdrop_url()
    
    def get_release_year(self):
        if (None != self.release_date):
            return self.release_date[:4]
        return None
    
    def get_vote_percentage(self):
        if (None != self.vote_average):
            return int(float(self.vote_average)*10)
        return None
    
    def get_backdrop_url(self):
        if (None != self.backdrop_path):
            return f'https://image.tmdb.org/t/p/original{self.backdrop_path}'
        return None
