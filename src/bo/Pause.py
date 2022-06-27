from bo.Zeitintervall import Zeitintervall

class Pause(Zeitintervall):
    def __init__(self):
        super().__init__()
        self._start_pause = ""
        self._ende_pause = ""
        self.set_type("Pause")


    def set_start_pause(self, value):
        self.start_pause = value

    def get_start_pause(self):
        return self._start_pause

    def set_ende_pause(self, value):
        self.ende_pause = value

    def get_ende_pause(self):
        return self._ende_pause


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Pause()."""
        obj = Pause()
        obj.set_id(dictionary["id"])
        obj.set_person_id(dictionary["person_id"])
        obj.set_start_pause(dictionary["start_pause"])
        obj.set_ende_pause(dictionary["ende_pause"])
        obj.set_letzte_aenderung()

        return obj
        