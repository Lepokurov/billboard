from sql_constructor_general import get_count, get_count_table
import sql_request_songs


def get_count_all_song() -> int:
    return get_count_table('song')


def get_count_song_by_title(title) -> int:
    """
    Getting count of songs with this title
    :param title: title of song
    :return: count
    """
    sql_request = sql_request_songs.sql_request_songs_by_title(title, True)

    count = get_count(sql_request)
    return count


def get_count_song_by_artist(artist) -> int:
    """
    Getting count of songs with this artist
    :param artist: name of artist
    :return: count
    """
    sql_request = sql_request_songs.sql_request_songs_by_artist(artist, True)

    count = get_count(sql_request)
    return count


def get_count_song_by_year(year) -> int:
    """
    Getting count of songs with this year
    :param year: year's of getting at billboard
    :return: count
    """
    sql_request = sql_request_songs.sql_request_songs_by_year(year, True)

    count = get_count(sql_request)
    return count


def get_count_song_by_genre(genre) -> int:
    """
    Getting count of songs with this genre
    :param genre: name genre
    :return: count
    """
    sql_request = sql_request_songs.sql_request_songs_by_genre(genre, True)

    count = get_count(sql_request)
    return count


def get_count_song_billboard_more_once() -> int:
    """
     Getting count of songs that hits billboard several times
    :return: count
    """
    sql_request = sql_request_songs.sql_request_songs_hit_several_times(True)

    count = get_count(sql_request)
    return count
