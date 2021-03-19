def create_data(sql_data: tuple) -> dict:
    data = {
        'id': sql_data[0],
        'name': sql_data[1],
        'image': sql_data[2],
    }
    return data


def create_data_of_year(sql_data: tuple) -> list:
    """
    It need for description some objects (artists or genres)
    :param sql_data: sql data
    :return: list of objects (artists or genres)
    """
    data = []
    for sql_line in sql_data:
        data_ = create_data(sql_line)
        data_['count'] = sql_line[3]
        data.append(data_)
    return data
