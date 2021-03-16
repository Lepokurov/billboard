from connection_to_data_base import get_count
from models import create_genres_count
from sql_constructor_general import get_count_table
from sql_request_genres import sql_request_count_songs_genre, sql_request_count_artists_genre


def get_count_all_genre() -> int:
    """
    all count of genres
    :return: count of genres
    """
    count = get_count(get_count_table('genre'))
    return count


def get_count_current_genre(id_genre) -> dict:
    """
    Getting count of songs and artist with this genre
    :param id_genre: current genre
    :return: dictionary with the song and artist items that contain count
    """

    song_count = get_count(sql_request_count_songs_genre(id_genre))
    artist_count = get_count(sql_request_count_artists_genre(id_genre))

    genres_count = create_genres_count(song_count, artist_count)
    return genres_count
