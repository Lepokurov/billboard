from Artist import Artist
from factory import Factory
factory = Factory()


def get_artists(type_: str, value_: str, page: int, step: int):
    """
    get Artist element with list attr
    :param type_: required type
    :param value_: required value
    :param page: number of page
    :param step: count of elements
    :return: Artist class with list attr
    """
    artist = factory.get_elem_list(Artist, type_, value_, page, step)
    prepare_artist_info_to_show(artist)
    return artist


def get_artist(id_artist):
    """
    get Artist element with attrs
    :param id_artist: id of artist
    :return: element class with attrs
    """
    artist = factory.get_elem_solo(Artist, id_artist)
    age_info_artist(artist)
    return artist


def count_artists(type_: str, value_=''):
    """
    get count artist by type and value
    :param type_: required type
    :param value_: required value
    :return: count artist
    """
    count = factory.get_elem_count(Artist, type_, value_)
    return count


def prepare_artist_info_to_show(artists):
    # that is different because i am not smart sometimes)))
    for artist in artists.list:
        if artist['group'] == 'True':
            artist['age'] = 'The group'
        elif int(artist['age']) < 0:
            artist['age'] = str(artist['age'])[1:] + ' years (Dead)'
        else:
            artist['age'] = str(artist['age']) + ' years'


def age_info_artist(artist):
    # that is different because i am not smart sometimes)))
    if artist.group == 'True':
        artist.age = 'The group'
    elif int(artist.age) < 0:
        artist.age = str(artist.age)[1:] + ' years (Dead)'
    else:
        artist.age = str(artist.age) + ' years'
