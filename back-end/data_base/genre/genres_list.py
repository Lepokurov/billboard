from connection_to_data_base import get_data_from_db
from mapper_genre import create_genres_list
from sql_request_genres import sql_constructor_genres


def get_genres_all(content: dict, start=0, step=0) -> list:
    """
    Get list of genres data from start to end (start+step) inclusive
    :param content: dictionary that contain the type and value
    :param start: the start row
    :param step: number of rows
    :return: list of genres data
    """
    sql_request = sql_constructor_genres(start, step, content['type'])
    genres = _get_genres_list(sql_request)
    return genres


def _get_genres_list(sql_request):
    """
    get list of genres by slq request
    :param sql_request: slq request
    :return: list of genres
    """
    sql_data = get_data_from_db(sql_request)
    genres = create_genres_list(sql_data)
    return genres
