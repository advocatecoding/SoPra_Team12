from bo import BusinessObject as bo

"""
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
 * @author [Nicola Pany](https://github.com/NicolaPany)
"""

class Urlaub (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person_id = None
        self._start_date = None
        self._end_date = None

    def set_person_id(self, person_id):
        """Setzen der Person ID."""
        self._person_id = person_id

    def get_person_id(self):
        """Auslesen der Person ID."""
        return self._person_id

    def set_start_date(self, start_date):
        """Setzen der Start Date."""
        self._start_date = start_date

    def get_start_date(self):
        """Auslesen der Start Date."""
        return self._start_date

    def set_end_date(self, end_date):
        """Setzen der End Date."""
        self._end_date = end_date

    def get_end_date(self):
        """Auslesen der End Date."""
        return self._end_date


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Urlaub()."""
        obj = Urlaub()
        obj.set_id(dictionary["id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_start_date(dictionary["start_datum"])
        obj.set_end_date(dictionary["end_datum"])
        obj.set_letzte_aenderung()

        return obj