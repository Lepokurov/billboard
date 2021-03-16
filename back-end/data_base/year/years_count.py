from connection_to_data_base import get_count


def get_count_year_all() -> int:


    count = get_count(sql_request)
    return count


def get_count_year_search(search) -> int:
    sql_request = """SELECT count(*) FROM billboard WHERE billboard.position = 1 """


    count = get_count(sql_request)
    return count
