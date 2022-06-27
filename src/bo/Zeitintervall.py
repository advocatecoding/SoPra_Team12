from bo import BusinessObject as bo

class Zeitintervall(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._type = ""
        self._person_id = ""
        self._start = ""
        self._ende = ""
        self._projektarbeit_id = None
        self._pause_id = None

    def set_type(self, value):
        self._type = value

    def get_type(self):
        return self._type

    def set_projektarbeit_id(self, value):
        self._projektarbeit_id = value

    def get_projektarbeit_id(self):
        return self._projektarbeit_id

    def set_pause_id(self, value):
        self._pause_id = value

    def get_pause_id(self):
        return self._pause_id

    def get_person_id(self):
        return self._person_id

    def set_person_id(self, value):
        self._person_id = value

    def get_start(self):
        return self._start

    def set_start(self, value):
        self._start = value

    def get_ende(self):
        return self._ende

    def set_ende(self, value):
        self._ende = value