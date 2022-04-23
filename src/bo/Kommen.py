from bo.Ereignis import Ereignis

class Kommen(Ereignis):

    def __init__(self, zeitpunkt):
        super().__init__(zeitpunkt)
        self.__zeitpunkt = zeitpunkt

    def set_start(self, value):
        self.__zeitpunkt = value

    def get_start(self):
        return self.__zeitpunkt
