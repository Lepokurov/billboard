from connection_to_data_base import get_data_from_db
from models import create_songs_artist, create_song
from sql_request_songs import sql_request_song, sql_request_songs_artist, sql_request_songs_year, \
    sql_request_songs_genre


def get_song(id_song) -> dict:
    """
    get all information (columns) about song by id
    :param id_song: id of song
    :return: song
    """
    sql_request = sql_request_song(id_song)
    sql_data = get_data_from_db(sql_request)
    song = create_song(sql_data[0])
    return song


def get_songs_artist(id_artist, id_song_pass=0, limit=0) -> dict:
    """
    Get artist's songs list
    :param id_artist: id of artist
    :param id_song_pass: id song to skip
    :param limit: limit songs
    :return: artist's songs list
    """
    sql_request = sql_request_songs_artist(id_artist, id_song_pass, limit)

    sql_data = get_data_from_db(sql_request)

    songs = create_songs_artist(sql_data, id_song_pass)

    return songs


def get_songs_year(year) -> dict:
    """
    get year's song list
    :param year: year :)
    :return: year's song list
    """
    sql_request = sql_request_songs_year(year)
    sql_data = get_data_from_db(sql_request)

    songs = models.create_songs_year(sql_data)

    return songs


def get_songs_genre(id_genre, limit=0) -> dict:
    """
    Get genre's song list
    :param id_genre: id of genre
    :param limit: limit songs
    :return: genre's song list
    """
    sql_request = sql_request_songs_genre(id_genre, limit)
    sql_data = get_data_from_db(sql_request)

    songs = models.create_songs_genre(sql_data)

    return songs
