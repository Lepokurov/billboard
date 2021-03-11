import data_base


############# Songs  ##################
def get_songs_info(start, step, content):
    songs = {}

    if content['type'] == 'default':
        songs = data_base.get_songs_info_all(start, step)
    elif content['type'] == 'year':
        songs = data_base.get_songs_info_by_year(content['year'], start, step)
    elif content['type'] == 'random':
        songs = data_base.get_songs_info(start)
    elif content['type'] == 'artist':
        songs = data_base.get_songs_info_by_artist_name(content['artist_name'], start, step)
    elif content['type'] == 'title':
        songs = data_base.get_songs_info_by_title(content['title'], start, step)
    elif content['type'] == 'genre':
        songs = data_base.get_songs_info_by_genre(content['genre'], start, step)
    elif content['type'] == 'billboard_more_once':
        songs = data_base.get_songs_info_billboard_more_once(start, step)
    # i don't want to do it in html, and i prepared information here, but this is not necessary
    for song in songs.values():

        new_title = song['title'].split('(')[0]
        # If name started with (
        if new_title == '':
            new_title = song['title'].split(')')[1]
        if len(new_title) > 30:
            new_title = new_title[:30]+'...'
        song['title'] = new_title

        if len(song['album']) > 30:
            song['album'] = song['album'][:30] + '...'
        # for show only
        year = ''
        position = ''
        for billboard in song['billboard'].values():
            year += billboard['year'] + ', '
            position += str(billboard['position']) + ', '
        song['year'] = year[:-2]
        song['position'] = position[:-2]

    return songs


def get_random_index_songs():
    indexes_rnd = []
    count_songs = data_base.get_count_song()
    indexes_rnd.append(13)
    for i in range(53):
        import random
        ind = random.randint(1, count_songs)
        indexes_rnd.append(ind)
    content = {'type': 'random'}
    songs = get_songs_info(indexes_rnd, 0, content)
    return songs


def get_all_songs_navigation(page, content):
    step = 51
    start = step * (page - 1)
    songs = get_songs_info(start, step, content)
    return songs


def get_all_songs(page):
    content = {'type': 'default'}
    songs = get_all_songs_navigation(page, content)
    return songs


def get_all_songs_by_year(page, year):
    content = {'type': 'year', 'year': year}
    songs = get_all_songs_navigation(page, content)
    return songs


def get_all_songs_by_artist_name(page, artist_name):
    content = {'type': 'artist', 'artist_name': artist_name}
    songs = get_all_songs_navigation(page, content)
    return songs


def get_all_songs_by_title(page, title):
    content = {'type': 'title', 'title': title}
    songs = get_all_songs_navigation(page, content)
    return songs


def get_all_songs_by_genre(page, genre):
    content = {'type': 'genre', 'genre': genre}
    songs = get_all_songs_navigation(page, content)
    return songs


def get_all_songs_billboard_more_once(page):
    content = {'type': 'billboard_more_once'}
    songs = get_all_songs_navigation(page, content)
    return songs


############# Songs Count ##################
def get_all_songs_count():
    all_song_count = data_base.get_count_song()
    return all_song_count


def get_all_songs_count_by_year(year):
    all_song_count = data_base.get_count_song_by_year(year)
    return all_song_count


def get_all_songs_count_by_artist_name(artist_name):
    all_song_count = data_base.get_count_song_by_artist_name(artist_name)
    return all_song_count


def get_all_songs_count_by_title(title):
    all_song_count = data_base.get_count_song_by_title(title)
    return all_song_count


def get_all_songs_count_by_genre(genre):
    all_song_count = data_base.get_count_song_by_genre(genre)
    return all_song_count


def get_all_songs_count_billboard_more_once():
    all_song_count = data_base.get_count_song_billboard_more_once()
    return all_song_count


############# Song ##################
def get_song_info(id_song):
    song = data_base.get_song(id_song)
    artists = data_base.get_performers_song(id_song)
    for artist in artists.values():
        artist['other_songs'] = data_base.get_songs_artist(str(artist['id']), str(id_song), 7)
    song['artists'] = artists
    song['genres'] = data_base.get_genres_song(id_song)
    song['billboard'] = data_base.get_billboard_song(id_song)

    return song
#####################################


############# Artists ##################
def get_artists_info(start, step, content):
    artists = {}
    if content['type'] == 'default':
        artists = data_base.get_artists_info_all(start, step)
    elif content['type'] == 'name':
        artists = data_base.get_artists_info_by_name(content['name'], start, step)
    elif content['type'] == 'song':
        artists = data_base.get_artists_info_by_song(content['song'], start, step)
    elif content['type'] == 'genre':
        artists = data_base.get_artists_info_by_genre(content['genre'], start, step)
    elif content['type'] == 'dead':
        artists = data_base.get_artists_info_dead(start, step)

    for artist in artists.values():
        get_age_artist(artist)

    return artists


