from connection_to_data_base import get_data_from_db
from mapper_artist import create_artist, create_artists
from mapper_general import create_data_of_year
from sql_request_artists import sql_request_featuring_artists, sql_request_artist, sql_request_performers_of_song, \
    sql_request_artists_year, sql_request_artists_genre


def get_artist(id_artist: int) -> dict:
    """
    get all information (columns) about artist by id
    :param id_artist: id of artist
    :return: dict artists data
    """
    sql_request = sql_request_artist(id_artist)
    sql_data = get_data_from_db(sql_request)
    artist = create_artist(sql_data)
    return artist


def get_featuring_artists(id_artist: int) -> list:
    """
    get all the artists with whom current artist has performed songs
    :param id_artist: id of artist
    :return: list artists data
    """
    sql_request = sql_request_featuring_artists(id_artist)

    sql_data = get_data_from_db(sql_request)
    artists = create_artists(sql_data)
    return artists


def get_performers_of_song(id_song: int) -> list:
    """
    get all performer's artists of song by song id
    :param id_song: id of song
    :return: list artists data
    """
    sql_request = sql_request_performers_of_song(id_song)

    sql_data = get_data_from_db(sql_request)
    artists = create_artists(sql_data)
    return artists


def get_artists_of_year(year: int) -> list:
    """
    get all performer's artists of songs by billboard year
    :param year: billboard year
    :return: list artists data
    """
    sql_request = sql_request_artists_year(year)

    sql_data = get_data_from_db(sql_request)
    artists = create_data_of_year(sql_data)
    return artists


def get_artists_genre(id_genre: int, limit=0) -> list:
    """
    get all artist by the genre
    :param id_genre: id of genre
    :param limit: limit of genres
    :return: list artists data
    """
    sql_request = sql_request_artists_genre(id_genre, limit)

    sql_data = get_data_from_db(sql_request)

    artists = create_artists(sql_data)
    return artists
