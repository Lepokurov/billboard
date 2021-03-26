from Song import Song
from factory import Factory
factory = Factory()


def get_songs(type_: str, value_: str, page: int, step: int):
    """
    get Song element with list attr
    :param type_: required type
    :param value_: required value
    :param page: number of page
    :param step: count of elements
    :return: Song class with list attr
    """
    songs = factory.get_elem_list(Song, type_, value_, page, step)
    prepare_song_info_to_show(songs)
    return songs


def get_song(id_song):
    """
    get Song element with attrs
    :param id_song: id of song
    :return: Song class with attrs
    """
    song = factory.get_elem_solo(Song, id_song)
    return song


def count_songs(type_: str, value_=''):
    """
    get count songs by type and value
    :param type_: required type
    :param value_: required value
    :return: count songs
    """
    count = factory.get_elem_count(Song, type_, value_)
    return count


def prepare_song_info_to_show(songs):
    """
    Change list info for showing
    :param songs:
    """
    for song in songs.list:
        new_title = song['title'].split('(')[0]
        # If name started with (
        if new_title == '':
            new_title = song['title'].split(')')[1]
        if len(new_title) > 30:
            new_title = new_title[:30] + '...'
        song['title'] = new_title

        if len(song['album']) > 30:
            song['album'] = song['album'][:30] + '...'
        # for show only
        year = ''
        position = ''
        for billboard in song['billboard'].values():
            year += billboard['year'] + ', '
            position += str(billboard['position']) + ', '
        song['year'] = year[:-2]
        song['position'] = position[:-2]
