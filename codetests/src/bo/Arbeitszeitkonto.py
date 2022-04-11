class Arbeitszeitkonto:
    def __init__(self):
        self.zeit_gesamt = 0
        self.__owner = None

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_zeit_gesamt(self):
        return self.zeit_gesamt

    def set_zeit_gesamt(self, value):
        self.zeit_gesamt += value