from bo import BusinessObject as bo


class Ereignis(bo.BusinessObject):

    def __init__(self, ereignis):
        super().__init__()
        self.__zeitpunkt = ""
        self.__person = None
        self.__aktivitaet = None

    def get_zeitpunkt(self):
        return self.__zeitpunkt

    def set_zeitpunkt(self, value):
        self.__zeitpunkt = value

    def get_person(self):
        return self.__person

    def set_person(self, value):
        self.__person = value

    def get_aktivitaet(self):
        return self.__aktivitaet

    def set_aktivitaet(self, value):
        self.__aktivitaet = value
