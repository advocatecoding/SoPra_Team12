from bo import BusinessObject as bo

class Ereignisbuchung(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._kommen_id = ""
        self._gehen_id = ""

    def get_kommen_id(self):
        """Auslesen der Kommen ID."""
        return self._kommen_id

    def set_kommen_id(self, value):
        """Setzen der Kommen ID."""
        self._kommen_id = value

    def get_gehen_id(self):
        """Auslesen der Gehen ID."""
        return self._gehen_id

    def set_gehen_id(self, value):
        """Setzen der Gehen ID."""
        self._gehen_id = value


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Ereignisbuchung()."""
        obj = Ereignisbuchung()
        obj.set_id(dictionary["id"])
        obj.set_kommen_id(dictionary["kommen_id"])
        obj.set_gehen_id(dictionary["gehen_id"])
        obj.set_letzte_aenderung()

        return obj