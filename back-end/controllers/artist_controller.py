from Artist import Artist
from factory import Factory
factory = Factory()


def get_artists(type_: str, value_: str, page: int, step: int):
    artist = factory.get_elem_list(Artist, type_, value_, page, step)
    prepare_artist_info_to_show(artist)
    return artist


def get_artist(id_song):
    artist = factory.get_elem_solo(Artist, id_song)
    age_info_artist(artist)
    return artist


def count_artists(type_: str, value_=''):
    count = factory.get_elem_count(Artist, type_, value_)
    return count


def prepare_artist_info_to_show(artists):
    for artist in artists.list:
        if artist['group'] == 'True':
            artist['age'] = 'The group'
        elif int(artist['age']) < 0:
            artist['age'] = str(artist['age'])[1:] + ' years (Dead)'
        else:
            artist['age'] = str(artist['age']) + ' years'


def age_info_artist(artist):
    if artist.group == 'True':
        artist.age = 'The group'
    elif int(artist.age) < 0:
        artist.age = str(artist.age)[1:] + ' years (Dead)'
    else:
        artist.age = str(artist.age) + ' years'

