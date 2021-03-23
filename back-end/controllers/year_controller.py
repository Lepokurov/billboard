from Year import Year
from factory import Factory
factory = Factory()


def get_years(type_: str, value_: str, page: int, step: int):
    years = factory.get_elem_list(Year, type_, value_, page, step)
    return years


def get_year(id_song):
    years = factory.get_elem_solo(Year, id_song)
    return years


def count_years(type_: str, value_=''):
    count = factory.get_elem_count(Year, type_, value_)
    return count
