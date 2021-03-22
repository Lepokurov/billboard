from Genre import Genre
from general_controller import get_elem_list, get_elem_solo, get_elem_count


def get_genres(type_: str, value_: str, page: int, step: int):
    genre = get_elem_list(Genre, type_, value_, page, step)
    return genre


def get_genre(id_song):
    genre = get_elem_solo(Genre, id_song)
    return genre


def count_genres(type_: str, value_=''):
    count = get_elem_count(Genre, type_, value_)
    return count
