import sql_request_artists
from connection_to_data_base import get_count
from sql_constructor_general import get_count_table


def get_count_all_artist() -> int:
    sql_request = get_count_table('artist')

    count = get_count(sql_request)
    return count


def get_count_artists_by_name(name) -> int:
    """
    Getting count of the artists with this name
    :param name: artist name
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_name(name, True)

    count = get_count(sql_request)
    return count


def get_count_artists_by_song(song) -> int:
    """
    Getting count of the artists who performed this song
    :param song: title of song
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_song(song, True)

    count = get_count(sql_request)
    return count


def get_count_artists_by_genre(genre) -> int:
    """
    Getting count of the artists with this genre
    :param genre: name of genre
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_genre(genre, True)

    count = get_count(sql_request)
    return count


def get_count_artists_dead() -> int:
    """
    Getting count of the dead artists
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_dead(True)

    count = get_count(sql_request)
    return count

