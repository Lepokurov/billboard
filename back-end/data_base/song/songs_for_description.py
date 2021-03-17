from connection_to_data_base import get_data_from_db
from sql_request_songs import sql_request_song, sql_request_songs_artist, sql_request_songs_year, \
    sql_request_songs_genre


def get_song(id_song) -> tuple:
    """
    get all information (columns) about song by id
    :param id_song: id of song
    :return: tuple song data
    """
    sql_request = sql_request_song(id_song)
    sql_data = get_data_from_db(sql_request)
    return sql_data


def get_songs_artist(id_artist, id_song_pass=0, limit=0) -> tuple:
    """
    Get artist's songs data tuple
    :param id_artist: id of artist
    :param id_song_pass: id song to skip
    :param limit: limit songs
    :return: artist's songs data tuple
    """
    sql_request = sql_request_songs_artist(id_artist, id_song_pass, limit)

    sql_data = get_data_from_db(sql_request)

    return sql_data


def get_songs_year(year) -> tuple:
    """
    get year's song data tuple
    :param year: year :)
    :return: year's song data tuple
    """
    sql_request = sql_request_songs_year(year)
    sql_data = get_data_from_db(sql_request)

    return sql_data


def get_songs_genre(id_genre, limit=0) -> tuple:
    """
    Get genre's song data tuple
    :param id_genre: id of genre
    :param limit: limit songs
    :return: genre's song data tuple
    """
    sql_request = sql_request_songs_genre(id_genre, limit)
    sql_data = get_data_from_db(sql_request)

    return sql_data
