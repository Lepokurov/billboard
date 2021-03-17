from connection_to_data_base import get_data_from_db
from sql_request_artists import sql_request_featuring_artists, sql_request_artist, sql_request_performers_of_song, \
    sql_request_artists_year, sql_request_artists_genre


def get_artist(id_artist: int) -> tuple:
    """
    get all information (columns) about artist by id
    :param id_artist: id of artist
    :return: sql artist data
    """
    sql_request = sql_request_artist(id_artist)
    sql_data = get_data_from_db(sql_request)
    return sql_data


def get_featuring_artists(id_artist: int) -> tuple:
    """
    get all the artists with whom current artist has performed songs
    :param id_artist: id of artist
    :return: sql artist data tuple
    """
    sql_request = sql_request_featuring_artists(id_artist)

    sql_data = get_data_from_db(sql_request)
    return sql_data


def get_performers_of_song(id_song: int) -> tuple:
    """
    get all performer's artists of song by song id
    :param id_song: id of song
    :return: sql artist data tuple
    """
    sql_request = sql_request_performers_of_song(id_song)

    sql_data = get_data_from_db(sql_request)
    return sql_data


def get_artists_year(year: int) -> tuple:
    """
    get all performer's artists of songs by billboard year
    :param year: billboard year
    :return: sql artist data tuple
    """
    sql_request = sql_request_artists_year(year)

    sql_data = get_data_from_db(sql_request)

    artists = models.create_data_year(sql_data)
    return artists


def get_artists_genre(id_genre: int, limit=0) -> tuple:
    """
    get all artist by the genre
    :param id_genre: id of genre
    :param limit: limit of genres
    :return: sql artist data tuple
    """
    sql_request = sql_request_artists_genre(id_genre, limit)

    sql_data = get_data_from_db(sql_request)

    return sql_data
