from connection_to_data_base import get_data_from_db
from sql_constructor_general import get_ids_all
from sql_request_artists import sql_constructor_artists


def get_artists_all(start: int, step: int) -> tuple:
    """
    Getting list artists from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: sql artist data
    """
    id_artists = get_ids_all(start, step)
    order = 'order artist.id_artist'
    sql_data = _get_artists_list(id_artists, order)
    return sql_data


def _get_artists_list(id_artists: list, order='') -> tuple:
    """
     Main function for getting list of artists by ids
    :param id_artists: list of required ids of artists
    :param order: request information of 'order by'
    :return: sql tuple of artists data or empty tuple if doesn't have required information
    """
    sql_request = sql_constructor_artists(id_artists, order)
    if sql_request == '':
        return ()
    sql_data = get_data_from_db(sql_request)

    return sql_data