def get_all_artists_navigation(page, content):
    step = 51
    start = step * (page - 1)
    artists = get_artists_info(start, step, content)
    return artists


def get_all_artists(page):
    content = {'type': 'default'}
    artists = get_all_artists_navigation(page, content)
    return artists


def get_all_artists_by_name(page, name):
    content = {'type': 'name', 'name': name}
    artists = get_all_artists_navigation(page, content)
    return artists


def get_all_artists_by_song(page, song):
    content = {'type': 'song', 'song': song}
    artists = get_all_artists_navigation(page, content)
    return artists


def get_all_artists_by_genre(page, genre):
    content = {'type': 'genre', 'genre': genre}
    artists = get_all_artists_navigation(page, content)
    return artists


def get_all_artists_dead(page):
    content = {'type': 'dead'}
    artists = get_all_artists_navigation(page, content)
    return artists


############# Artist ##################
def get_artist_info(id_artist):
    artist = data_base.get_artist(id_artist)

    get_age_artist(artist)

    artist['genres'] = data_base.get_genres_artist(id_artist)
    artist['songs'] = data_base.get_songs_artist(id_artist)
    years = []
    for song in artist['songs'].values():
        for billboard in song['billboard'].values():
            years.append(billboard['year'])
    artist['feats'] = data_base.get_featuring_artists(id_artist)
    artist['years_info'] = data_base.get_years_info(years)
    return artist


############# Artists Count ##################
def get_all_artists_count():
    all_artist_count = data_base.get_count_artist()
    return all_artist_count


def get_all_artists_count_by_name(name):
    all_artist_count = data_base.get_count_artist_by_name(name)
    return all_artist_count


def get_all_artists_count_by_song(song):
    all_artist_count = data_base.get_count_artist_by_song(song)
    return all_artist_count


def get_all_artists_count_by_genre(genre):
    all_artist_count = data_base.get_count_artist_by_genre(genre)
    return all_artist_count


def get_all_artists_count_dead():
    all_artist_count = data_base.get_count_artist_dead()
    return all_artist_count


######### Artsits data ##############
def get_age_artist(artist):
    if artist['group'] == 'True':
        artist['age'] = 'The group'
    elif int(artist['age']) < 0:
        artist['age'] = str(artist['age'])[1:] + ' years (Dead)'
    else:
        artist['age'] = str(artist['age']) + ' years'
#####################################


############# Years ##################
def get_years_info(start, step, content):
    years = {}
    if content['type'] == 'default':
        years = data_base.get_years_info_all(start, step)
    elif content['type'] == 'search':
        years = data_base.get_years_info_search(content['search'], start, step)
    return years


def get_all_years_navigation(page, content):
    step = 21
    start = 2020 - ((page - 1) * step)
    years = get_years_info(start, step, content)
    return years


def get_all_years(page):
    content = {'type': 'default'}
    years = get_all_years_navigation(page, content)
    return years


def get_all_years_search(page, search):
    content = {'type': 'search', 'search': search}
    years = get_all_years_navigation(page, content)
    return years


############# Years count ##################
def get_all_years_count():
    all_years_count = data_base.get_count_year()
    return all_years_count


def get_all_years_count_search(search):
    all_years_count = data_base.get_count_year_search(search)
    return all_years_count


############# Year ##################
def get_year_info(year):
    year = {
        'songs': data_base.get_songs_year(year),
        'artists': data_base.get_artists_year(year),
        'genres': data_base.get_genres_year(year)
    }
    return year
#####################################


########### Genres ##################
def get_genres_info(start, step, content):
    genres = {}

    if content['type'] == 'songs':
        genres = data_base.get_genres_info_by_song(start, step)
    elif content['type'] == 'artists':
        genres = data_base.get_genres_info_by_artist(start, step)
    return genres


def get_all_genres_navigation(page, content):
    step = 51
    start = step * (page - 1)
    artists = get_genres_info(start, step, content)
    return artists


def get_genres_info_by_song(page):
    content = {'type': 'songs'}
    genres = get_all_genres_navigation(page, content)
    return genres


def get_genres_info_by_artist(page):
    content = {'type': 'artists'}
    genres = get_all_genres_navigation(page, content)
    return genres


######## Genre count ###############
def get_all_genres_count():
    all_count_genre = data_base.get_count_genre()
    return all_count_genre


########### Genre ##################
def get_genre_info(id_genre):
    genre = data_base.get_genre(id_genre)
    genre['songs'] = data_base.get_songs_genre(id_genre)
    genre['artists'] = data_base.get_artists_genre(id_genre)
    genre['years'] = data_base.get_years_genre(id_genre)
    genre['count'] = data_base.get_count_current_genre(id_genre)
    return genre
#####################################


if __name__ == '__main__':
    print(get_songs_info([1, 2]))
