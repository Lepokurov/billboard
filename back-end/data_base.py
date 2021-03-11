import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import models


def _connect_to_bd():
    try:
        connection = psycopg2.connect(user="postgres",
                                      database="billboard_data",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection
    except (Exception, Error) as error:
        print("Error of connecting to PostgreSQL", error)
        return error


def _get_data_db(sql_request) -> tuple:
    connection = _connect_to_bd()
    cursor = connection.cursor()
    cursor.execute(sql_request)
    sql_data = cursor.fetchall()
    connection.close()
    return sql_data


########### Songs ##################
def get_songs_info(id_songs: list, order='') -> dict:
    sql_request = """SELECT song.id_song, song.title_song, song.album_song, song.image_song, artist.name_artist,
    billboard.year, billboard.position
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
          LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE song.id_song = 0"""
    if not id_songs:
        return {}
    for id_song in id_songs:
        sql_request += ' or song.id_song =' + str(id_song)
    sql_request += order

    sql_data = _get_data_db(sql_request)
    songs = models.create_songs_info(sql_data)
    return songs


def _get_songs_info_range(sql_request, start, step, order='') -> dict:
    sql_request += ' and song.id_song is not null'
    sql_request += ' LIMIT ' + str(step)
    sql_request += ' OFFSET ' + str(start)
    if order == '':
        order = 'order by billboard.position, artist.id_artist'

    sql_data = _get_data_db(sql_request)
    id_songs = models.create_ids(sql_data)
    songs = get_songs_info(id_songs, order)
    return songs


def get_songs_info_all(start, step) -> dict:
    id_songs = [i for i in range(start, start + step)]
    songs = get_songs_info(id_songs)
    return songs


def get_songs_info_by_title(title, start, step) -> dict:
    sql_request = """SELECT song.id_song FROM song """
    sql_request += "WHERE POSITION('" + title + "' in LOWER(title_song))>0"

    songs = _get_songs_info_range(sql_request, start, step)
    return songs


def get_songs_info_by_genre(genre, start, step) -> dict:
    sql_request = """SELECT song.id_song
    FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre)
     LEFT JOIN song ON (song_genre.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0"

    songs = _get_songs_info_range(sql_request, start, step)
    return songs


def get_songs_info_by_year(year, start, step) -> dict:
    sql_request = """SELECT song.id_song
    FROM song
          LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE billboard.year ='""" + str(year) + "'"
    order = ' order by billboard.position'

    songs = _get_songs_info_range(sql_request, start, step, order)
    return songs


def get_songs_info_by_artist_name(artist_name, start, step) -> dict:
    sql_request = """SELECT song.id_song
    FROM artist
        LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist)
        LEFT JOIN song ON (song_performers.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + artist_name + "' in LOWER(name_artist))>0"
    songs = _get_songs_info_range(sql_request, start, step)
    return songs


def get_songs_info_billboard_more_once(start, step) -> dict:
    sql_request = '''SELECT song.id_song
    FROM song
            WHERE EXISTS (SELECT NULL
              FROM billboard c
              WHERE c.id_song = song.id_song
              GROUP BY c.id_song
              HAVING COUNT(*) > 1 ) '''
    songs = _get_songs_info_range(sql_request, start, step)
    return songs


########### songs count ##################
def get_count_song_by_title(title) -> int:
    sql_request = """SELECT COUNT(*) FROM song """
    sql_request += "WHERE POSITION('" + title + "' in LOWER(title_song))>0 and song.id_song is not null"

    count = _get_count(sql_request)
    return count


def get_count_song_by_artist_name(artist_name) -> int:
    sql_request = """SELECT COUNT(*)
    FROM artist
        LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist)
        LEFT JOIN song ON (song_performers.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + artist_name + "' in LOWER(name_artist))>0"

    count = _get_count(sql_request)
    return count


def get_count_song_by_year(year) -> int:
    sql_request = "SELECT COUNT(*) FROM billboard where billboard.year ='" + str(year) + "'"

    count = _get_count(sql_request)
    return count


def get_count_song_by_genre(genre) -> int:
    sql_request = """SELECT COUNT(*)
    FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre)
      LEFT JOIN song ON (song_genre.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0 and song.id_song is not null"

    count = _get_count(sql_request)
    return count


def get_count_song_billboard_more_once() -> int:
    sql_request = '''SELECT COUNT(*)
    FROM song
            WHERE EXISTS (SELECT NULL
              FROM billboard c
              WHERE c.id_song = song.id_song
              GROUP BY c.id_song
              HAVING COUNT(*) > 1 ) '''

    count = _get_count(sql_request)
    return count


########### Song/songs to artist/year/genre #################
def get_song(id_song):
    sql_request = "SELECT * from song where id_song =" + str(id_song)
    sql_data = _get_data_db(sql_request)
    song = models.create_song(sql_data[0])
    return song


def get_songs_artist(id_artist, id_song_pass=0, limit=0) -> dict:
    sql_request = """
    SELECT song.id_song, song.title_song, song.released_song ,song.image_song, billboard.year, billboard.position
    FROM song
     LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
      LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
       LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE artist.id_artist = """ + str(id_artist) + ' order by song.id_song '
    if limit:
        sql_request += 'LIMIT ' + str(limit)

    sql_data = _get_data_db(sql_request)

    songs = models.create_songs_artist(sql_data, id_song_pass)

    return songs


def get_songs_year(year) -> dict:
    sql_request = """
    SELECT song.id_song, song.title_song, song.released_song ,song.image_song, billboard.position
    FROM song
       LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE billboard.year =  '""" + str(year) + "' order by billboard.position "

    sql_data = _get_data_db(sql_request)

    songs = models.create_songs_year(sql_data)

    return songs


def get_songs_genre(id_genre, limit=0) -> dict:
    sql_request = """
    SELECT song.id_song, song.title_song, song.released_song ,song.image_song
    FROM song
     LEFT JOIN song_genre ON (song_genre.id_song = song.id_song) 
      LEFT JOIN genre ON (song_genre.id_genre = genre.id_genre)
         WHERE genre.id_genre = """ + str(id_genre)
    sql_request += ' order by song.id_song'
    if limit:
        sql_request += ' LIMIT ' + str(limit)

    sql_data = _get_data_db(sql_request)

    songs = models.create_songs_genre(sql_data)

    return songs


#####################################


########### ARTISTS ##################
def get_artists_info(id_artists: list, order='') -> dict:
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.age_artist, artist.image_artist, artist.group_artist,
     COUNT(artist.id_artist) AS songs
    FROM artist
      LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist) 
        LEFT JOIN song ON (song_performers.id_song = song.id_song)
    WHERE artist.id_artist =0"""
    if not id_artists:
        return {}
    for id_artist in id_artists:
        sql_request += ' or artist.id_artist=' + str(id_artist)
    sql_request += ' GROUP BY artist.id_artist '
    sql_request += order

    sql_data = _get_data_db(sql_request)

    artists = models.create_artists_info(sql_data)
    return artists


def _get_artists_info_range(sql_request, start, step, order='') -> dict:
    sql_request += ' and artist.id_artist is not null'
    sql_request += ' LIMIT ' + str(step)
    sql_request += ' OFFSET ' + str(start)

    sql_data = _get_data_db(sql_request)
    id_artists = models.create_ids(sql_data)
    artists = get_artists_info(id_artists, order)
    return artists


def get_artists_info_all(start, step) -> dict:
    id_songs = [i for i in range(start, start + step)]
    order = 'order by artist.id_artist'
    artists = get_artists_info(id_songs, order)
    return artists


def get_artists_info_by_name(name, start, step) -> dict:
    sql_request = """SELECT artist.id_artist FROM artist """
    sql_request += "WHERE POSITION('" + name + "' in LOWER(name_artist))>0"

    artists = _get_artists_info_range(sql_request, start, step)
    return artists


def get_artists_info_by_song(song, start, step) -> dict:
    sql_request = """SELECT artist.id_artist 
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist) """
    sql_request += "WHERE POSITION('" + song + "' in LOWER(title_song))>0"
    order = 'order by artist.id_artist'
    artists = _get_artists_info_range(sql_request, start, step, order)
    return artists


def get_artists_info_by_genre(genre, start, step) -> dict:
    sql_request = """SELECT artist.id_artist
    FROM genre 
     LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre)
      LEFT JOIN artist ON (artist_genre.id_artist = artist.id_artist)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0"
    order = 'order by artist.id_artist'
    artists = _get_artists_info_range(sql_request, start, step, order)
    return artists


