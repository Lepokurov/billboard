class Year:
    def __init__(self, year: int, step=1):
        """
        Initialisation of year
        :param year: billboard year/the start row (list)
        :param step: number of rows if need one elem (no list) then step = 1
        """
        self.year = year
        self.step = step
