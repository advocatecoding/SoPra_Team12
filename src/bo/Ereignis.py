from bo import BusinessObject as bo


class Ereignis(bo.BusinessObject):

    def __init__(self, zeitpunkt):
        super().__init__()
        self.__zeitpunkt = zeitpunkt