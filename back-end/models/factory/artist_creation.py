from Artist import Artist
from artists_for_description import get_artist, get_featuring_artists
from artists_list import get_artists_all
from artists_search import search_artists
from artsits_count import get_count_artists
from generel_tool import add_to_class
from genres_for_description import get_genres_artist
from songs_for_description import get_songs_artist
from years_list import get_years_list


def artist_information(artist: Artist, content: dict):
    """
    change artist class with required attr by content
    :param artist: Artist class
    :param content: dictionary that contain the type and value of searching
    """
    if content['page'] == 'solo':
        __artist_solo_page(artist)
    elif content['page'] == 'list':
        __artist_list_page(artist, content)
    elif content['page'] == 'count':
        __get_count_artists_list(artist, content)


def __artist_solo_page(artist: Artist):
    """
    add attrs to artist elem for solo page showing
    :param artist: Artist class
    """
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


def __artist_list_page(artist: Artist, content: dict):
    """
    add attrs to artist elem for list page showing
    :param artist: Artist class
    :param content: dictionary that contain the type and value of searching
    """
    start = artist.id
    step = artist.step
    if content['type'] == 'all':
        artists = get_artists_all(start, step)
    else:
        artists = search_artists(content, start, step)
    artist.list = artists
    del artist.step
    del artist.id


def __get_count_artists_list(artist: Artist, content: dict):
    """
    add count attr to artist elem
    :param artist: Artist class
    :param content: dictionary that contain the type and value of searching
    """
    artist.count = get_count_artists(content)
