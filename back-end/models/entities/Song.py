class Song:
    def __init__(self, id_song: int, step=1):
        """
        Initialisation of song
        :param id_song: id of song/the start row (list)
        :param step: number of rows if need one elem (no list) then step = 1
        """
        self.id = id_song
        self.step = step
