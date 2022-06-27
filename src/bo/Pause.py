from bo.Zeitintervall import Zeitintervall

class Pause(Zeitintervall):
    def __init__(self):
        super().__init__()
        self.set_type("Pause")
        