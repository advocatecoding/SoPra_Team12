from bo import BusinessObject as bo


class Ereignis(bo.BusinessObject):

    def __init__(self, zeitpunkt):
        super().__init__()
        self.__zeitpunkt = zeitpunkt
        self.__person = ""

    def get_zeitpunkt(self):
        return self.__zeitpunkt


    def get_person_id(self):
        return self.__person

    def set_person_id(self, value):
        self.__person = value