from Genre import Genre
from factory import Factory
factory = Factory()


def get_genres(type_: str, value_: str, page: int, step: int):
    """
    get Genre element with list attr
    :param type_: required type
    :param value_: required value
    :param page: number of page
    :param step: count of elements
    :return: Genre class with list attr
    """
    genre = factory.get_elem_list(Genre, type_, value_, page, step)
    return genre


def get_genre(id_genre):
    """
    get Genre element with attrs
    :param id_genre: id of genre
    :return: Genre class with attrs
    """
    genre = factory.get_elem_solo(Genre, id_genre)
    return genre


def count_genres(type_: str, value_=''):
    """
    get count genres by type and value
    :param type_: required type
    :param value_: required value
    :return: count genres
    """
    count = factory.get_elem_count(Genre, type_, value_)
    return count
