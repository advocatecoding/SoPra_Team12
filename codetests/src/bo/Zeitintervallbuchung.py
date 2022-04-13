from bo.BusinessObject import BusinessObject as bo

class Zeitinverallbuchung(bo):

    def __init__(self):
        self.__person_id = None
        self.__aktivitaet_id = None
        self.__buchungsart_id = None
        self.__zeit = 0

        if self.__buchungsart_id is None:
            print("Wir haben ein Pause")


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
        self.__person_id = value

    def get_person(self):
        return self.__person_id

    def set_aktivitaet(self, value):
        self.__aktivitaet_id = value

    def get_aktivitaet(self):
        return self.__aktivitaet_id

    def get_buchungsart(self):
        return self.__buchungsart_id

    def set_buchungsart(self, value):
        self.__buchungsart_id = value

"""
if type(buchungsart) == Projektarbeit:
Wenn Zeitintervall eine Projektarbeit ist -> Keine Pause
aktivität.set_gearbeitet(zeit)
"""