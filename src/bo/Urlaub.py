from bo import BusinessObject as bo

class Urlaub (bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person_id = None
        self._start_date = None
        self._end_date = None

    def set_person_id(self, person_id):
        self._person_id = person_id

    def get_person_id(self):
        return self._person_id

    def set_start_date(self, start_date):
        self._start_date = start_date

    def get_start_date(self):
        return self._start_date

    def set_end_date(self, end_date):
        self._end_date = end_date

    def get_end_date(self):
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