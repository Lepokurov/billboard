def create_content(page_: str, type_='', value_='') -> dict:
    """
    Important part, dict with tags of require content
    :param page_: solo or list page require
    :param type_: get information of the song or artist by the type (all, by_song, by_title...)
    :param value_: value
    :return: content dict or raise the type error if given wrong params
    """
    if not (page_ == 'solo' or page_ == 'list' or page_ == 'count'):
        raise TypeError

    if page_ == 'list' and type_ == '':
        type_ = 'all'

    if not (type_ == 'by_name' or type_ == 'by_genre' or type_ == 'by_song'
            or type_ == 'dead' or type_ == 'group' or type_ == 'by_title' or type_ == 'by_year'
            or type_ == 'by_artist' or type_ == 'hit_several_times' or type_ == 'search'
            or type_ == 'all'):
        raise TypeError
    content = {
        'type': type_,
        'value': value_,
        'page': page_
    }
    return content
