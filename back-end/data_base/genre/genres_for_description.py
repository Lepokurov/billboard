from connection_to_data_base import get_data_from_db
from sql_request_genres import sql_request_genre, sql_request_genres_year, sql_request_genres_artist, \
    sql_request_genres_song


def get_genre(id_genre) -> tuple:
    """
    get all information (columns) about genre by id
    :param id_genre: id of song
    :return: genre
    """
    sql_request = sql_request_genre(id_genre)
    sql_data = get_data_from_db(sql_request)
    return sql_data


def get_genres_year(year) -> tuple:
    """
    get year's genre data
    :param year: billboard year
    :return: genre data
    """
    sql_request = sql_request_genres_year(year)

    sql_data = get_data_from_db(sql_request)

    return sql_data


def get_genres_artist(id_artist) -> tuple:
    """
    Get artist's genre data
    :param id_artist: id of artist
    :return: artist's genre data
    """
    sql_request = sql_request_genres_artist(id_artist)

    sql_data = get_data_from_db(sql_request)

    return sql_data


def get_genres_song(id_song) -> tuple:
    """
    Get song's genre data
    :param id_song: id of song
    :return: sql song's genre data
    """
    sql_request = sql_request_genres_song(id_song)

    sql_data = get_data_from_db(sql_request)

    return sql_data
