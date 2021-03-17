from BillbordElement import BillboardElement


class Song(BillboardElement):
    def __init__(self, id_song: int, title: str, image: str):
        """
        Initialisation of song
        Necessary params:
        :param id_song: id of song
        :param title: title of song
        :param image: cover of song
        """
        super().__init__(id_song, title, image)
        self.id = id_song
        self.title = title
        self.image = image

