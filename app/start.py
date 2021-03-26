import math

from flask import Flask, render_template, redirect, url_for, request

from artist_controller import get_artists, count_artists, get_artist
from genre_controller import count_genres, get_genres, get_genre
from song_controller import get_songs, count_songs, get_song
from year_controller import get_years, count_years, get_year

app = Flask(__name__)

# calculates once to increase speed
max_count = 0
title_page = ''


def get_count_of_page(count_elem):
    max_page = max_count / count_elem
    max_page = math.ceil(max_page)
    return max_page


# SONGS
@app.route('/', methods=["GET"])
def index():
    return redirect(url_for('year_default'))


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


# ARTISTS
@app.route('/artists/<type_>/<value_>/<page>', methods=["GET"])
def artists_show(page, type_, value_):
    global max_count, title_page
    artists_elem = 51
    page = int(page)
    artists = get_artists(type_, value_, page, artists_elem)
    max_page = get_count_of_page(artists_elem)
    return render_template('artists.html', artists=artists, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page)


@app.route('/artists_default', methods=["GET"])
def artists_default():
    global max_count, title_page
    type_ = 'all'
    max_count = count_artists(type_)
    title_page = 'Artists: ' + str(max_count)

    return redirect(url_for('artists_show', page=1, type_=type_, value_='_'))


@app.route('/artist_by_name', methods=["POST"])
def artist_by_name():
    global max_count, title_page
    name = request.form['name'].lower()
    type_ = 'by_name'
    max_count = count_artists(type_, name)
    title_page = 'Artists by ' + request.form['name'] + ' name: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, type_=type_, value_=name))


@app.route('/artist_by_song', methods=["POST"])
def artist_by_song():
    global max_count, title_page
    song = request.form['song'].lower()
    type_ = 'by_song'
    max_count = count_artists(type_, song)
    title_page = 'Artists by ' + request.form['song'] + ' song: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, type_=type_, value_=song))


@app.route('/artist_by_genre', methods=["POST"])
def artist_by_genre():
    global max_count, title_page
    genre = request.form['genre'].lower()
    type_ = 'by_genre'
    max_count = count_artists(type_, genre)
    title_page = 'Artists by ' + request.form['genre'] + ' genre: ' + str(max_count)
    return redirect(url_for('artists_show', page=1, type_=type_, value_=genre))


@app.route('/artist_dead', methods=["POST"])
def artists_dead():
    global max_count, title_page
    type_ = 'dead'
    max_count = count_artists(type_)
    title_page = 'Dead artists: ' + str(max_count)

    return redirect(url_for('artists_show', page=1, type_=type_, value_='_'))
#####################################


# YEARS
@app.route('/years/<type_>/<value_>/<page>', methods=["GET"])
def years_show(page, type_, value_):
    global max_count, title_page
    years_elem = 21
    page = int(page)
    years = get_years(type_, value_, page, years_elem)
    max_page = get_count_of_page(years_elem)
    return render_template('years.html', years=years, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page)


@app.route('/year_default', methods=["GET"])
def year_default():
    global max_count, title_page
    type_ = 'all'
    max_count = count_years(type_)
    title_page = 'Years: ' + str(max_count)

    return redirect(url_for('years_show', page=1, type_=type_, value_='_'))


@app.route('/year_search', methods=["POST"])
def year_search():
    global max_count, title_page
    search = request.form['search']
    type_ = 'search'
    max_count = count_years(type_, search)
    title_page = 'Years of ' + search + ': ' + str(max_count)
    return redirect(url_for('years_show', page=1, type_=type_, value_=search))
#####################################


# GENRES
@app.route('/genres/<type_>/<value_>/<page>', methods=["GET"])
def genres_show(page, type_, value_):
    global max_count, title_page
    years_elem = 51
    page = int(page)
    genres = get_genres(type_, value_, page, years_elem)
    max_page = get_count_of_page(years_elem)
    return render_template('genres.html', genres=genres, max_page=max_page, page=page, next_page=page + 1,
                           previous_page=page - 1, title_page=title_page, content=type_)


@app.route('/genres_default', methods=["GET"])
def genres_default():
    # Default genres page is sorted by songs
    return redirect(url_for('genres_by_songs'))


@app.route('/genres_by_songs', methods=["GET", "POST"])
def genres_by_songs():
    global max_count, title_page
    type_ = 'by_song'
    max_count = count_genres(type_)
    title_page = 'Genres : ' + str(max_count) + 'order by songs'

    return redirect(url_for('genres_show', page=1, type_=type_, value_='_'))


@app.route('/genres_by_artists', methods=["GET", "POST"])
def genres_by_artists():
    global max_count, title_page
    type_ = 'by_artist'
    max_count = count_genres(type_)
    title_page = 'Genres : ' + str(max_count) + 'order by songs'

    return redirect(url_for('genres_show', page=1, type_=type_, value_='_'))


@app.route('/genres_search', methods=["POST"])
def genres_search():
    global max_count, title_page
    search = request.form['search']
    type_ = 'search'
    max_count = count_genres(type_, search)
    title_page = 'Genres of ' + search + ': ' + str(max_count)
    return redirect(url_for('genres_show', page=1, type_=type_, value_=search))
#####################################


# SOLO PAGES
@app.route('/song_show/<id_song>', methods=["GET"])
def song_show(id_song):
    song = get_song(id_song)
    return render_template('song.html', song=song)


@app.route('/artist_show/<id_artist>', methods=["GET"])
def artist_show(id_artist):
    artist = get_artist(id_artist)
    return render_template('artist.html', artist=artist)


@app.route('/year_show/<year_>', methods=["GET"])
def year_show(year_):
    year = get_year(year_)
    return render_template('year.html', year=year, current_year=year_)


@app.route('/genre_show/<id_genre>', methods=["GET"])
def genre_show(id_genre):
    genre = get_genre(id_genre)
    return render_template('genre.html', genre=genre)
