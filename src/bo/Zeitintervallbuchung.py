from bo.BusinessObject import BusinessObject as bo

class Zeitinverallbuchung(bo):

    def __init__(self, zeitintervall=None):
        self._zeitintervall = zeitintervall
        self._projekt = None

    def get_zeitintervall(self):
        return self._zeitintervall

    def set_zeitintervall(self, value):
        self._zeitintervall = value

    def get_projekt(self):
        return self._projekt

    def set_projekt(self, value):
        self._projekt = value

"""
    def __init__(self):
        self.__person = None
        self.__aktivitaet = None
        self.__buchungsart = None
        self.__zeit = 0


    def set_zeitintervallbuchung(self, zeit, person, aktivitaet, buchungsart):
        self.set_person(person)
        self.set_aktivitaet(aktivitaet)
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

    def set_aktivitaet(self, value):
        self.__aktivitaet = value

    def get_aktivitaet(self):
        return self.__aktivitaet

    def get_buchungsart(self):
        return self.__buchungsart

    def set_buchungsart(self, value):
        self.__buchungsart = value
"""
"""
if type(buchungsart) == Projektarbeit:
Wenn Zeitintervall eine Projektarbeit ist -> Keine Pause
aktivität.set_gearbeitet(zeit)
"""