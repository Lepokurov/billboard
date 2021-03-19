from connection_to_data_base import get_data_from_db
from mapper_year import create_billboard_of_song, create_years_genre
from sql_constructor_general import get_ids_by_request
from sql_request_years import _sql_request_billboard_song, _sql_request_years_genre
from years_list import get_years_list


def get_billboard_of_song(id_song) -> list:
    """
    Get billboard year and position of song
    :param id_song: id song
    :return: year and position data
    """
    sql_request = _sql_request_billboard_song(id_song)

    sql_data = get_data_from_db(sql_request)
    billboard = create_billboard_of_song(sql_data)
    return billboard


def get_years_genre(id_genre) -> dict:
    """
    get years that has song with current genre
    :param id_genre: current genre
    :return: tuple years data
    """
    # It's look strange, but it's fine, probably
    sql_request = _sql_request_years_genre(id_genre)
    sql_data = get_data_from_db(sql_request)
    years_list = get_ids_by_request(sql_request)
    years_data = get_years_list(years_list)

    years = create_years_genre(sql_data, years_data)
    return years
