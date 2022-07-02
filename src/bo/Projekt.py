from bo import BusinessObject as bo

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
 * @author [Talha Yildirim](https://github.com/talha16)
"""

class Projekt(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._projektname = ""
        self._auftraggeber = ""
        """ Wir durch ein Zeitintervall Objekt festgelegt """
        self.__projektlaufzeit = None
        self._projektleiter = None


    def get_projektlaufzeit(self):
        """Setzen der Projektlaufzeit."""
        return self.__projektlaufzeit

    def set_projektlaufzeit(self, value):
        """Auslesen der Projektlaufzeit."""
        self.__projektlaufzeit = value

    def set_projektleiter(self,projektleiter):
        """Setzen des Projektleiters."""
        self._projektleiter = projektleiter

    def get_projektleiter(self):
        """Auslesen des Projektleiters."""
        return self._projektleiter

    def set_name(self, name):
        """Setzen des Projektnamens."""
        self._projektname = name

    def get_name(self):
        """Auslesen des Projektnamens."""
        return self._projektname

    def set_auftraggeber(self,auftraggeber):
        """Setzen des Auftraggebers."""
        self._auftraggeber = auftraggeber

    def get_auftraggeber(self):
        """Auslesen des Auftraggebers."""
        return self._auftraggeber


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Projekt()."""
        obj = Projekt()
        obj.set_id(dictionary["id"])
        obj.set_projektleiter(dictionary["projektleiter"])
        obj.set_name(dictionary["projektname"])
        obj.set_auftraggeber(dictionary["auftraggeber"])
        obj.set_letzte_aenderung()

        return obj


