from bo import BusinessObject as bo

class Ereignisbuchung(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._kommen_id = ""
        self._gehen_id = ""

    def get_kommen_id(self):
        return self._kommen_id

    def set_kommen_id(self, value):
        self._kommen_id = value

    def get_gehen_id(self):
        return self._gehen_id

    def set_gehen_id(self, value):
        self._gehen_id = value
