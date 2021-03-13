from connection_to_data_base import get_data_from_db


def limit_information(sql_request: str, start=0, step=0) -> str:
    if start:
        sql_request += ' LIMIT ' + str(step)
    if step:
        sql_request += ' OFFSET ' + str(start)
    return sql_request


def get_count(sql_request) -> int:
    sql_data = get_data_from_db(sql_request)

    return sql_data[0][0]


def get_count_table(table_name) -> int:
    sql_request = "SELECT COUNT(*) FROM " + table_name

    count = get_count(sql_request)
    return count




