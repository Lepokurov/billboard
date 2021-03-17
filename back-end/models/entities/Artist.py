from BillbordElement import BillboardElement


class Artist(BillboardElement):
    def __init__(self, id_artist: int, name: str, image: str):
        """
        Initialisation of artist
        Necessary params:
        :param id_artist: id go artist
        :param name: title of artist
        :param image: image of artist
        """
        super().__init__(id_artist, name, image)
        self.id = id_artist
        self.name = name
        self.image = image

