from bo import Person


class Projektleiter(Person):

    def __init__(self):
        super().__init__()
        self._vorname = ""
        self._nachname = ""
        self._mail_adresse = ""
        self._benutzername = ""
        self._urlaubstage = 0
        self._ueberstunden = 0