from bo.Person import Person
from bo import BusinessObject as bo


class Aktivitaet(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self.__kapazität = 0
        self.__dauer = 0
        self.__arbeitszeit = {}

    def get_name(self):
        """Auslesen des Aktivitätsnamen."""
        return self._name

    def set_name(self, value):
        """Setzen der Aktivitätsnamen."""
        self._name = value

    def set_arbeitszeit(self, arbeiter, zeit):
        self.__arbeitszeit[arbeiter] = zeit

    def set_arbeitszeit2(self, dict):
        self.__arbeitszeit = dict

    def get_arbeitszeit(self):
        return self.__arbeitszeit

# person1 = Person("Harry", 0)
# person2 = Person("Hermine", 1)

# arbeitszeitszuweisung = {person1: 30, person2: 15}

# aktivitätA = Aktivität()
# aktivitätA.set_arbeitszeit2(arbeitszeitszuweisung)


# aktivitätA.set_arbeitszeit(person1.get_id(), 30)
# aktivitätA.set_arbeitszeit(person2.get_id(), 15)
# print(aktivitätA.get_arbeitszeit())