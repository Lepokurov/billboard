from connection_to_data_base import get_data_from_db
from mapper_song import create_song, create_songs_genre, create_songs_year, create_songs_artist
from sql_request_songs import sql_request_song, sql_request_songs_artist, sql_request_songs_year, \
    sql_request_songs_genre


def get_song(id_song: int) -> dict:
    """
    get all information (columns) about song by id
    :param id_song: id of song
    :return: dict song data
    """
    sql_request = sql_request_song(id_song)
    sql_data = get_data_from_db(sql_request)
    song = create_song(sql_data)
    return song


def get_songs_artist(id_artist: int, id_song_pass=0, limit=0) -> list:
    """
    Get artist's songs data tuple
    :param id_artist: id of artist
    :param id_song_pass: id song to skip
    :param limit: limit songs
    :return: artist's songs data dict
    """
    sql_request = sql_request_songs_artist(id_artist, id_song_pass, limit)

    sql_data = get_data_from_db(sql_request)
    songs = create_songs_artist(sql_data)
    return songs


def get_songs_year(year: int) -> list:
    """
    get year's song data tuple
    :param year: year :)
    :return: year's song data dict
    """
    sql_request = sql_request_songs_year(year)
    sql_data = get_data_from_db(sql_request)
    songs = create_songs_year(sql_data)
    return songs


def get_songs_genre(id_genre: int, limit=0) -> list:
    """
    Get genre's song data tuple
    :param id_genre: id of genre
    :param limit: limit songs
    :return: genre's song data tuple
    """
    sql_request = sql_request_songs_genre(id_genre, limit)
    sql_data = get_data_from_db(sql_request)
    songs = create_songs_genre(sql_data)
    return songs
