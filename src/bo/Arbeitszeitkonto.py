class Arbeitszeitkonto:
    def __init__(self, owner):
        self.zeit_gesamt = 0
        self.__owner = owner
        self.__owner_id = owner.get_id()
        self.__projektarbeiten = []
        self.__pausen = []

    def set_owner(self, owner):
        self.__owner = owner

    def set_owner_id(self, owner):
        self.__owner_id = owner.get_id()

    def get_owner(self):
        return self.__owner

    def get_zeit_gesamt(self):
        return self.zeit_gesamt

    def get_buchungen(self):
        return self.__buchungen

    def add_buchung(self, zeitintervallbuchung):
        if zeitintervallbuchung.get_buchungsart() == "Projektarbeit":
            self.__projektarbeiten.append(zeitintervallbuchung)
        else:
            """ Wenn es keine Projektarbeit ist, muss es eine Pause sein. """
            self.__pausen.append(zeitintervallbuchung)
