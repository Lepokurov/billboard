import sql_request_artists
from connection_to_data_base import get_count
from sql_constructor_general import get_count_table


def get_count_artists(content) -> int:
    """
    get count of artist by required content
    :param content: dictionary that contain the type and value of searching
    :return: count
    """
    count = 0
    if content['type'] == 'by_name':
        count = __get_count_artists_by_name(content['value'])
    elif content['type'] == 'by_song':
        count = __get_count_artists_by_song(content['value'])
    elif content['type'] == 'by_genre':
        count = __get_count_artists_by_genre(content['value'])
    elif content['type'] == 'dead':
        count = __get_count_artists_dead()
    elif content['type'] == 'group':
        count = __get_count_artists_group()
    elif content['type'] == 'all':
        count = __get_count_all_artist()
    return count


def __get_count_all_artist() -> int:
    """
    get count of all artist
    :return: count
    """
    sql_request = get_count_table('artist')

    count = get_count(sql_request)
    return count


def __get_count_artists_by_name(name: str) -> int:
    """
    Get count of the artists with this name
    :param name: artist name
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_name(name, True)

    count = get_count(sql_request)
    return count


def __get_count_artists_by_song(song: str) -> int:
    """
    Get count of the artists who performed this song
    :param song: title of song
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_song(song, True)

    count = get_count(sql_request)
    return count


def __get_count_artists_by_genre(genre: str) -> int:
    """
    Get count of the artists with this genre
    :param genre: name of genre
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_by_genre(genre, True)

    count = get_count(sql_request)
    return count


def __get_count_artists_dead() -> int:
    """
    Get count of the dead artists
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_dead(True)

    count = get_count(sql_request)
    return count


def __get_count_artists_group() -> int:
    """
    Get count of the dead artists
    :return: count
    """
    sql_request = sql_request_artists.sql_request_artists_group(True)

    count = get_count(sql_request)
    return count
