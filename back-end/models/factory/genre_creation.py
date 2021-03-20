from Genre import Genre
from artists_for_description import get_artists_genre
from generel_tool import add_to_class
from genres_count import get_count_current_genre
from genres_for_description import get_genre
from genres_list import get_genres_all
from songs_for_description import get_songs_genre
from years_for_description import get_years_genre


def genre_information(genre: Genre, content: dict):
    if content['page'] == 'solo':
        __genre_solo_page(genre)
    if content['page'] == 'list':
        __genre_list_page(genre, content)


def __genre_solo_page(genre: Genre):
    id_genre = genre.id
    genre_ = get_genre(id_genre)
    genre_['songs'] = get_songs_genre(id_genre)
    genre_['artists'] = get_artists_genre(id_genre)
    genre_['years'] = get_years_genre(id_genre)
    genre_['count'] = get_count_current_genre(id_genre)
    add_to_class(genre, genre_)


def __genre_list_page(genre: Genre, content: dict):
    start = genre.id
    step = genre.step

    if content['type'] == 'all':
        genres = get_genres_all(content, start, step)
    else:
        genres = get_genres_all(content, start, step)

    genre.list = genres
    del genre.step
    del genre.id
