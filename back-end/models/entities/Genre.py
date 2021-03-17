from BillbordElement import BillboardElement


class Genre(BillboardElement):
    def __init__(self, id_genre: int, name: str, image: str):
        """
        Initialisation of genre
        Necessary params:
        :param id_genre: id genre
        :param name: name of genre
        :param image: picture of genre
        """
        super().__init__(id_genre, name, image)
        self.id = id_genre
        self.name = name
        self.image = image
