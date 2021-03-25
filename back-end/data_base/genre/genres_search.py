from genres_list import _get_genres_list
from sql_request_genres import sql_constructor_genres


def search_genres(content: dict, start=0, step=0) -> list:
    """
    Get list of genres data by search from start to end (start+step) inclusive
    :param content: dictionary that contain the type and value
    :param start: the start row
    :param step: number of rows
    :return: list of genres data
    """
    sql_request = sql_constructor_genres(start, step, 'by_song', content['value'])
    genres = _get_genres_list(sql_request)
    return genres
