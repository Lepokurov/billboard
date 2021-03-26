from connection_to_data_base import get_count
from mapper_genre import create_genres_count
from sql_constructor_general import get_count_table
from sql_request_genres import sql_request_count_songs_genre, sql_request_count_artists_genre, sql_constructor_genres, \
    sql_request_genres


def get_count_genres(content) -> int:
    """
    get count of genre by required content
    :param content: dictionary that contain the type and value of searching
    :return: count
    """
    count = 0
    if content['type'] == 'by_song' or content['type'] == 'by_artist':
        count = __get_count_all_genre()
    elif content['type'] == 'search':
        count = __get_count_genre_search(content['value'])
    return count


def __get_count_all_genre() -> int:
    """
    get count of all genre
    :return: count of genres
    """
    count = get_count(get_count_table('genre'))
    return count


def __get_count_genre_search(search) -> int:
    """
    get count of genres by search data
    :param search: search year data
    :return: count
    """
    sql_request = sql_request_genres('by_song', search, True)
    count = get_count(sql_request)
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
