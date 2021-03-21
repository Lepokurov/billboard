import math

import controller

from flask import Flask, render_template, redirect, url_for, request

from song_controller import get_songs, count_songs

app = Flask(__name__)

# calculates once to increase speed
max_count = 0
title_page = ''


def get_count_of_page(count_elem):
    max_page = max_count / count_elem
    max_page = math.ceil(max_page)
    return max_page


########### SONGS ##################
@app.route('/', methods=["GET"])
def index():
    songs = controller.get_random_index_songs()
    return render_template('index.html', songs=songs)


@app.route('/songs/<type_>/<value_>/<page>', methods=["GET"])
def songs_show(page, type_, value_):
    global max_count, title_page
    songs_elem = 51
    page = int(page)
    songs = get_songs(type_, value_, page, songs_elem)
    max_page = get_count_of_page(songs_elem)
    return render_template('songs.html', songs=songs, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page)


@app.route('/songs_default', methods=["GET"])
def songs_default():
    global max_count, title_page
    type_ = 'all'
    max_count = count_songs(type_)
    title_page = 'All songs : ' + str(max_count)
    return redirect(url_for('songs_show', page=1, type_=type_, value_='_'))


@app.route('/songs_by_year', methods=["POST"])
def songs_by_year():
    global max_count, title_page
    year = request.form['year']
    type_ = 'by_year'
    max_count = count_songs(type_, year)
    title_page = 'Songs of ' + year + ' year: ' + str(max_count)
    return redirect(url_for('songs_show', page=1, type_=type_, value_=year))


@app.route('/songs_by_artist', methods=["POST"])
def songs_by_artist():
    global max_count, title_page
    artist = request.form['artist'].lower()
    type_ = 'by_artist'
    max_count = count_songs(type_, artist)
    title_page = 'Songs of ' + request.form['artist'] + ' artist: ' + str(max_count)
    return redirect(url_for('songs_show', page=1, type_=type_, value_=artist))


@app.route('/songs_by_title', methods=["POST"])
def songs_by_title():
    global max_count, title_page
    title = request.form['title'].lower()
    type_ = 'by_title'
    max_count = count_songs(type_, title)
    title_page = 'Songs ' + request.form['title'] + ' title: ' + str(max_count)
    return redirect(url_for('songs_show', page=1,  type_=type_, value_=title))


@app.route('/songs_by_genre', methods=["POST"])
def songs_by_genre():
    global max_count, title_page
    genre = request.form['genre'].lower()
    type_ = 'by_genre'
    max_count = count_songs(type_, genre)
    title_page = 'Songs ' + request.form['genre'] + ' genre: ' + str(max_count)
    return redirect(url_for('songs_show', page=1, type_=type_, value_=genre))


@app.route('/songs_hit_several_times', methods=["POST"])
def hit_several_times():
    global max_count, title_page
    type_ = 'hit_several_times'
    max_count = count_songs(type_)
    title_page = 'Songs hit billboard several times: ' + str(max_count)

    return redirect(url_for('songs_show', page=1, type_=type_, value_='_'))


#####################################


########### Artists ##################


@app.route('/artists/<content>/<page>', methods=["GET"])
def artists_show(page, content):
    global max_count, title_page
    page = int(page)
    artists = {}
    if content == 'default':
        artists = controller.get_all_artists(page)

    elif 'name' in content:
        name = content[4:]
        artists = controller.get_all_artists_by_name(page, name)

    elif 'song' in content:
        song = content[4:]
        artists = controller.get_all_artists_by_song(page, song)

    elif 'genre' in content:
        genre = content[5:]
        artists = controller.get_all_artists_by_genre(page, genre)

    elif 'artists_dead' == content:
        artists = controller.get_all_artists_dead(page)

    max_page = max_count / 51
    max_page = math.ceil(max_page)
    return render_template('artists.html', artists=artists, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page)


@app.route('/artists_default', methods=["GET"])
def artists_default():
    global max_count, title_page
    max_count = controller.get_all_artists_count()
    title_page = 'Artists : ' + str(max_count)
    content = 'default'
    return redirect(url_for('artists_show', page=1, content=content))