def get_artists_info_dead(start, step) -> dict:
    sql_request = """SELECT artist.id_artist
    FROM artist WHERE (POSITION('-' in age_artist)>0) and (select length(age_artist))<4"""
    order = 'order by artist.id_artist'
    artists = _get_artists_info_range(sql_request, start, step, order)
    return artists


########### artists count #################
def get_count_artist_by_name(name) -> int:
    sql_request = """SELECT COUNT(*) FROM artist """
    sql_request += "WHERE POSITION('" + name + "' in LOWER(name_artist))>0 and artist.id_artist is not null"

    count = _get_count(sql_request)
    return count


def get_count_artist_by_song(song) -> int:
    sql_request = """SELECT count(*)
     FROM song
       LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
         LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist) """
    sql_request += "WHERE POSITION('" + song + "' in LOWER(title_song))>0"

    count = _get_count(sql_request)
    return count


def get_count_artist_by_genre(genre) -> int:
    sql_request = """SELECT  count(*)
        FROM genre 
         LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre)
          LEFT JOIN artist ON (artist_genre.id_artist = artist.id_artist)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0"

    count = _get_count(sql_request)
    return count


def get_count_artist_dead() -> int:
    sql_request = """SELECT count(*)
    FROM artist WHERE (POSITION('-' in age_artist)>0) and (select length(age_artist))<4"""

    count = _get_count(sql_request)
    return count


########### ARTIST/Artists by song/year/genre ##################
def get_artist(id_artist) -> dict:
    sql_request = "SELECT * from artist where id_artist =" + str(id_artist)
    sql_data = _get_data_db(sql_request)
    artist = models.create_artist(sql_data[0])
    return artist


def get_featuring_artists(id_artist) -> dict:
    sql_request_first = """SELECT song_performers.id_song
    FROM artist
        LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist)
    WHERE artist.id_artist =""" + str(id_artist)

    id_songs = _get_data_db(sql_request_first)

    sql_request_second = """ SELECT artist.id_artist, artist.name_artist, artist.image_artist
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
    WHERE song.id_song =0"""
    for id_song in id_songs:
        sql_request_second += ' or song.id_song =' + str(id_song[0])

    sql_data = _get_data_db(sql_request_second)

    artists = models.create_featuring_artists(sql_data, id_artist)
    return artists


def get_performers_song(id_song) -> dict:
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
    WHERE song.id_song =""" + id_song

    sql_data = _get_data_db(sql_request)

    artists = models.create_artists(sql_data)
    return artists


