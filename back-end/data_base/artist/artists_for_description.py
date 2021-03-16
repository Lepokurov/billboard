from connection_to_data_base import get_data_from_db
from sql_request_artists import sql_request_featuring_artists, sql_request_artist, sql_request_performers_of_song, \
    sql_request_artists_year, sql_request_artists_genre


def get_artist(id_artist):
    """
    get all information (columns) about artist by id
    :param id_artist: id of artist
    :return: artist
    """
    sql_request = sql_request_artist(id_artist)
    sql_data = get_data_from_db(sql_request)
    artist = models.create_artist(sql_data[0])
    return artist


def get_featuring_artists(id_artist) -> list:
    """
    get all the artists with whom current artist has performed songs
    :param id_artist: id of artist
    :return: artist list
    """
    sql_request = sql_request_featuring_artists(id_artist)

    sql_data = get_data_from_db(sql_request)

    artists = models.create_featuring_artists(sql_data, id_artist)
    return artists


def get_performers_of_song(id_song) -> list:
    """
    get all performer's artists of song by song id
    :param id_song: id of song
    :return: artist list
    """
    sql_request = sql_request_performers_of_song(id_song)

    sql_data = get_data_from_db(sql_request)

    artists = models.create_artists(sql_data)
    return artists


def get_artists_year(year) -> list:
    """
    get all performer's artists of songs by billboard year
    :param year: billboard year
    :return: artist list
    """
    sql_request = sql_request_artists_year(year)

    sql_data = get_data_from_db(sql_request)

    artists = models.create_data_year(sql_data)
    return artists


def get_artists_genre(id_genre, limit=0) -> list:
    """
    get all artist by the genre
    :param id_genre: id of genre
    :param limit: limit of genres
    :return: artist list
    """
    sql_request = sql_request_artists_genre(id_genre, limit)

    sql_data = get_data_from_db(sql_request)

    artists = models.create_artists(sql_data)

    return artists
