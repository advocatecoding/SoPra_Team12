from bo.Zeitintervall import Zeitintervall

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
"""

class Projektarbeit(Zeitintervall):
    def __init__(self):
        super().__init__()
        self._projekt_id = ""
        self._person_id = ""
        self._aktivitaet_id = ""
        self._start = ""
        self._ende = ""
        self.set_type("Projektarbeit")


    def set_projekt_id(self, value):
        """Setzen der Projekt ID."""
        self._projekt_id = value

    def get_projekt_id(self):
        """Auslesen der Projekt ID."""
        return self._projekt_id

    def set_person_id(self, value):
        """Setzen der Person ID."""
        self._person_id = value

    def get_person_id(self):
        """Auslesen der Person ID."""
        return self._person_id

    def set_aktivitaet_id(self, value):
        """Setzen der Aktivität ID."""
        self._aktivitaet_id = value

    def get_aktivitaet_id(self):
        """Auslesen der Aktivität ID."""
        return self._aktivitaet_id



    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in Projektarbeit()."""
        obj = Projektarbeit()
        obj.set_id(dictionary["id"])
        obj.set_projekt_id(dictionary["projekt_id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_aktivitaet_id(dictionary["aktivitaet_id"])
        obj.set_start(dictionary["start"])
        obj.set_ende(dictionary["ende"])
        obj.set_letzte_aenderung()

        return obj