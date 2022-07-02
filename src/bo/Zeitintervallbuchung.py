from bo.BusinessObject import BusinessObject as bo

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
 * @author [Talha Yildirim](https://github.com/talha16)
"""

class Zeitinverallbuchung(bo):

    def __init__(self, zeitintervall=None, aktivitaet=None):
        """ Das übergebene Zeitintervallobjekt beinhaltet ein Zeitintervall & eine Person """
        if zeitintervall and aktivitaet is not None:
            self._zeitintervall = zeitintervall.get_zeitintervall()
            self._person_id = zeitintervall.get_person().get_id()
            self._aktivitaet_id = aktivitaet.get_id()
            self.__buchungsart = type(zeitintervall).__name__
            """ Im nächsten Schritt: self.__projekt_id = aktivitaet.get_projekt_id();"""
            if self.__buchungsart == "Projektarbeit":
                print("Die Person {0} hat auf die Aktivität {1} eine Projektarbeit von {2}h gebucht".format(
                    self.__person.get_vorname(), self.__aktivitaet.get_name(), self._zeitintervall))
            else:
                print("Die Person {0} hat auf die Aktivität {1} eine Pause von {2}h gebucht".format(
                    self.__person.get_vorname(), self.__aktivitaet.get_name(), self._zeitintervall))

        self._projekt_id = ""


    def get_buchungsart(self):
        return self.__buchungsart

    def get_zeitintervall(self):
        return self._zeitintervall

    def set_zeitintervall(self, value):
        self._zeitintervall = value

    def get_projekt(self):
        return self._projekt_id

    def get_person_id(self):
        return self._person_id

    def set_person_id(self, value):
        self._person_id = value

    def get_aktivitaet(self):
        return self._aktivitaet_id


    def get_projekt_id(self):
        return self._projekt_id

    def set_projekt_id(self, value):
        self._projekt_id = value


    def get_aktivitaet_id(self):
        return self._aktivitaet_id

    def set_aktivitaet_id(self, value):
        self._aktivitaet_id = value

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Zeitinverallbuchung()
        obj.set_id(dictionary["id"])
        obj.set_projekt_id(dictionary["projekt_id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_aktivitaet_id(dictionary["aktivitaet_id"])
        obj.set_zeitintervall(dictionary["gearbeitete_zeit"])
        obj.set_letzte_aenderung()

        return obj

