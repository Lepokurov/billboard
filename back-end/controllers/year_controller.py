from Year import Year
from factory import Factory
factory = Factory()


def get_years(type_: str, value_: str, page: int, step: int):
    """
    get Year element with list attr
    :param type_: required type
    :param value_: required value
    :param page: number of page
    :param step: count of elements
    :return: Year class with list attr
    """
    years = factory.get_elem_list(Year, type_, value_, page, step)
    return years


def get_year(year):
    """
    get Year element with attrs
    :param year: billboard year
    :return: Year class with attrs
    """
    years = factory.get_elem_solo(Year, year)
    return years


def count_years(type_: str, value_=''):
    """
    get count years by type and value
    :param type_: required type
    :param value_: required value
    :return: count years
    """
    count = factory.get_elem_count(Year, type_, value_)
    return count