def get_artists_year(year) -> dict:
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist, COUNT(artist.id_artist) AS counts
    FROM artist
      LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist) 
        LEFT JOIN song ON (song_performers.id_song = song.id_song)
         LEFT JOIN billboard ON (billboard.id_song = song.id_song)"""

    sql_request += "WHERE billboard.year ='" + str(year) + "'"
    sql_request += "GROUP BY artist.id_artist 	order by counts desc"

    sql_data = _get_data_db(sql_request)

    artists = models.create_data_year(sql_data)
    return artists


def get_artists_genre(id_genre, limit=0):
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist
    FROM artist
      LEFT JOIN artist_genre ON (artist_genre.id_artist = artist.id_artist) 
       LEFT JOIN genre ON (artist_genre.id_genre = genre.id_genre)
    WHERE genre.id_genre =""" + str(id_genre)
    if limit:
        sql_request += ' LIMIT ' + str(limit)
    sql_data = _get_data_db(sql_request)

    artists = models.create_artists(sql_data)

    return artists


#####################################


############ years  #################
def get_years_info(years_, order='') -> dict:
    sql_request = """
    SELECT  billboard.year, artist.name_artist, song.title_song, song.image_song
    FROM billboard
    LEFT JOIN song ON (billboard.id_song = song.id_song) 
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
    WHERE billboard.position = 1 """

    sql_request += 'and ('
    for year in years_:
        sql_request += " billboard.year = '" + str(year) + "' or"
    sql_request = sql_request[:-2]
    sql_request += ') '
    sql_request += order

    sql_data = _get_data_db(sql_request)

    years = models.create_years_info(sql_data)
    return years


def _get_years_info_range(sql_request, start, step, order='') -> dict:
    # I don't want to do 1 request to catch last billboard year, and i know that is not good at future
    # mb i gonna rewrite that
    last_year = 2020
    start = start - last_year
    sql_request += ' LIMIT ' + str(step)
    sql_request += ' OFFSET ' + str(abs(start))

    sql_data = _get_data_db(sql_request)
    years_ = models.create_ids(sql_data)
    years = get_years_info(years_, order)
    return years


def get_years_info_all(start, step) -> dict:
    years_ = [i for i in range(start, start - step - 1, -1)]
    order = 'order by billboard.year DESC'
    years = get_years_info(years_, order)
    return years


def get_years_info_search(search, start, step) -> dict:
    sql_request = """ SELECT  billboard.year
    FROM billboard
    WHERE billboard.position = 1"""
    sql_request += " and (POSITION('" + str(search) + "' in year) > 0)"

    years = _get_years_info_range(sql_request, start, step)
    return years


def get_billboard_song(id_song) -> dict:
    sql_request = """
        SELECT billboard.year, billboard.position
    FROM song
      LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE song.id_song =""" + id_song

    sql_data = _get_data_db(sql_request)

    billboard_song = models.create_billboard_song(sql_data)
    return billboard_song


