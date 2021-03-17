from Artist import Artist
from Genre import Genre
from Song import Song
from artists_for_description import get_performers_of_song
from general_creation import create_list_general
from genres_for_description import get_genres_song
from songs_for_description import get_song


def create_song_all_information(id_song) -> Song:
    song_data = get_song(id_song)
    # tuple is 1 row
    song_data = song_data[0]
    song = Song(song_data[0], song_data[1], song_data[5])
    song.released = song_data[2]
    song.length = song_data[3]
    song.album = song_data[4]
    song.wiki_link = song_data[6]
    song.youtube_link = song_data[7]

    song.genres = create_list_general(get_genres_song(id_song), Genre)
    song.artists = create_list_general(get_performers_of_song(id_song), Artist)

    return song


def songs_artist(id_artist, limit=0) -> list:
    song_list = []
    return song_list


a = create_song_all_information(1)
b =1