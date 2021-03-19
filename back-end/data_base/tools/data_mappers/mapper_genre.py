from mapper_general import create_data


def create_genre(sql_data: tuple):
    """
    Create genre dict.
    :param sql_data: sql data
    :return: dict of artist
    """
    sql_data = sql_data[0]
    genre = create_data(sql_data)
    return genre


def create_genres_list(sql_data: tuple):
    """
    Create genre list.
    :param sql_data: sql data
    :return: list of genres
    """
    genres = []
    for sql_line in sql_data:
        genre = create_data(sql_line)
        genre['songs_count'] = sql_line[3]
        genres.append(genre)
    return genres


def create_genres(sql_data: tuple) -> list:
    """
    Create genre list. Used to describe objects
    :param sql_data: sql data
    :return: list of genres
    """
    genres = []
    for sql_line in sql_data:
        genre = create_data(sql_line)
        genres.append(genre)
    return genres


def create_genres_count(songs_count: int, artists_count: int) -> dict:
    """
    Count song and artist of genre
    :param songs_count: song count
    :param artists_count: artist count
    :return: dict
    """
    genres_count = {
        'songs': songs_count,
        'artists': artists_count
    }
    return genres_count
