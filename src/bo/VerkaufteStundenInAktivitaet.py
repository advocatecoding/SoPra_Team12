from bo import BusinessObject as bo

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
"""

class VerkaufteStundenInAktivitaet(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person = ""
        self._aktivitaet = ""
        self._gebuchte_stunden = 0


    def get_person(self):
        """Auslesen der Person ID."""
        return self._person

    def set_person(self, value):
        """Setzen der Person ID."""
        self._person = value

    def get_aktivitaet(self):
        """Auslesen der Aktivität ID."""
        return self._aktivitaet

    def set_aktivitaet(self, value):
        """Setzen der Aktivität ID."""
        self._aktivitaet = value

    def get_gebuchte_stunden(self):
        """Auslesen der gebuchten stunden."""
        return self._gebuchte_stunden

    def set_gebuchte_stunden(self, gebuchte_stunden):
        """Setzen der gebuchten stunden."""
        self._gebuchte_stunden = gebuchte_stunden


    def from_dict(dictionary=dict()):
        obj = VerkaufteStundenInAktivitaet()
        obj.set_person(dictionary["mitarbeiter"])
        obj.set_aktivitaet(dictionary["aktivitaet"])
        obj.set_gebuchte_stunden(dictionary["gebuchte_stunden"])
        obj.set_letzte_aenderung()

        return obj


