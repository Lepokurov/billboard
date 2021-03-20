class Artist:
    def __init__(self, id_artist: int, step=1):
        """
        Initialisation of artist
        :param id_artist: id go artist/the start row (list)
        :param step: number of rows if need one elem (no list) then step = 1
        """
        self.id = id_artist
        self.step = step
