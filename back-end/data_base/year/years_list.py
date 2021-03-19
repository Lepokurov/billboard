from connection_to_data_base import get_data_from_db
from mapper_year import create_years_list
from sql_request_years import _sql_constructor_years


def get_years_all(start, step) -> dict:
    """
    Getting tuple of years data from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: dict of years data
    """
    years_ = [i for i in range(start, start - step - 1, -1)]
    order = 'order by billboard.year DESC'
    years = get_years_list(years_, order)
    return years


def get_years_list(years_, order='') -> dict:
    """
    Main function for getting tuple of years data by ids
    :param years_: list of required years
    :param order: request information of 'order by'
    :return: tuple of years data or empty list if doesn't have required information
    """
    sql_request = _sql_constructor_years(years_, order)

    sql_data = get_data_from_db(sql_request)
    years = create_years_list(sql_data)
    return years
