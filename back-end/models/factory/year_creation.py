from Year import Year
from artists_for_description import get_artists_of_year
from generel_tool import add_to_class
from genres_for_description import get_genres_year
from songs_for_description import get_songs_year


def year_information(year: Year, content: dict):
    if content['page'] == 'solo':
        __song_solo_page(year)


def __song_solo_page(year: Year):
    year_ = year.year
    year_dict = {
        'songs': get_songs_year(year_),
        'artists': get_artists_of_year(year_),
        'genres': get_genres_year(year_)
    }
    add_to_class(year, year_dict)
