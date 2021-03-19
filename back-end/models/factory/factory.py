from Artist import Artist
from Genre import Genre
from Song import Song
from Year import Year
from artist_creation import artist_information
from genre_creation import genre_information
from song_creation import song_information
from year_creation import year_information


class Factory:
    def __call__(self, billboard_elem, content: dict):
        if isinstance(billboard_elem, Song):
            song_information(billboard_elem, content)
        if isinstance(billboard_elem, Artist):
            artist_information(billboard_elem, content)
        if isinstance(billboard_elem, Genre):
            genre_information(billboard_elem, content)
        if isinstance(billboard_elem, Year):
            year_information(billboard_elem, content)


factory = Factory()
elem = Year(2014)
factory(elem,{'page': 'solo'})
a =1