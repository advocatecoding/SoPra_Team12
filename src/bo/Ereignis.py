from bo import BusinessObject as bo


class Ereignis(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._person_id = ""
        self._type = ""

    def get_person_id(self):
        return self._person_id

    def set_person_id(self, value):
        self._person_id = value

    def get_type(self):
        return self._type

    def set_type(self, value):
        self._type = value