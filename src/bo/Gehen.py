from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self):
        super().__init__()
        self._ende = ""
        self.set_type("Gehen")

    def set_ende(self, value):
        """Setzen der Endzeit."""
        self._ende = value

    def get_ende(self):
        """Auslesen der Endzeit."""
        return self._ende

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Gehen()."""
        obj = Gehen()
        obj.set_id(dictionary["id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_ende(dictionary["ende"])
        obj.set_letzte_aenderung()

        return obj