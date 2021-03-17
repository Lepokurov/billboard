from sql_constructor_general import get_ids_by_request
from sql_request_songs import sql_request_songs_artist_ids


def sql_request_artists_list() -> str:
    """
    Request for list artists
    :return: The request that included the columns and tables for necessary information about artists
    """
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.age_artist, artist.image_artist, artist.group_artist,
     COUNT(artist.id_artist) AS songs
    FROM artist
      LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist) 
        LEFT JOIN song ON (song_performers.id_song = song.id_song)"""
    return sql_request


def sql_constructor_artists(id_artists: list, order) -> str:
    """
    Constructor of the sql request of a artist list
    :param id_artists: list required ids of artists
    :param order: request information of 'order by'
    :return: complete request for getting data of the artist list
    """
    sql_request = sql_request_artists_list()
    sql_request += ' WHERE artist.id_artist =0'
    if not id_artists:
        return ""
    for id_artist in id_artists:
        sql_request += ' or artist.id_artist=' + str(id_artist)
    sql_request += ' GROUP BY artist.id_artist '
    sql_request += order
    return sql_request


def __get_columns(count: bool) -> str:
    """
    getting columns: ids or count rows
    :param count: if need count then changed request
    :return: columns
    """
    if not count:
        columns = 'COUNT(*)'
    else:
        columns = 'artist.id_artist'
    return columns


def sql_request_artists_by_name(name: str, count=False) -> str:
    """
    Request to get ids of artists by name
    :param name: name artist
    :param count: if need count then changed request
    :return: str request
    """

    sql_request = "SELECT " + __get_columns(count) + " FROM artists "
    sql_request += "WHERE POSITION('" + name + "' in LOWER(name_artist))>0"
    return sql_request


def sql_request_artists_by_song(song: str, count=False) -> str:
    """
    Request to get ids of artists by title performed songs
    :param song: title of song
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT ' + __get_columns(count)
    sql_request += """ FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist) """
    sql_request += "WHERE POSITION('" + song + "' in LOWER(title_song))>0"

    return sql_request


def sql_request_artists_by_genre(genre: str, count=False) -> str:
    """
    Request to get ids of artists by genre artist
    :param genre: name of genre
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT' + __get_columns(count)
    sql_request += """FROM genre 
     LEFT JOIN artist_genre ON (artist_genre.id_genre = genre.id_genre)
      LEFT JOIN artist ON (artist_genre.id_artist = artist.id_artist)"""
    sql_request += "WHERE POSITION('" + genre + "' in LOWER(name_genre))>0"

    return sql_request


def sql_request_artists_dead(count=False) -> str:
    """
    Request to get ids of dead artists
    :param count: if need count then changed request
    :return: str request
    """
    sql_request = 'SELECT ' + __get_columns(count)
    sql_request += "FROM artist WHERE (POSITION('-' in age_artist)>0) and (select length(age_artist))<4"
    return sql_request


def sql_request_artist(id_artist) -> str:
    """
    Request to get all info by current artist id
    :param id_artist: id of a artist
    :return: request
    """
    sql_request = "SELECT * from artist where id_artist =" + str(id_artist)
    return sql_request


def sql_request_featuring_artists(id_artist) -> str:
    """
    Complex request
    At first it here need to get ids of songs by artist and then construct request
    :param id_artist: id of artist
    :return: str request
    """
    id_songs = get_ids_by_request(sql_request_songs_artist_ids(id_artist))
    sql_request = """ SELECT artist.id_artist, artist.name_artist, artist.image_artist
        FROM song
          LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
            LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
        WHERE not artist.id_artist = """ + str(id_artist)
    sql_request += ' and (song.id_song = 0'
    for id_song in id_songs:
        sql_request += ' or song.id_song =' + str(id_song)
    sql_request += ') GROUP BY artist.id_artist '
    return sql_request


def sql_request_performers_of_song(id_song) -> str:
    """
    request to get all performer's artists of song by song id
    :param id_song:
    :return: request
    """
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist
    FROM song
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
    WHERE song.id_song =""" + str(id_song)
    return sql_request


def sql_request_artists_year(year) -> str:
    """
    request to get all performer's artists of songs by billboard year
    :param year: billboard year
    :return: request
    """
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist, COUNT(artist.id_artist) AS counts
    FROM artist
      LEFT JOIN song_performers ON (song_performers.id_artist = artist.id_artist) 
        LEFT JOIN song ON (song_performers.id_song = song.id_song)
         LEFT JOIN billboard ON (billboard.id_song = song.id_song)"""

    sql_request += "WHERE billboard.year ='" + str(year) + "'"
    sql_request += "GROUP BY artist.id_artist 	order by counts desc"
    return sql_request


def sql_request_artists_genre(id_genre, limit) -> str:
    """
    request to get all artist by the genre
    :param id_genre: id of genre
    :param limit: limit of genres
    :return: sql request
    """
    sql_request = """
    SELECT artist.id_artist, artist.name_artist, artist.image_artist
    FROM artist
      LEFT JOIN artist_genre ON (artist_genre.id_artist = artist.id_artist) 
       LEFT JOIN genre ON (artist_genre.id_genre = genre.id_genre)
    WHERE genre.id_genre =""" + str(id_genre)
    if limit:
        sql_request += ' LIMIT ' + str(limit)
    return sql_request
