class Genre:
    def __init__(self, id_genre: int, step=1):
        """
        Initialisation of genre
        :param id_genre: id genre/the start row (list)
        :param step: number of rows if need one elem (no list) then step = 1
        """
        self.id = id_genre
        self.step = step
