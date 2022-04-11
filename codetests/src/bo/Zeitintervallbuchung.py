from bo.BusinessObject import BusinessObject as bo

class Zeitinverallbuchung(bo):

    def __init__(self):
        self.__person = None
        self.__aktivität = None
        self.__buchungsart = None
        self.__zeit = 0


    def set_zeitintervallbuchung(self, zeit, person, aktivität, buchungsart):
        self.set_person(person)
        self.set_aktivität(aktivität)
        self.set_buchungsart(buchungsart)
        self.set_zeit(zeit)


    def get_zeit(self):
        return self.__zeit

    def set_zeit(self, value):
        self.__zeit = value

    def set_person(self, value):
        self.__person = value

    def get_person(self):
        return self.__person

    def set_aktivität(self, value):
        self.__aktivität = value

    def get_aktivität(self):
        return self.__aktivität

    def get_buchungsart(self):
        return self.__buchungsart

    def set_buchungsart(self, value):
        self.__buchungsart = value

"""
if type(buchungsart) == Projektarbeit:
Wenn Zeitintervall eine Projektarbeit ist -> Keine Pause
aktivität.set_gearbeitet(zeit)
"""