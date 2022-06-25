from bo.Ereignis import Ereignis

class Kommen(Ereignis):

    def __init__(self, zeitpunkt, person):
        super().__init__(zeitpunkt, person)
        self.__zeitpunkt = zeitpunkt
        self.__person = person

    def set_start(self, value):
        self.__zeitpunkt = value

    def get_start(self):
        return self.__zeitpunkt
