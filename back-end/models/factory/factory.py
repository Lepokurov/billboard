from Artist import Artist
from Genre import Genre
from Song import Song
from Year import Year
from artist_creation import artist_information
from content_create import create_content
from genre_creation import genre_information
from song_creation import song_information
from year_creation import year_information


class Factory:

    def get_elem_list(self, element, type_, value_, page, step):
        """
        get class with list attr
        :param element: Song/Artist/Genre/Year class
        :param type_: required type
        :param value_: required value
        :param page: number of page
        :param step: count of elements
        :return: element class with list attr
        """
        content = create_content('list', type_, value_)
        start = self.__get_start(page, step)
        elem = element(start, step)
        self.__create_elem(elem, content)
        return elem

    def get_elem_solo(self, element, id_elem):
        """
        get class with attrs
        :param element: Song/Artist/Genre/Year class
        :param id_elem: id of element
        :return: element class with attrs
        """
        elem = element(id_elem)
        self.__create_elem(elem, {'page': 'solo'})
        return elem

    def get_elem_count(self, element, type_, value_) -> int:
        """
        get count
        :param element: Song/Artist/Genre/Year class
        :param type_: required type
        :param value_: required value
        :return: count
        """
        content = create_content('count', type_, value_)
        elem = element(0)
        self.__create_elem(elem, content)
        return elem.count

    @staticmethod
    def __get_start(page, step) -> int:
        """
        get started elem by page
        :param page: number of page
        :param step: count of elements
        :return: started elem
        """
        start = step * (page - 1)
        return start

    @staticmethod
    def __create_elem(billboard_elem, content: dict):
        """
        change class elem by content
        :param billboard_elem: Song/Artist/Genre/Year class
        :param content: dictionary that contain the type and value of searching
        if billboard_elem not is Song/Artist/Genre/Year class raise classmethod error
        """
        if isinstance(billboard_elem, Song):
            song_information(billboard_elem, content)
        elif isinstance(billboard_elem, Artist):
            artist_information(billboard_elem, content)
        elif isinstance(billboard_elem, Genre):
            genre_information(billboard_elem, content)
        elif isinstance(billboard_elem, Year):
            year_information(billboard_elem, content)
        else:
            raise classmethod