@app.route('/artist_by_name', methods=["POST"])
def artist_by_name():
    global max_count, title_page
    name = request.form['name']
    content = 'name' + name.lower()
    max_count = controller.get_all_artists_count_by_name(name.lower())
    title_page = 'Artists ' + name + ' name: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, content=content))


@app.route('/artist_by_song', methods=["POST"])
def artist_by_song():
    global max_count, title_page
    song = request.form['song']
    content = 'song' + song.lower()
    max_count = controller.get_all_artists_count_by_song(song.lower())
    title_page = 'Artists ' + song + ' song: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, content=content))


@app.route('/artist_by_genre', methods=["POST"])
def artist_by_genre():
    global max_count, title_page
    genre = request.form['genre']
    content = 'genre' + genre.lower()
    max_count = controller.get_all_artists_count_by_genre(genre.lower())
    title_page = 'Artists ' + genre + ' genre: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, content=content))


@app.route('/artist_dead', methods=["POST"])
def artists_dead():
    global max_count, title_page
    max_count = controller.get_all_artists_count_dead()
    title_page = 'Dead artists: ' + str(max_count)
    content = 'artists_dead'
    return redirect(url_for('artists_show', page=1, content=content))


#####################################


############# Years ##################
@app.route('/years/<content>/<page>', methods=["GET"])
def years_show(page, content):
    global max_count, title_page
    page = int(page)
    years = {}

    if content == 'default':
        years = controller.get_all_years(page)

    elif 'search' in content:
        year = content[6:]
        years = controller.get_all_years_search(page, year)

    max_page = max_count / 21
    max_page = math.ceil(max_page)
    return render_template('years.html', years=years, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page)


@app.route('/year_default', methods=["GET"])
def year_default():
    global max_count, title_page
    max_count = controller.get_all_years_count()
    title_page = 'Years : ' + str(max_count)
    content = 'default'
    return redirect(url_for('years_show', page=1, content=content))


@app.route('/year_search', methods=["POST"])
def year_search():
    global max_count, title_page
    search = request.form['search']
    content = 'search' + search.lower()
    max_count = controller.get_all_years_count_search(search.lower())
    title_page = 'Search ' + search + ' in years: ' + str(max_count)
    return redirect(url_for('years_show', page=1, content=content))


#####################################


########### Genres ##################
@app.route('/genres/<content>/<page>', methods=["GET"])
def genres_show(page, content):
    global max_count, title_page
    page = int(page)
    genres = {}

    if content == 'songs':
        genres = controller.get_genres_info_by_song(page)
    elif content == 'artists':
        genres = controller.get_genres_info_by_artist(page)

    max_page = max_count / 51
    max_page = math.ceil(max_page)
    return render_template('genres.html', genres=genres, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page, content=content)


@app.route('/genres_default', methods=["GET"])
def genres_default():
    global max_count
    max_count = controller.get_all_genres_count()
    # Default genres page is sorted by songs
    return redirect(url_for('genres_songs'))


@app.route('/genres_songs', methods=["GET", "POST"])
def genres_songs():
    global title_page
    title_page = 'Genres : ' + str(max_count) + 'order by songs'
    content = 'songs'
    return redirect(url_for('genres_show', page=1, content=content))


@app.route('/genres_artists', methods=["GET", "POST"])
def genres_artists():
    global title_page
    title_page = 'Genres : ' + str(max_count) + 'order by artists'
    content = 'artists'
    return redirect(url_for('genres_show', page=1, content=content))


#########################################


############ Solo pages #################
@app.route('/song_show/<id_song>', methods=["GET"])
def song_show(id_song):
    song = controller.get_song_info(str(id_song))
    return render_template('song.html', song=song)


@app.route('/artist_show/<id_artist>', methods=["GET"])
def artist_show(id_artist):
    artist = controller.get_artist_info(str(id_artist))
    return render_template('artist.html', artist=artist)


@app.route('/year_show/<year>', methods=["GET"])
def year_show(year):
    year_info = controller.get_year_info(year)
    return render_template('year.html', year=year_info, current_year=year)


@app.route('/genre_show/<id_genre>', methods=["GET"])
def genre_show(id_genre):
    genre = controller.get_genre_info(id_genre)
    return render_template('genre.html', genre=genre)
