from connection_to_data_base import get_data_from_db
from models import create_ids


def limit_information(sql_request: str, start, step) -> str:
    """
    For limiting rows by request
    :param sql_request:
    :param start: the start row
    :param step: number of rows
    :return: request str
    """
    if not start and not step:
        return sql_request
    sql_request += ' LIMIT ' + str(step)
    sql_request += ' OFFSET ' + str(start)
    return sql_request


def get_count_table(table_name) -> int:
    """
    constructor request to get all rows at table name
    :param table_name: name of table from database
    :return: request str
    """
    sql_request = "SELECT COUNT(*) FROM " + table_name

    return sql_request


def get_ids_all(start, step) -> list:
    """
    Getting all ids from start to end (start+step) inclusive
    :param start: the start row
    :param step: number of rows
    :return: list of ids
    """
    ids = [i for i in range(start, start + step+1)]
    return ids


def get_ids_by_request(sql_request, start=0, step=0) -> list:
    """
    Getting ids from start to end (start+step) inclusive by request
    :param sql_request: request
    :param start: the start row
    :param step: number of rows
    :return: list of ids
    """
    sql_request = limit_information(sql_request, start, step)
    sql_data = get_data_from_db(sql_request)
    ids = create_ids(sql_data)
    return ids
