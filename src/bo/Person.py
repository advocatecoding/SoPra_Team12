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
        self._user_id = ""

    def get_vorname(self):
        """Auslesen des Vornamens."""
        return self._vorname

    def set_vorname(self, value):
        """Setzen des Vornamens."""
        self._vorname = value

    def get_nachname(self):
        """Auslesen des Nachnamens."""
        return self._nachname

    def set_nachname(self, value):
        """Setzen des Nachnamens."""
        self._nachname = value

    def get_mail_adresse(self):
        """Auslesen der E-Mail Adresse."""
        return self._mail_adresse

    def set_mail_adresse(self, value):
        """Setzen der E-Mail Adresse."""
        self._mail_adresse = value

    def get_benutzername(self):
        """Auslesen des Benutzernamens."""
        return self._benutzername

    def set_benutzername(self, value):
        """Setzen des Benutzernamens."""
        self._benutzername = value

    def get_urlaubstage(self):
        """Auslesen der Urlaubstage."""
        return self._urlaubstage

    def set_urlaubstage(self, value):
        """Setzen der Urlaubstage."""
        self._urlaubstage = value

    def get_ueberstunden(self):
        """Auslesen der Überstunden."""
        return self._ueberstunden

    def set_ueberstunden(self, value):
        """Setzen der Überstunden."""
        self._ueberstunden = value

    def get_user_id(self):
        return self._user_id

    def set_user_id(self, value):
        self._user_id = value


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Person()."""
        obj = Person()
        obj.set_id(dictionary["id"])
        obj.set_vorname(dictionary["vorname"])
        obj.set_nachname(dictionary["nachname"])
        obj.set_mail_adresse(dictionary["mail_adresse"])
        obj.set_benutzername(dictionary["benutzername"])
        obj.set_urlaubstage(dictionary["urlaubstage"])
        obj.set_ueberstunden(dictionary["überstunden"])
        obj.set_letzte_aenderung()
        obj.set_user_id(dictionary["user_id"])

        return obj






