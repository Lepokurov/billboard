from Song import Song
from artists_for_description import get_performers_of_song
from generel_tool import add_to_class
from genres_for_description import get_genres_song
from songs_for_description import get_song, get_songs_artist
from years_for_description import get_billboard_of_song


def song_information(song: Song, content: dict):
    if content['page'] == 'solo':
        __song_solo_page(song)


def __song_solo_page(song: Song):
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
