from bo.Ereignis import Ereignis

"""

 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
 * @author [Manuel Bräuninger](https://github.com/manu-br)
"""

class Kommen(Ereignis):

    def __init__(self):
        super().__init__()
        self._start_kommen = ""
        self.set_type("Kommen")

    def set_start_kommen(self, value):
        self._start_kommen = value

    def get_start_kommen(self):
        return self._start_kommen

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Kommen()."""
        obj = Kommen()
        obj.set_id(dictionary["id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_start_kommen(dictionary["start_kommen"])
        obj.set_letzte_aenderung()

        return obj