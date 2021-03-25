from connection_to_data_base import get_data_from_db
from mapper_artist import create_artists_list
from sql_constructor_general import get_ids_all
from sql_request_artists import sql_constructor_artists


def get_artists_all(start: int, step: int) -> list:
    """
    Getting list artists from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: list artists data
    """
    id_artists = get_ids_all(start, step)
    order = 'order by artist.id_artist'
    artists = _get_artists_list(id_artists, order)
    return artists


def _get_artists_list(id_artists: list, order='') -> list:
    """
     Main function for getting list of artists by ids
    :param id_artists: list of required ids of artists
    :param order: request information of 'order by'
    :return: list of artists data or empty list if doesn't have required information
    """
    sql_request = sql_constructor_artists(id_artists, order)
    if sql_request == '':
        return []
    sql_data = get_data_from_db(sql_request)

    artists = create_artists_list(sql_data)
    return artists
