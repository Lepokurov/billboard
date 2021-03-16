from connection_to_data_base import get_data_from_db
from models import create_songs_info
from sql_constructor_general import get_ids_all
from sql_request_songs import sql_constructor_songs


def get_songs_all(start, step) -> list:
    """
    Getting list songs from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: list of songs
    """
    id_songs = get_ids_all(start, step)
    songs = get_songs_list(id_songs)
    return songs


def get_songs_list(id_songs: list, order='') -> list:
    """
    Main function for getting list of songs by ids
    :param id_songs: list required ids of songs
    :param order: request information of 'order by'
    :return: list of songs or empty list if doesn't have required information
    """
    sql_request = sql_constructor_songs(id_songs, order)
    if sql_request == '':
        return []

    sql_data = get_data_from_db(sql_request)
    songs = create_songs_info(sql_data)
    return songs



