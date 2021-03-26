from Year import Year
from artists_for_description import get_artists_of_year
from generel_tool import add_to_class
from genres_for_description import get_genres_year
from songs_for_description import get_songs_year
from years_count import get_count_years
from years_list import get_years_all
from years_search import search_years


def year_information(year: Year, content: dict):
    """
    change year class with required attr by content
    :param year: Year class
    :param content: dictionary that contain the type and value of searching
    """
    if content['page'] == 'solo':
        __year_solo_page(year)
    elif content['page'] == 'list':
        __year_list_page(year, content)
    elif content['page'] == 'count':
        __get_count_years_list(year, content)


def __year_solo_page(year: Year):
    """
    add attrs to year elem for solo page showing
    :param year: Year class
    """
    year_ = year.year
    year_dict = {
        'songs': get_songs_year(year_),
        'artists': get_artists_of_year(year_),
        'genres': get_genres_year(year_)
    }
    add_to_class(year, year_dict)


def __year_list_page(year_: Year, content: dict):
    """
    add attrs to year elem for list page showing
    :param year_: Year class
    :param content: dictionary that contain the type and value of searching
    """
    start = year_.year
    step = year_.step
    if content['type'] == 'all':
        years = get_years_all(start, step)
    else:
        years = search_years(content, start, step)
    year_.list = years
    del year_.step
    del year_.year


def __get_count_years_list(year: Year, content: dict):
    """
    add count attr to year elem
    :param year: Year class
    :param content: dictionary that contain the type and value of searching
    """
    year.count = get_count_years(content)
