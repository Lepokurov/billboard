from connection_to_data_base import get_data_from_db
from models import create_billboard_song
from sql_constructor_general import get_ids_by_request
from sql_request_years import sql_request_billboard_song, sql_request_years_genre
from years_list import get_years_list


def get_billboard_song(id_song) -> list:
    """
    Get billboard year and position of song
    :param id_song: id song
    :return: year and position
    """
    sql_request = sql_request_billboard_song(id_song)

    sql_data = get_data_from_db(sql_request)

    billboard_song = create_billboard_song(sql_data)
    return billboard_song


def get_years_genre(id_genre) -> list:
    """
    get years that has song with current genre
    :param id_genre: current genre
    :return: years list
    """
    # It's look strange
    years_list = get_ids_by_request(sql_request_years_genre(id_genre))
    years_data = get_years_list(years_list)

    years = models.create_years_genre(sql_request_years_genre(id_genre), years_data)
    return years

