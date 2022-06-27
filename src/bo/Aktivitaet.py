from bo.Person import Person
from bo import BusinessObject as bo


class Aktivitaet(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._name = ""
        self._projektname = ""
        self._kapazität = 0
        self._dauer = 0
        self.__arbeitszeit = {}

    def get_name(self):
        """Auslesen des Aktivitätsnamen."""
        return self._name

    def set_name(self, value):
        """Setzen der Aktivitätsnamen."""
        self._name = value

    def set_projektname(self, name):
        """Setzen des Projektnamens."""
        self._projektname = name

    def get_projektname(self):
        """Auslesen des Projektnamens."""
        return self._projektname

    def get_kapazitaet(self):
        """Auslesen der Kapazität."""
        return self._kapazität

    def set_kapazitaet(self, value):
        """Setzen der Kapazität."""
        self._kapazität = value

    def get_dauer(self):
        """Auslesen der Dauer."""
        return self._dauer

    def set_dauer(self, value):
        """Setzen der Dauer."""
        self._dauer = value

    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in eine Aktivität()."""
        obj = Aktivitaet()
        obj.set_id(dictionary["id"])
        obj.set_name(dictionary["aktivitaetname"])
        obj.set_projektname(dictionary["projekt_id"])
        obj.set_dauer(dictionary["dauer"])
        obj.set_kapazitaet(dictionary["kapazität"])
        obj.set_letzte_aenderung()

        return obj













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