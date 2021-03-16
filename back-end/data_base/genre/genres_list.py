from connection_to_data_base import get_data_from_db
from models import create_genres_info
from sql_request_genres import sql_constructor_genres


def get_genres_all(start, step, sort='song'):
    """
    Getting list genres from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :param sort: genre sorting by 'sort', the default sorting is by song
    :return: list of songs
    """
    sql_request = sql_constructor_genres(start, step, sort)
    sql_data = get_data_from_db(sql_request)

    genres = create_genres_info(sql_data)
    return genres

