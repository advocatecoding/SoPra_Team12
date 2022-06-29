from bo import BusinessObject as bo

class MitarbeiterAnsicht(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person = ""
        self._nachname = ""
        self._aktivitaet = ""
        self._projekt = ""
        self._gearbeitete_zeit = 0


    def get_person(self):
        """Auslesen der Person ID """
        return self._person

    def set_person(self, value):
        """Setzen der Person ID."""
        self._person = value

    def get_nachname(self):
        """Auslesen des Nachnamens """
        return self._nachname

    def set_nachname(self, value):
        """Setzen des Nachnamens."""
        self._nachname = value

    def get_aktivitaet(self):
        """Auslesen der Aktivität ID."""
        return self._aktivitaet

    def set_aktivitaet(self, value):
        """Setzen der Aktivität ID."""
        self._aktivitaet = value

    def get_projekt(self):
        """Auslesen der Aktivität ID."""
        return self._projekt

    def set_projekt(self, value):
        """Setzen der Aktivität ID."""
        self._projekt = value


    def get_gearbeitete_zeit(self):
        """Auslesen der gebuchten stunden."""
        return self.__gearbeitete_zeit


    def set_gearbeitete_zeit(self, gearbeitete_zeit):
        """Setzen der gebuchten stunden."""
        self._gearbeitete_zeit = gearbeitete_zeit




    def from_dict(dictionary=dict()):
        obj = MitarbeiterAnsicht()
        obj.set_person(dictionary["mitarbeiter"])
        obj.set_nachname(dictionary["nachname"])
        obj.set_aktivitaet(dictionary["aktivitaet"])
        obj.set_projekt(dictionary["projekt"])
        obj.set_gearbeitete_zeit(dictionary["gearbeitete_zeit"])
        obj.set_letzte_aenderung()

        return obj


