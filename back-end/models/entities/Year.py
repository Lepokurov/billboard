from BillbordElement import BillboardElement


class Year(BillboardElement):
    """
    Billboard year
    """
    def __init__(self, year: int):
        """
        Initialisation of year
        :param year: billboard year
        """
        super().__init__(year, '', '')
        self.year = year


