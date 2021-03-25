from connection_to_data_base import get_count
from sql_request_years import _sql_request_years_all, _sql_request_years_search


def get_count_years(content) -> int:
    count = 0
    if content['type'] == 'search':
        count = __get_count_year_search(content['value'])
    elif content['type'] == 'all':
        count = __get_count_year_all()
    return count


def __get_count_year_all() -> int:
    """
    get count billboard years
    :return: count
    """
    sql_request = _sql_request_years_all()

    count = get_count(sql_request)
    return count


def __get_count_year_search(search) -> int:
    """
    get count billboard years by search year data
    :param search: search year data
    :return: count
    """
    sql_request = _sql_request_years_search(search)

    count = get_count(sql_request)
    return count
