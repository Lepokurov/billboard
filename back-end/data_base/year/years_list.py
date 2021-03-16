from connection_to_data_base import get_data_from_db
from models import create_years_info
from sql_request_years import sql_constructor_years


def get_years_all(start, step) -> list:
    """
    Getting list of years from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: list of years
    """
    years_ = [i for i in range(start, start - step - 1, -1)]
    order = 'order by billboard.year DESC'
    years = get_years_list(years_, order)
    return years


def get_years_list(years_, order='') -> list:
    """
     Main function for getting list of artists by ids
    :param years_: list of required years
    :param order: request information of 'order by'
    :return: list of artists or empty list if doesn't have required information
    """
    sql_request = sql_constructor_years(years_, order)

    sql_data = get_data_from_db(sql_request)

    years = create_years_info(sql_data)
    return years
