def _sql_request_years_list() -> str:
    """
    Request for list years
    :return: The request that included the columns and tables for necessary information about years
    """
    sql_request = """
    SELECT  billboard.year, artist.name_artist, song.title_song, song.image_song
    FROM billboard
    LEFT JOIN song ON (billboard.id_song = song.id_song) 
      LEFT JOIN song_performers ON (song_performers.id_song = song.id_song) 
        LEFT JOIN artist ON (song_performers.id_artist = artist.id_artist)
    WHERE billboard.position = 1 """
    return sql_request


def _sql_constructor_years(years, order):
    """
    Constructor of the sql request of a year list
    :param years: list required ids of artists
    :param order: request information of 'order by'
    :return: complete request for getting data of the artist list
    """
    sql_request = _sql_request_years_list()
    sql_request += 'and ('
    for year in years:
        sql_request += " billboard.year = '" + str(year) + "' or"
    sql_request = sql_request[:-2]
    sql_request += ') '
    sql_request += order
    return sql_request


def _sql_request_search_years(search_year) -> str:
    """
    Request to get appropriate years
    :param search_year: year
    :return: sql request
    """
    sql_request = """ SELECT  billboard.year
    FROM billboard
    WHERE billboard.position = 1"""
    sql_request += " and (POSITION('" + str(search_year) + "' in year) > 0)"
    return sql_request


def _sql_request_years_all():
    """
    request to get count billboard years
    :return: request
    """
    sql_request = """SELECT count(*) FROM billboard WHERE billboard.position = 1 """
    return sql_request


def _sql_request_years_search(search):
    """
    request to get count billboard years by search year data
    :param search: search year data
    :return: request
    """
    sql_request = _sql_request_years_all()
    sql_request += " and (POSITION('" + str(search) + "' in year) > 0)"
    return sql_request


def _sql_request_billboard_song(id_song):
    """
    request to get billboard year and position of song
    :param id_song: id of song
    :return: request
    """
    sql_request = """
        SELECT billboard.year, billboard.position
    FROM song
      LEFT JOIN billboard ON (billboard.id_song = song.id_song)
    WHERE song.id_song =""" + id_song
    return sql_request


def _sql_request_years_genre(id_genre):
    """
    request to get years that has song with current genre
    :param id_genre: current genre
    :return: years list
    """
    sql_request = """
    SELECT  billboard.year, COUNT(genre.id_genre) AS counts
    FROM genre
     LEFT JOIN song_genre ON (song_genre.id_genre = genre.id_genre) 
      LEFT JOIN billboard ON (billboard.id_song = song_genre.id_song)"""
    sql_request += "WHERE genre.id_genre =" + str(id_genre)
    sql_request += ' GROUP BY billboard.year order by billboard.year desc'
    return sql_request
