
def sql_request_songs_list() -> str:
    """
    Request for list songs
    :return: The request that included the columns and tables for necessary information about songs
    """
    sql_request = """SELECT song.id_song, song.title_song, song.album_song, song.image_song, artist.name_artist,
    billboard.year, billboard.position
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
          LEFT JOIN billboard ON (billboard.id_song = song.id_song)"""
    return sql_request


def __get_columns(count: bool) -> str:
    """
    getting columns: ids or count rows
    :param count: if need count then changed request
    :return:
    """
    if not count:
        columns = 'COUNT(*)'
    else:
        columns = 'song.id_song'
    return columns


def sql_request_songs_by_title(title: str, count=False) -> str:
    """
    Request to get ids of songs by title
    :param title: title of songs
    :param count: if need count then changed request
    :return: str request
    """

    sql_request = "SELECT " + __get_columns(count) + " FROM song "
    sql_request += "WHERE POSITION('" + title + "' in LOWER(title_song))>0"
    return sql_request


def sql_request_songs_by_genre(genre: str, count=False) -> str:
    """
    Request to get ids of songs by genre song
    :param genre: name of genre
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT' + __get_columns(count)
    sql_request += """FROM genre 
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre)
      LEFT JOIN song ON (song_genre.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0 and song.id_song is not null"

    return sql_request


def sql_request_songs_by_year(year: str, count=False) -> str:
    """
    Request to get ids of songs by year's of getting at billboard
    :param year: year
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT' + __get_columns(count)
    sql_request += """FROM song
         LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE billboard.year ='""" + str(year) + "'"

    return sql_request


def sql_request_songs_by_artist(artist: str, count=False) -> str:
    """
    Request to get ids of songs by performer artist name
    :param artist: name of artist
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT' + __get_columns(count)
    sql_request += """FROM artist
     LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist)
      LEFT JOIN song ON (song_performers.id_song = song.id_song)"""
    sql_request += "WHERE POSITION('" + artist + "' in LOWER(name_artist))>0"

    return sql_request


def sql_request_songs_hit_several_times(count=False) -> str:
    """
    Request to get ids of songs that hit billboard several times
    :param count: if need count then changed request
    :return: str request
    """
    'SLOWLY WORK, NEED REWRITE IT'
    sql_request = 'SELECT' + __get_columns(count)
    sql_request += """FROM song
            WHERE EXISTS (SELECT NULL
              FROM billboard c
              WHERE c.id_song = song.id_song
              GROUP BY c.id_song
              HAVING COUNT(*) > 1 ) """

    return sql_request


def sql_request_song(id_song) -> str:
    """
    Request to get all info by current song id
    :param id_song: id of a song
    :return: request
    """
    sql_request = "SELECT * from song where id_song =" + str(id_song)
    return sql_request


def sql_request_songs_artist(id_artist, id_song_pass, limit) -> str:
    """
    Get request to get artist's song list
    :param id_artist: id of artist
    :param id_song_pass: id song to skip
    :param limit: limit songs
    :return: str request
    """
    sql_request = sql_request_songs_list()
    sql_request += 'WHERE artist.id_artist =' + str(id_artist)
    sql_request += 'and not song.id_song =' + str(id_song_pass) + ' order by song.id_song'
    if limit:
        sql_request += 'LIMIT ' + str(limit)
    return sql_request


def sql_request_songs_year(year) -> str:
    """
    Get request to get year's song list
    :param year: year
    :return: str request
    """
    sql_request = """
       SELECT song.id_song, song.title_song, song.released_song ,song.image_song, billboard.position
       FROM song
          LEFT JOIN billboard ON (billboard.id_song = song.id_song)
       WHERE billboard.year =  '""" + str(year) + "' order by billboard.position "
    return sql_request


def sql_request_songs_genre(id_genre, limit) -> str:
    """
    Get request to get genre's song list
    :param id_genre: id of genre
    :param limit: limit songs
    :return: str request
    """
    sql_request = """
        SELECT song.id_song, song.title_song, song.released_song ,song.image_song
        FROM song
         LEFT JOIN song_genre ON (song_genre.id_song = song.id_song) 
          LEFT JOIN genre ON (song_genre.id_genre = genre.id_genre)
             WHERE genre.id_genre = """ + str(id_genre)
    sql_request += ' order by song.id_song'
    if limit:
        sql_request += ' LIMIT ' + str(limit)
    return sql_request


def sql_request_songs_artist_ids(id_artist) -> str:
    """
    Part of complex request
    request to get ids songs of artist
    :param id_artist: id of artist
    :return: request
    """
    sql_request = """SELECT song_performers.id_song
    FROM artist
        LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist)
    WHERE artist.id_artist =""" + str(id_artist)
    return sql_request
