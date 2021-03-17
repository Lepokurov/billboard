from connection_to_data_base import get_data_from_db
from sql_constructor_general import get_ids_by_request
from sql_request_years import _sql_request_billboard_song, _sql_request_years_genre
from years_list import _get_years_list


def get_billboard_song(id_song) -> tuple:
    """
    Get billboard year and position of song
    :param id_song: id song
    :return: year and position data
    """
    sql_request = _sql_request_billboard_song(id_song)

    sql_data = get_data_from_db(sql_request)

    return sql_data


def get_years_genre(id_genre) -> tuple:
    """
    get years that has song with current genre
    :param id_genre: current genre
    :return: tuple years data
    """
    # It's look strange
    years_list = get_ids_by_request(_sql_request_years_genre(id_genre))
    years_data = _get_years_list(years_list)

    return years_data

