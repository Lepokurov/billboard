from connection_to_data_base import get_data_from_db
from sql_request_genres import sql_constructor_genres


def get_genres_all(start, step, sort='song') -> tuple:
    """
    Get tuple of genres data from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :param sort: genre sorting by 'sort', the default sorting is by song
    :return: tuple of genres data
    """
    sql_request = sql_constructor_genres(start, step, sort)
    sql_data = get_data_from_db(sql_request)

    return sql_data
