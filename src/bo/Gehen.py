from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self, zeitpunkt):
        super().__init__(zeitpunkt)
        self.__zeitpunkt = zeitpunkt

    def set_end(self, value):
        self.__zeitpunkt = value

    def get_end(self):
        return self.__zeitpunkt