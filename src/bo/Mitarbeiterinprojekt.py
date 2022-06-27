from bo import BusinessObject as bo

class MitarbeiterInProjekt(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person = ""
        self._projekt = ""
        self._verkaufte_stunden = 0


    def get_person(self):
        """Auslesen des Vornamens."""
        return self._person

    def set_person(self, value):
        """Setzen des Vornamens."""
        self._person = value

    def get_projekt(self):
        """Auslesen des Projektnamens."""
        return self._projekt

    def set_projekt(self, value):
        """Setzen des Projektnamens."""
        self._projekt = value

    def get_verkaufte_stunden(self):
        """Auslesen der E-Mail Adresse."""
        return self._verkaufte_stunden


    def set_verkaufte_stunden(self, verkaufte_stunden):
         self._verkaufte_stunden = verkaufte_stunden


    def from_dict(dictionary=dict()):
        obj = MitarbeiterInProjekt()
        obj.set_person(dictionary["mitarbeiter"])
        obj.set_projekt(dictionary["projekt_id"])
        obj.set_verkaufte_stunden(dictionary["verkaufte_stunden"])
        obj.set_letzte_aenderung()

        return obj


