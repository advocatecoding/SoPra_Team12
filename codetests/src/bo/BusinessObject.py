from abc import ABC

class BusinessObject(ABC):
    def __init__(self):
        self._id = 0
        self._letzte_aenderung = None

    def get_id(self):
        return self._id

    def set_id(self, value):
        self._id = value

    def get_letzte_aenderung(self):
        return self._letzte_aenderung

    def set_letzte_aenderung(self, value):
        self._letzte_aenderung = value