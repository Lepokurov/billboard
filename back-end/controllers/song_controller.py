from Song import Song
from general_controller import get_elem_list, get_elem_solo, get_elem_count


def get_songs(type_: str, value_: str, page: int, step: int):
    songs = get_elem_list(Song, type_, value_, page, step)
    prepare_song_info_to_show(songs)
    return songs


def get_song(id_song):
    song = get_elem_solo(Song, id_song)
    return song


def count_songs(type_: str, value_=''):
    count = get_elem_count(Song, type_, value_)
    return count


def prepare_song_info_to_show(songs):
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

get_songs('by_year', '1999', 1, 52)