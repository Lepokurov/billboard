import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def __connection():
    """
    Trying to connect to database
    :return: If connection is correct, then return connection. If connection is incorrect, then raise the error
    """
    try:
        connection = psycopg2.connect(user="postgres",
                                      database="billboard_data",
                                      password="admin",
                                      host="127.0.0.1",
                                      port="5432")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection
    except (Exception, Error) as error:
        print("Error of connecting to PostgreSQL", error)
        return error


def get_data_from_db(sql_request) -> tuple:
    """
    Function for getting information from the database
    :param sql_request: sql request
    :return: the data from database in tuple object
    """
    connection = __connection()
    cursor = connection.cursor()
    cursor.execute(sql_request)
    sql_data = cursor.fetchall()
    connection.close()
    return sql_data


