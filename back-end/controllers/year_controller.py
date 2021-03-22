from Year import Year
from general_controller import get_elem_list, get_elem_solo, get_elem_count


def get_years(type_: str, value_: str, page: int, step: int):
    years = get_elem_list(Year, type_, value_, page, step)
    return years


def get_year(id_song):
    years = get_elem_solo(Year, id_song)
    return years


def count_years(type_: str, value_=''):
    count = get_elem_count(Year, type_, value_)
    return count
