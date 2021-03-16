from connection_to_data_base import get_data_from_db
from models import create_genre, create_data_year, create_genres
from sql_request_genres import sql_request_genre, sql_request_genres_year, sql_request_genres_artist, \
    sql_request_genres_song


def get_genre(id_genre):
    """
    get all information (columns) about genre by id
    :param id_genre: id of song
    :return: genre
    """
    sql_request = sql_request_genre(id_genre)
    sql_data = get_data_from_db(sql_request)
    genre = create_genre(sql_data[0])
    return genre


def get_genres_year(year) -> list:
    """
    get year's genre list
    :param year: billboard year
    :return: genre list
    """
    sql_request = sql_request_genres_year(year)

    sql_data = get_data_from_db(sql_request)

    genres = create_data_year(sql_data)
    return genres


def get_genres_artist(id_artist) -> list:
    """
    Get artist's genre list
    :param id_artist: id of artist
    :return: artist's genre list
    """
    sql_request = sql_request_genres_artist(id_artist)

    sql_data = get_data_from_db(sql_request)

    genres = create_genres(sql_data)
    return genres


def get_genres_song(id_song) -> list:
    """
    Get song's genre list
    :param id_song: id of song
    :return: song's genre list
    """
    sql_request = sql_request_genres_song(id_song)

    sql_data = get_data_from_db(sql_request)

    genres = create_genres(sql_data)
    return genres
