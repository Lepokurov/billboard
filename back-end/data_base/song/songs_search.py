from models import create_ids
from songs_list import get_songs_list
from sql_constructor_general import limit_information
from connection_to_data_base import get_data_from_db
import sql_request_songs


def search_songs(content: dict, start: int, step: int) -> list:
    """
    Get songs by the required parameters
    :param content: dictionary that contain the type and value
    :param start: the start row
    :param step: number of rows
    :return: list of songs by the required parameters
    """
    id_songs = _get_ids_songs_by_search(content, start, step)
    songs = get_songs_list(id_songs, content['order'])
    return songs


def _get_ids_songs_by_search(content: dict, start: int, step: int) -> list:
    """
    Searching songs ids by the required parameters
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list required ids of songs
    """
    ids = []
    if content['type'] == 'by_title':
        ids = __get_songs_ids_by_title(content, start, step)
    elif content['type'] == 'by_genre':
        ids = __get_songs_ids_by_genre(content, start, step)
    elif content['type'] == 'by_year':
        ids = __get_songs_ids_by_year(content, start, step)
    elif content['type'] == 'by_artist':
        ids = __get_songs_ids_by_artist(content, start, step)
    elif content['type'] == 'hit_several_times':
        ids = __get_songs_ids_hit_several_times(content, start, step)

    return ids


def __get_songs_ids_by_title(content, start, step) -> list:
    """
    Getting ids of songs by the title song and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs by title
    """
    sql_request = sql_request_songs.sql_request_songs_by_title(content['value'])
    content['order'] = 'order by billboard.position, artist.id_artist'
    ids = _get_ids_song(sql_request, start, step)
    return ids


def __get_songs_ids_by_genre(content, start, step) -> list:
    """
    Getting ids of songs by the genre song and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs by genre
    """
    sql_request = sql_request_songs.sql_request_songs_by_genre(content['value'])
    content['order'] = 'order by billboard.position, artist.id_artist'
    ids = _get_ids_song(sql_request, start, step)
    return ids


def __get_songs_ids_by_year(content, start, step) -> list:
    """
    Getting ids of songs by year's of getting at billboard and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs by year
    """
    sql_request = sql_request_songs.sql_request_songs_by_year(content['value'])
    content['order'] = ' order by billboard.position'

    ids = _get_ids_song(sql_request, start, step)
    return ids


def __get_songs_ids_by_artist(content, start, step) -> list:
    """
    Getting ids of songs by performer artist name and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs by year
    """
    sql_request = sql_request_songs.sql_request_songs_by_artist(content['value'])
    content['order'] = 'order by billboard.position, artist.id_artist'
    ids = _get_ids_song(sql_request, start, step)
    return ids


def __get_songs_ids_hit_several_times(content, start, step) -> list:
    """
    Getting ids of songs that hit billboard several times and also add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs that hit billboard several times
    """
    sql_request = sql_request_songs.sql_request_songs_hit_several_times()
    content['order'] = 'order by billboard.position, artist.id_artist'
    ids = _get_ids_song(sql_request, start, step)
    return ids


def _get_ids_song(sql_request, start=0, step=0) -> list:
    """
    Getting ids of songs list by sql request
    :param sql_request: sql request
    :param start: the start row
    :param step: number of rows
    :return: list ids of songs by sql request
    """
    sql_request += ' and song.id_song is not null'
    sql_request = limit_information(sql_request, start, step)
    sql_data = get_data_from_db(sql_request)
    id_songs = create_ids(sql_data)
    return id_songs
