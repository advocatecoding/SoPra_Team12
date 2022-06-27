from bo.Ereignis import Ereignis

class Gehen(Ereignis):

    def __init__(self):
        super().__init__()
        self._ende = ""
        self.set_type("Gehen")

    def set_ende(self, value):
        self._ende = value

    def get_ende(self):
        return self._ende