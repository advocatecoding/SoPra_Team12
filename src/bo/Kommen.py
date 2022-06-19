from bo.Ereignis import Ereignis

class Kommen(Ereignis):

    def __init__(self, zeitpunkt):
        super().__init__(zeitpunkt)
        self.__zeitpunkt = zeitpunkt
        self.__person_id = ""

    def set_person_id(self, value):
        self.__person_id = value

    def get_person_id(self):
        return self.__person_id


    def get_start(self):
        return self.__zeitpunkt
