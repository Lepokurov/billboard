def create_song(sql_data: tuple):
    sql_data = sql_data[0]
    song = {
        'id': sql_data[0],
        'title': sql_data[1],
        'released': sql_data[2],
        'length': sql_data[3],
        'album': sql_data[4],
        'image': sql_data[5],
        'wiki_link': sql_data[6],
        'youtube_link': sql_data[7]
    }
    return song


def decorator_list(create_dict):
    """
    From dict to list
    :param create_dict: function where i created dict (but need list)
    :return: song list
    """
    def wrapper(sql_data):
        songs_dict = create_dict(sql_data)
        song_list = []
        for song in songs_dict.values():
            song_list.append(song)
        return song_list
    return wrapper


@decorator_list
def create_songs_list(sql_data: tuple):
    """
    It's create the dict of songs by sql the request
    :param sql_data: sql data
    :return: dict of songs
    """
    # I written that nightmare for increasing speed of loading.
    # 1 request to bd more faster that 200 (50 songs * find artists * years in billboard)
    # I try to unit the column at request, byt it's was broke the sort, and the sort is so important to my project
    # i don't have time to figure out how i can unit the columns and save the sort. I imagine it's like a legacy code
    # And i actually don't already remember as well how this beast is work.
    songs = {}

    id_song_list = {}
    id_elem = 0

    for sql_line in sql_data:
        if songs == {} or not sql_line[0] in id_song_list:
            id_elem += 1
            id_song_list[sql_line[0]] = id_elem
            song = {
                'id': sql_line[0],
                'title': sql_line[1],
                'album': sql_line[2],
                'image': sql_line[3],
                'artists':  sql_line[4],
                'billboard': {}
            }
            id_billboard = 1
            billboard = {
                'year': sql_line[5],
                'position': sql_line[6]
            }
            song['billboard'][id_billboard] = billboard
            songs[id_elem] = song

        else:
            current_id = id_song_list[sql_line[0]]
            if sql_line[4] not in songs[current_id]['artists']:
                songs[current_id]['artists'] += ', ' + sql_line[4]

            new_year = False
            billboard = {
                'year': sql_line[5],
                'position': sql_line[6]
            }
            for billboard_ in songs[current_id]['billboard'].values():
                if billboard == billboard_:
                    new_year = False
                    break
                new_year = True

            if new_year:
                # last id
                id_billboard = int(sorted(songs[current_id]['billboard'])[-1]) + 1
                songs[current_id]['billboard'][id_billboard] = billboard

    return songs


@decorator_list
def create_songs_artist(sql_data):
    """
    create data of songs of the artist
    :param sql_data: sql data
    :return: songs of artist
    """
    songs = {}
    id_elem = 0
    id_billboard = 0
    for sql_line in sql_data:
        billboard = {
            'year': sql_line[5],
            'position': sql_line[6]
        }
        if songs == {} or not songs[id_elem]['id'] == sql_line[0]:
            id_billboard = 1
            id_elem += 1
            # id_song = title_song, image_song
            songs[id_elem] = __song(sql_line)
            songs[id_elem]['billboard'] = {id_billboard: billboard}
        else:
            id_billboard += 1
            songs[id_elem]['billboard'][id_billboard] = billboard

    return songs


def create_songs_year(sql_data) -> list:
    songs = []

    for sql_line in sql_data:
        song = __song(sql_line)
        song['position'] = sql_line[4]
        songs.append(song)

    return songs


def create_songs_genre(sql_data) -> list:
    """
    create data of a songs of the genre
    :param sql_data: sql data
    :return: list of songs
    """
    songs = []
    for sql_line in sql_data:
        song = __song(sql_line)
        songs.append(song)

    return songs


def __song(sql_data) -> dict:
    """
    Create song
    :param sql_data: sql data
    :return: song dict
    """
    song = {
        'id': sql_data[0],
        'title': sql_data[1],
        'released': sql_data[2],
        'image': sql_data[3]
    }
    return song
