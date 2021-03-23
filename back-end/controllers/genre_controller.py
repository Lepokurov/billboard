from Genre import Genre
from factory import Factory
factory = Factory()


def get_genres(type_: str, value_: str, page: int, step: int):
    genre = factory.get_elem_list(Genre, type_, value_, page, step)
    return genre


def get_genre(id_song):
    genre = factory.get_elem_solo(Genre, id_song)
    return genre


def count_genres(type_: str, value_=''):
    count = factory.get_elem_count(Genre, type_, value_)
    return count