def get_years_genre(id_genre) -> dict:
    sql_request = """
    SELECT  billboard.year, COUNT(genre.id_genre) AS counts
    FROM genre
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
      LEFT JOIN billboard ON (billboard.id_song = song_genre.id_song)"""
    sql_request += "WHERE genre.id_genre =" + str(id_genre)
    sql_request += ' GROUP BY billboard.year order by billboard.year desc'

    sql_data = _get_data_db(sql_request)

    years_list = models.create_ids(sql_data)
    years_data = get_years_info(years_list)

    years = models.create_years_genre(sql_data, years_data)
    return years


########## year count ###############
def get_count_year() -> int:
    sql_request = """SELECT count(*) FROM billboard WHERE billboard.position = 1 """

    count = _get_count(sql_request)
    return count


def get_count_year_search(search) -> int:
    sql_request = """SELECT count(*) FROM billboard WHERE billboard.position = 1 """
    sql_request += " and (POSITION('" + str(search) + "' in year) > 0)"

    count = _get_count(sql_request)
    return count


#####################################


##########Genres##################
def get_genres_info(start, step, sql_request) -> dict:
    sql_request += ' order by counts DESC '
    sql_request += 'LIMIT ' + str(step)
    sql_request += ' OFFSET ' + str(start)

    sql_data = _get_data_db(sql_request)

    genres = models.create_genres_info(sql_data)
    return genres


def get_genres_info_by_song(start, step) -> dict:
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre, COUNT(genre.id_genre) AS counts
    FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
    GROUP BY genre.id_genre"""

    genres = get_genres_info(start, step, sql_request)
    return genres


def get_genres_info_by_artist(start, step) -> dict:
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre, COUNT(genre.id_genre) AS counts
    FROM genre 
     LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre) 
    GROUP BY genre.id_genre"""

    genres = get_genres_info(start, step, sql_request)
    return genres


def get_genres_song(id_song) -> dict:
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre
    FROM song 
    LEFT JOIN song_genre ON (song_genre.id_song = song.id_song)
      LEFT JOIN genre ON (song_genre.id_genre = genre.id_genre)
    WHERE song.id_song =""" + id_song

    sql_data = _get_data_db(sql_request)

    genres = models.create_genres(sql_data)
    return genres


########### Genre/genres by song/artist/year ################
def get_genre(id_genre) -> dict:
    sql_request = "SELECT * from genre where id_genre =" + str(id_genre)
    sql_data = _get_data_db(sql_request)
    genre = models.create_genre(sql_data[0])
    return genre


def get_genres_year(year) -> dict:
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre,  COUNT(genre.id_genre) AS counts
    FROM genre
      LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
        LEFT JOIN song ON (song_genre.id_song = song.id_song) 
        LEFT JOIN billboard ON (billboard.id_song = song.id_song)"""

    sql_request += "WHERE billboard.year ='" + str(year) + "'"
    sql_request += "GROUP BY genre.id_genre	order by counts desc"

    sql_data = _get_data_db(sql_request)

    genres = models.create_data_year(sql_data)
    return genres


def get_genres_artist(id_artist) -> dict:
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre
    FROM artist
      LEFT JOIN artist_genre ON (artist_genre.id_artist = artist.id_artist) 
        LEFT JOIN genre ON (artist_genre.id_genre = genre.id_genre)
    WHERE artist.id_artist =""" + id_artist

    sql_data = _get_data_db(sql_request)

    genres = models.create_genres(sql_data)
    return genres


######### genre COUNT ###################
def get_count_current_genre(id_genre):
    sql_request = """
    SELECT COUNT(genre.id_genre) AS counts FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
      LEFT JOIN song ON (song_genre.id_song = song.id_song) 
    WHERE genre.id_genre =""" + str(id_genre)
    song_count = _get_count(sql_request)

    sql_request = """
    SELECT COUNT(genre.id_genre) AS counts FROM genre 
     LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre) 
      LEFT JOIN artist ON (artist_genre.id_artist = artist.id_artist) 
    WHERE genre.id_genre =""" + str(id_genre)
    artist_count = _get_count(sql_request)

    genres_count = models.create_genres_count(song_count, artist_count)
    return genres_count


#####################################


########### COUNTS ##################
def _get_count(sql_request) -> int:
    sql_data = _get_data_db(sql_request)

    return sql_data[0][0]


def _get_count_table(table_name) -> int:
    sql_request = "SELECT COUNT(*) FROM " + table_name

    count = _get_count(sql_request)
    return count


def get_count_song() -> int:
    return _get_count_table('song')


def get_count_artist() -> int:
    return _get_count_table('artist')


def get_count_genre() -> int:
    return _get_count_table('genre')


#####################################
if __name__ == '__main__':
    print(get_artist(2))
    o = 'o'
