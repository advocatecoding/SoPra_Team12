from bo import BusinessObject as bo

class Ereignisbuchung(bo.BusinessObject):
    def __init__(self, start, ende):
        super().__init__()
        self.__startereignis = start.get_start()
        self.__endereignis = ende.get_ende()
        #self.__ereignis_type = type(self.__ereignis).__name__
        self.__person = start.get_person()
        """ Da in der Init-Methode alle Attribute gesetzt werden, benötigen wir keine setter-Methoden mehr"""

    def get_startereignis(self):
        return self.__startereignis

    def get_endereignis(self):
        return self.__endereignis

    def get_person(self):
        return self.__person

