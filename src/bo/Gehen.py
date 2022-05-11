from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self, zeitpunkt):
        super().__init__(zeitpunkt)
        self.__zeitpunkt = zeitpunkt

    def set_ende(self, value):
        self.__zeitpunkt = value

    def get_ende(self):
        return self.__zeitpunkt