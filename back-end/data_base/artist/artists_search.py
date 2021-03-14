import sql_request_artists
from artists_list import get_artists_list
from sql_constructor_general import get_ids_by_request


def search_artists(content: dict, start: int, step: int) -> list:
    """
    Get artists by the required parameters
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list of artists by the required parameters
    """
    id_songs = _get_ids_artists_by_search(content, start, step)
    artists = get_artists_list(id_songs, content['order'])
    return artists


def _get_ids_artists_by_search(content: dict, start: int, step: int) -> list:
    """
    Searching artists ids by the required parameters
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list required ids of songs
    """
    ids = []
    if content['type'] == 'by_name':
        ids = __get_artists_ids_by_name(content, start, step)
    elif content['type'] == 'by_genre':
        ids = __get_artists_ids_by_genre(content, start, step)
    elif content['type'] == 'by_song':
        ids = __get_artists_ids_by_song(content, start, step)
    elif content['type'] == 'dead':
        ids = __get_artists_ids_dead(content, start, step)

    return ids


def __get_artists_ids_by_name(content, start, step) -> list:
    """
    Getting ids of artists by the name artist and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of artists by name
    """
    sql_request = sql_request_artists.sql_request_artists_by_name(content['value'])
    content['order'] = ''
    ids = get_ids_by_request(sql_request, start, step)
    return ids


def __get_artists_ids_by_song(content, start, step) -> list:
    """
    Getting ids of artists by title performed songs and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of artists by title performed songs
    """
    sql_request = sql_request_artists.sql_request_artists_by_song(content['value'])
    content['order'] = 'order by artist.id_artist'
    ids = get_ids_by_request(sql_request, start, step)
    return ids


def __get_artists_ids_by_genre(content, start, step) -> list:
    """
    Getting ids of artists by genre artist and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of artists by genre artist
    """
    sql_request = sql_request_artists.sql_request_artists_by_genre(content['value'])
    content['order'] = 'order by artist.id_artist'
    ids = get_ids_by_request(sql_request, start, step)
    return ids


def __get_artists_ids_dead(content, start, step) -> list:
    """
    Getting ids of dead artists and add to content a sort information
    :param content: dictionary that contain the type and value of searching
    :param start: the start row
    :param step: number of rows
    :return: list ids of dead artists
    """
    sql_request = sql_request_artists.sql_request_artists_dead()
    content['order'] = 'order by artist.id_artist'
    ids = get_ids_by_request(sql_request, start, step)
    return ids
