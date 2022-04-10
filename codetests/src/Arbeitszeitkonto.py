class Arbeitszeitkonto:
    def __init__(self):
        self.zeit_gesamt = 0
        self.__owner_id = None

    def set_owner(self, owner):
        self.__owner = owner