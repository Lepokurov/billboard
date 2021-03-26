from Song import Song
from artists_for_description import get_performers_of_song
from generel_tool import add_to_class
from genres_for_description import get_genres_song
from songs_count import get_count_songs
from songs_for_description import get_song, get_songs_artist
from songs_list import get_songs_all
from songs_search import search_songs
from years_for_description import get_billboard_of_song


def song_information(song: Song, content: dict):
    """
    change song class with required attr by content
    :param song: Song class
    :param content: dictionary that contain the type and value of searching
    """
    if content['page'] == 'solo':
        __song_solo_page(song)
    elif content['page'] == 'list':
        __song_list_page(song, content)
    elif content['page'] == 'count':
        __get_count_songs_list(song, content)


def __song_solo_page(song: Song):
    """
    add attrs to song elem for solo page showing
    :param song: Song class
    """
    id_song = song.id
    song_ = get_song(id_song)
    artists = get_performers_of_song(id_song)
    for artist in artists:
        id_artist = artist['id']
        artist['other_songs'] = get_songs_artist(id_artist, str(id_song), 7)
    song_['artists'] = artists
    song_['genres'] = get_genres_song(id_song)
    song_['billboard'] = get_billboard_of_song(id_song)
    add_to_class(song, song_)


def __song_list_page(song: Song, content: dict):
    """
    add attrs to song elem for list page showing
    :param song: Song class
    :param content: dictionary that contain the type and value of searching
    """
    start = song.id
    step = song.step
    if content['type'] == 'all':
        songs = get_songs_all(start, step)
    else:
        songs = search_songs(content, start, step)
    song.list = songs
    del song.step
    del song.id


def __get_count_songs_list(song: Song, content: dict):
    """
    add count attr to song elem
    :param song: Song class
    :param content: dictionary that contain the type and value of searching
    """
    song.count = get_count_songs(content)
