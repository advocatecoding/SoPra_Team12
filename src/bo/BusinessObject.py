from abc import ABC
from datetime import datetime

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

    def set_letzte_aenderung(self):
        """Wir möchten die Sekunden und kleinere Einheiten nicht anzeigen anlassen"""
        self._letzte_aenderung =  datetime.now().replace(second=0, microsecond=0)

    def set_letzte_aenderung_fuer_get_methode(self, value):
        """Notwendig damit keine neuen Werte für letzte_änderung gesetzt wird, wenn man sich Datensätze ausgeben lassen möchte"""
        self._letzte_aenderung =  value