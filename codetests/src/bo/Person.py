from bo import BusinessObject as bo

class Person(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = ""
        self._nachname = ""

    def get_vorname(self):
        return self._vorname

    def set_vorname(self, value):
        self._vorname = value

    def get_nachname(self):
        return self._nachname

    def set_nachname(self, value):
        self._nachname = value

    def get_name(self):
        return self.__name

