
def create_artist(sql_data):
    artist = {
        'id': sql_data[0],
        'name': sql_data[1],
        'age': _create_age(sql_data[2]),
        'group': sql_data[3],
        'image': sql_data[4],
        'wiki_link': sql_data[5],
        'bio': sql_data[6][1:-1]
    }
    return artist


def _create_age(data: str):
    if data.isdigit() or len(data)<4:
        return data
    import datetime
    date_artist = datetime.datetime.strptime(data, "%Y-%m-%d")
    date_now = datetime.datetime.today()
    date_delta = date_now - date_artist
    years = int(date_delta.days)//365
    return years


def create_song(sql_data):
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


def create_genre(sql_data):
    genre = {
        'id': sql_data[0],
        'name': sql_data[1],
        'image': sql_data[2],
    }
    return genre


def create_ids(sql_data):
    ids = [int(sql_line[0]) for sql_line in sql_data]
    a = 1
    return ids


def create_songs_info(sql_data):
    # I written that nightmare for increasing speed of loading.
    # 1 request to bd more faster that 200 (50 songs * find artists * years in billboard)
    # I rty to unit the column at request, byt it's was broke sort, and sor t is so important to my project
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
                # If more 40 rows the data of artists is reversed. I don't know why. 'Order by' no help.
                #if len(sql_data) > 50:
                #    songs[current_id]['artists'] = sql_line[4] + ', ' + songs[current_id]['artists']
                #else:
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


def create_artists_info(sql_data):
    artists = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        artists[id_elem] = {
            'id': sql_line[0],
            'name': sql_line[1],
            'age': _create_age(sql_line[2]),
            'image': sql_line[3],
            'group': sql_line[4],
            'songs_count': sql_line[5]
        }
    return artists


def create_years_info(sql_data):
    years = {}
    id_elem = int(sql_data[0][0]) + 1
    for sql_line in sql_data:
        if years == {} or not int(id_elem) == int(sql_line[0]):
            id_elem = sql_line[0]
            years[id_elem] = {
                'year': sql_line[0],
                'artists': sql_line[1],
                'title': sql_line[2],
                'image': sql_line[3],
            }
        else:
            years[id_elem]['artists'] += ', ' + sql_line[1]
    return years


def create_genres_info(sql_data):
    genres = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        genres[id_elem] = {
            'id': sql_line[0],
            'name': sql_line[1],
            'image': sql_line[2],
            'songs_count': sql_line[3]
        }
    return genres


def create_songs_artist(sql_data, id_song):
    songs = {}
    id_elem = 0
    id_billboard = 0
    for sql_line in sql_data:
        if str(id_song) == str(sql_line[0]):
            continue
        billboard = {
            'year': sql_line[4],
            'position': sql_line[5]
        }
        if songs == {} or not songs[id_elem]['id'] == sql_line[0]:
            id_billboard = 1
            id_elem += 1
            # id_song = title_song, image_song
            songs[id_elem] = {
                'id': sql_line[0],
                'title': sql_line[1],
                'released': sql_line[2],
                'image': sql_line[3],
                'billboard': {id_billboard: billboard}
            }
        else:
            id_billboard += 1
            songs[id_elem]['billboard'][id_billboard] = billboard

    return songs


def create_songs_year(sql_data):
    songs = {}
    id_elem = 0

    for sql_line in sql_data:
        id_elem += 1
        songs[id_elem] = {
            'id': sql_line[0],
            'title': sql_line[1],
            'released': sql_line[2],
            'image': sql_line[3],
            'position': sql_line[4],
        }

    return songs


def create_genres(sql_data):
    genres = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        genres[id_elem] = create_genre(sql_line)
    return genres


def create_billboard_song(sql_data):
    billboard_song = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        billboard_song[id_elem] = {
            'year': sql_line[0],
            'position': sql_line[1]
        }
    return billboard_song


def create_artists(sql_data):
    artists = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        artists[id_elem] = {
            'id': sql_line[0],
            'name': sql_line[1],
            'image': sql_line[2]
        }
    return artists


def create_data_year(sql_data):
    data = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        data[id_elem] = {
            'id': sql_line[0],
            'name': sql_line[1],
            'image': sql_line[2],
            'count':  sql_line[3]
        }
    return data


def create_featuring_artists(sql_data, id_artist):
    sql_data = set(sql_data)
    new_data = []
    for sql_line in sql_data:
        if not sql_line[0] == int(id_artist):
            new_data.append(sql_line)
    artists = create_artists(new_data)
    return artists


def create_years_genre(sql_data, years_data):
    for sql_line in sql_data:
        year = sql_line[0]
        years_data[year]['count'] = sql_line[1]
    return years_data


def create_songs_genre(sql_data):
    songs = {}
    id_elem = 0
    for sql_line in sql_data:
        id_elem += 1
        songs[id_elem] = {
            'id': sql_line[0],
            'title': sql_line[1],
            'released': sql_line[2],
            'image': sql_line[3]
        }

    return songs


def create_genres_count(songs_count, artists_count):
    genres_count = {
        'songs': songs_count,
        'artists': artists_count
    }
    return genres_count
