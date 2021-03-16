from sql_constructor_general import get_ids_by_request
from sql_request_years import sql_request_search_years
from years_list import get_years_list


def search_years(search_year, start=0, step=0):
    """
    Get years by the year
    :param search_year: year
    :param start: the start row
    :param step: number of rows
    :return: list of years by the required parameters
    """
    years_list = _get_years_(search_year, start, step)
    years = get_years_list(years_list)
    return years


def _get_years_(search_year, start, step) -> list:
    """
    get years (like ids) from search information
    :param search_year:search information
    :param start: the start row
    :param step: number of rows
    :return: years (like ids)
    """
    sql_request = sql_request_search_years(search_year)
    years = get_ids_by_request(sql_request, start, step)
    return years
