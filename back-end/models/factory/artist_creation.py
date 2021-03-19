from Artist import Artist
from artists_for_description import get_artist, get_featuring_artists
from generel_tool import add_to_class
from genres_for_description import get_genres_artist
from songs_for_description import get_songs_artist
from years_list import get_years_list


def artist_information(artist: Artist, content: dict):
    if content['page'] == 'solo':
        __artist_solo_page(artist)


def __artist_solo_page(artist: Artist):
    id_artist = artist.id
    artist_ = get_artist(id_artist)

    artist_['genres'] = get_genres_artist(id_artist)
    artist_['songs'] = get_songs_artist(id_artist)
    years = []
    for song in artist_['songs']:
        for billboard in song['billboard'].values():
            years.append(billboard['year'])
    artist_['feats'] = get_featuring_artists(id_artist)
    artist_['years'] = get_years_list(years)
    add_to_class(artist, artist_)
