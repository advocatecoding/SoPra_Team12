from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self, zeitpunkt, person):
        super().__init__(zeitpunkt, person)
        self.__zeitpunkt = zeitpunkt
        self.__person = person

    def set_ende(self, value):
        self.__zeitpunkt = value

    def get_ende(self):
        return self.__zeitpunkt