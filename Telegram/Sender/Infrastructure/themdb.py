# Python program for fetching TMDB movie data
# after installing our library we'll import or initialize TMDB and Movie object
from tmdbv3api import TMDb
from tmdbv3api import Movie

tmdb = TMDb()
# set you unique API key that you get from TMDB after registartion in my case this is my API key
TMDb.api_key = "6f15568d9aa3d15d0261a5454578c28b"
# you can also export your api key as environment variable using this below export command
# export TMDb_API_KEY='6f15568d9aa3d15d0261a5454578c28b'
# it's optional it's for setting language of Data that we'll fetch from TMDB
tmdb.language = "en"
# for debugging we have set it true
tmdb.debug = True
movie = Movie()
# here I have fetched movie data using movie_id
similar = movie.similar(343611)
# iterate through the data since it have multiple information
for s in similar:
    # print required data like in my case title of movie and it's overview, poster path
    print("Title of the movie: ", s.title)
    print("Overview of the movie:", s.overview)
    print("Poster of the Movie:", s.poster_path)
    # it will give us all movie data which have similar id=343611
# you can also fetch movies using other methods also like popular(), recommendation() etc.

"""
movie.search("tite", page=1)

[{'adult': False, 'backdrop_path': '/w81qHqr1CdbdRco8jpmu6lXMqyk.jpg',
 'genre_ids': [18], 'id': 766798, 'original_language': 'es', 'origi
nal_title': 'Madres paralelas', 'overview': 'Two unmarried women who have become pregnant by accident and are about to give birth meet in
 a hospital room: Janis, middle-aged, unrepentant and happy; Ana, a teenager, remorseful and frightened.', 
 'popularity': 76.856, 
 'poster_
path': '/gDaxYkYNbHuM2VlUazbcpnFZB6d.jpg', 'release_date': '2021-10-08', 'title': 'Parallel Mothers', 'video': False, 'vote_average': 6.9
, 'vote_count': 518}]

"""
