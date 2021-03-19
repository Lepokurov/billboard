def create_years_list(sql_data: tuple) -> dict:
    """
    Dict of years
    :param sql_data: sql data
    :return: dict of years (keys is years)
    """
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


def create_billboard_of_song(sql_data: tuple) -> list:
    """
    Create year and position list
    :param sql_data: sql data
    :return: list of billboard result
    """
    billboard_song = []
    for sql_line in sql_data:
        billboard_song_ = {
            'year': sql_line[0],
            'position': sql_line[1]
        }
        billboard_song.append(billboard_song_)
    return billboard_song


def create_years_genre(sql_data: tuple, years: dict):
    """
    Create list of years with count of songs.
    Because of that i choose to create year list by the dictionary
    :param sql_data: sql data with only years and count of songs
    :param years: dict data of years
    :return: list
    """
    # MB i need to rewrite that, but this is work well =)
    for sql_line in sql_data:
        year = sql_line[0]
        years[year]['count'] = sql_line[1]
    return years
