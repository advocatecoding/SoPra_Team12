from bo import BusinessObject as bo
from bo.Aktivitaet import Aktivitaet


class AktivitaetInProjekt(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._aktivitaet = ""
        self._projekt = ""

    def set_aktivitaet(self, value):
        self._aktivitaet = value

    def get_aktivitaet(self):
        return self._aktivitaet

    def get_projekt(self):
        """Auslesen des Projektnamens."""
        return self._projekt

    def set_projekt(self, value):
        """Setzen des Projektnamens."""
        self._projekt = value

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Aktivität()."""
        obj = AktivitaetInProjekt()
        obj.set_aktivitaet(dictionary["aktivitaet"])
        obj.set_projekt(dictionary["projekt"])

        return obj



