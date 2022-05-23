from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self, zeitpunkt, aktivitaet, person):
        super().__init__(zeitpunkt, aktivitaet, person)
        self.__zeitpunkt = zeitpunkt
        self.__person = person
        self.__aktivitaet = aktivitaet

    def set_ende(self, value):
        self.__zeitpunkt = value

    def get_ende(self):
        return self.__zeitpunkt