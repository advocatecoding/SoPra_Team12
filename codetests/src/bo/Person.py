from bo import BusinessObject as bo

class Person(bo.BusinessObject):

    def __init__(self):
        super().__init__()
        self._vorname = ""
        self._nachname = ""
        self._mail_adresse = ""
        self._benutzername = ""
        self._urlaubstage = 0
        self._ueberstunden = 0

    def get_vorname(self):
        return self._vorname

    def set_vorname(self, value):
        self._vorname = value

    def get_nachname(self):
        return self._nachname

    def set_nachname(self, value):
        self._nachname = value

    def get_mail_adresse(self):
        return self._mail_adresse

    def set_mail_adresse(self, value):
        self._mail_adresse = value

    def get_benutzername(self):
        return self._benutzername

    def set_benutzername(self, value):
        self._benutzername = value

    def get_urlaubstage(self):
        return self._urlaubstage

    def set_urlaubstage(self, value):
        self._urlaubstage = value

    def get_ueberstunden(self):
        return self._ueberstunden

    def set_ueberstunden(self, value):
        self._ueberstunden = value




