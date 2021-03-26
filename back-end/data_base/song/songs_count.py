from connection_to_data_base import get_count
from sql_constructor_general import get_count_table
from sql_request_songs import sql_request_songs_by_title, sql_request_songs_by_artist, sql_request_songs_by_year, \
    sql_request_songs_by_genre, sql_request_songs_hit_several_times


def get_count_songs(content) -> int:
    """
    get count of song by required content
    :param content: dictionary that contain the type and value of searching
    :return: count
    """
    count = 0
    if content['type'] == 'by_title':
        count = __get_count_song_by_title(content['value'])
    elif content['type'] == 'by_genre':
        count = __get_count_song_by_genre(content['value'])
    elif content['type'] == 'by_year':
        count = __get_count_song_by_year(content['value'])
    elif content['type'] == 'by_artist':
        count = __get_count_song_by_artist(content['value'])
    elif content['type'] == 'hit_several_times':
        count = __get_count_song_billboard_more_once()
    elif content['type'] == 'all':
        count = __get_count_all_song()
    return count


def __get_count_all_song() -> int:
    """
    get count of all song
    :return: count of songs
    """
    sql_request = get_count_table('song')

    count = get_count(sql_request)
    return count


def __get_count_song_by_title(title) -> int:
    """
    Getting count of songs with this title
    :param title: title of song
    :return: count
    """
    sql_request = sql_request_songs_by_title(title, True)

    count = get_count(sql_request)
    return count


def __get_count_song_by_artist(artist) -> int:
    """
    Getting count of songs with this artist
    :param artist: name of artist
    :return: count
    """
    sql_request = sql_request_songs_by_artist(artist, True)

    count = get_count(sql_request)
    return count


def __get_count_song_by_year(year) -> int:
    """
    Getting count of songs with this year
    :param year: year's of getting at billboard
    :return: count
    """
    sql_request = sql_request_songs_by_year(year, True)

    count = get_count(sql_request)
    return count


def __get_count_song_by_genre(genre) -> int:
    """
    Getting count of songs with this genre
    :param genre: name genre
    :return: count
    """
    sql_request = sql_request_songs_by_genre(genre, True)

    count = get_count(sql_request)
    return count


def __get_count_song_billboard_more_once() -> int:
    """
     Getting count of songs that hits billboard several times
    :return: count
    """
    sql_request = sql_request_songs_hit_several_times(True)

    count = get_count(sql_request)
    return count
