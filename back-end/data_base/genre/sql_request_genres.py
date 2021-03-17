from sql_constructor_general import limit_information


def sql_request_genres(sort) -> str:
    """
    Request to get genre list
    :param sort: genre sorting by 'sort', the default sorting is by song
    :return: sql request
    """
    sql_request = ''
    if sort == 'song':
        sql_request = """
        SELECT genre.id_genre, genre.name_genre, genre.image_genre, COUNT(genre.id_genre) AS counts
        FROM genre 
         LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
        GROUP BY genre.id_genre"""
    elif sort == 'artist':
        sql_request = """
        SELECT genre.id_genre, genre.name_genre, genre.image_genre, COUNT(genre.id_genre) AS counts
        FROM genre 
         LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre) 
        GROUP BY genre.id_genre"""

    return sql_request


def sql_constructor_genres(start, step, sort) -> str:
    """
    Constructor of the sql request of a genre list
    :param start: the start row
    :param step: number of rows
    :param sort: genre sorting by 'sort', the default sorting is by song
    :return: complete request for genre list data
    """
    sql_request = sql_request_genres(sort)
    sql_request += ' order by counts DESC '
    sql_request = limit_information(sql_request, start, step)

    return sql_request


def sql_request_genre(id_genre) -> str:
    """
    Request to get all info by current song id
    :param id_genre: id of a song
    :return: request
    """
    sql_request = "SELECT * from genre where id_genre =" + str(id_genre)
    return sql_request


def sql_request_genres_year(year) -> str:
    """
    request to get all genres of songs by billboard year
    :param year: billboard year
    :return: request
    """
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre,  COUNT(genre.id_genre) AS counts
    FROM genre
      LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
        LEFT JOIN song ON (song_genre.id_song = song.id_song) 
        LEFT JOIN billboard ON (billboard.id_song = song.id_song)"""

    sql_request += "WHERE billboard.year ='" + str(year) + "'"
    sql_request += "GROUP BY genre.id_genre	order by counts desc"
    return sql_request


def sql_request_genres_artist(id_artist) -> str:
    """
    request to get all genres of artist by id of artist
    :param id_artist: id of artist
    :return: request
    """
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre
    FROM artist
      LEFT JOIN artist_genre ON (artist_genre.id_artist = artist.id_artist) 
        LEFT JOIN genre ON (artist_genre.id_genre = genre.id_genre)
    WHERE artist.id_artist =""" + id_artist
    return sql_request


def sql_request_genres_song(id_song) -> str:
    """
    request to get all genres of song by id of song
    :param id_song: id of song
    :return: request
    """
    sql_request = """
    SELECT genre.id_genre, genre.name_genre, genre.image_genre
    FROM song 
    LEFT JOIN song_genre ON (song_genre.id_song = song.id_song)
      LEFT JOIN genre ON (song_genre.id_genre = genre.id_genre)
    WHERE song.id_song =""" + str(id_song)
    return sql_request


def sql_request_count_songs_genre(id_genre) -> str:
    """
    request to get count songs by current genre
    :param id_genre: id of genre
    :return: request
    """
    sql_request = """
    SELECT COUNT(genre.id_genre) AS counts FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
      LEFT JOIN song ON (song_genre.id_song = song.id_song) 
    WHERE genre.id_genre =""" + str(id_genre)
    return sql_request


def sql_request_count_artists_genre(id_genre) -> str:
    """
    request to get count artists by current genre
    :param id_genre: id of genre
    :return: request
    """
    sql_request = """
    SELECT COUNT(genre.id_genre) AS counts FROM genre 
     LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre) 
      LEFT JOIN artist ON (artist_genre.id_artist = artist.id_artist) 
    WHERE genre.id_genre =""" + str(id_genre)
    return sql_request
