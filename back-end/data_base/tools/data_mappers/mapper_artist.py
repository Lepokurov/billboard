from mapper_general import create_data


def create_artist(sql_data: tuple) -> dict:
    """
    Create artist dict.
    :param sql_data: sql data
    :return: dict of artist
    """
    sql_data = sql_data[0]
    artist = __artist(sql_data)
    artist['wiki_link'] = sql_data[5]
    artist['bio'] = sql_data[6][1:-1]
    return artist


def create_artists_list(sql_data: tuple) -> list:
    """
    Create artist list.
    :param sql_data: sql data
    :return: list of artists
    """
    artists = []
    for sql_line in sql_data:
        artist = create_data(sql_line)
        artist['songs_count'] = sql_line[5]
        artists.append(artist)
    return artists


def create_artists(sql_data: tuple) -> list:
    """
    Create artist list. Used to describe objects
    :param sql_data: sql data
    :return: list of artists
    """
    artists = []
    for sql_line in sql_data:
        artist = create_data(sql_line)
        artists.append(artist)
    return artists


def __artist(sql_data: tuple) -> dict:
    """
    Create artist
    :param sql_data: sql data
    :return: artist dict
    """
    artist = {
        'id': sql_data[0],
        'name': sql_data[1],
        'age': __create_age(sql_data[2]),
        'group': sql_data[3],
        'image': sql_data[4]
    }
    return artist


def __create_age(date: str) -> int:
    """
    Convert data
    :param date: date data
    :return: age of artist (if artist is dead that return negative number. Number is age of death of artist)
    """
    # if 24 or -78(dead person) then get it right from db
    if date.isdigit() or len(date) < 4:
        return int(date)
    import datetime
    date_artist = datetime.datetime.strptime(date, "%Y-%m-%d")
    date_now = datetime.datetime.today()
    date_delta = date_now - date_artist
    age = int(date_delta.days)//365
    return age
