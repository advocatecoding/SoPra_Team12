from bo.Ereignis import Ereignis

class Kommen(Ereignis):

    def __init__(self):
        super().__init__()
        self._start = ""
        self.set_type("Kommen")

    def set_ende(self, value):
        self._start = value

    def get_ende(self):
        return self._start
