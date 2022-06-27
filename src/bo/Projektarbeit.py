from bo.Zeitintervall import Zeitintervall

class Projektarbeit(Zeitintervall):
    def __init__(self):
        super().__init__()
        self._projekt_id = ""
        self._aktivitaet_id = ""
        self._gearbeitete_zeit = ""
        self.set_type("Projektarbeit")

    def set_projekt_id(self, value):
        self._projekt_id = value

    def get_projekt_id(self):
        return self._projekt_id

    def set_aktivitaet_id(self, value):
        self._aktivitaet_id = value

    def get_aktivitaet_id(self):
        return self._aktivitaet_id

    def set_gearbeitete_zeit(self, value):
        self._gearbeitete_zeit = value

    def get_gearbeitete_zeit(self):
        return self._gearbeitete_zeit

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Urlaub()."""
        obj = Projektarbeit()
        obj.set_id(dictionary["id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_projekt_id(dictionary["projekt_id"])
        obj.set_aktivitaet_id(dictionary["aktivitaet_id"])
        obj.set_gearbeitete_zeit(dictionary["gearbeitete_zeit"])
        obj.set_letzte_aenderung()

        return obj