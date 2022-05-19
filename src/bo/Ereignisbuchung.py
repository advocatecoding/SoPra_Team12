from bo import BusinessObject as bo

class Ereignisbuchung(bo.BusinessObject):
    def __init__(self, kommen, gehen):
        super().__init__()
        self.__startereignis = kommen.get_start()
        self.__endereignis = gehen.get_ende()
        #self.__ereignis_type = type(self.__ereignis).__name__
        self.__aktivitaet = kommen.get_aktivitaet()
        self.__person = kommen.get_person()

        """ Da in der Init-Methode alle Attribute gesetzt werden, benötigen wir keine setter-Methoden mehr"""

    def set_startereignis(self, value):
        self.__startereignis = value

    def get_startereignis(self):
        return self.__startereignis

    def set_endereignis(self, value):
        self.__endereignis  = value

    def get_endereignis(self):
        return self.__endereignis

    def add_ereignis(self, value):
        self.__ereignis_liste.append(value)

    def get_aktivitaet(self):
        return self.__aktivitaet

    def get_person(self):
        return self.__person


    def get_ereignis_list(self):
        return self.__ereignis_liste

    """ Falls nur ein Ereignis pro Ereignisbuchung gesetzt wird
        def get_ereignis_type(self):
            return self.__ereignis_type
    """

"""
    def __init__(self, start_ereignis, end_ereignis):
        super().__init__()
        self.__start_ereignis = start_ereignis
        self.__end_ereignis = end_ereignis

    def set_start_ereignis(self, value):
        self.__start_ereignis = value.get_start()
        print(type(self.__start_ereignis))

    def get_start_ereignis(self):
        return self.__start_ereignis

    def set_end_ereignis(self, value):
        self.__end_ereignis = value.get_end()

    def get_end_ereignis(self):
        return self.__end_ereignis
"""