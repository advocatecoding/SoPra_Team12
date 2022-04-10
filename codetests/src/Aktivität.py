from src.Person import Person

class Aktivität:
    def __init__(self):
        self.__arbeitszeit = {}

    def set_arbeitszeit1(self, arbeiter, zeit):
        self.__arbeitszeit[arbeiter] = zeit
    
    def set_arbeitszeit2(self, dict):
        self.__arbeitszeit = dict 
    

    def get_arbeitszeit(self):
        return self.__arbeitszeit


person1 = Person("Harry", 0)
person2 = Person("Hermine", 1)

arbeitszeitszuweisung = {person1: 30, person2: 15}

aktivitätA = Aktivität()
#aktivitätA.set_arbeitszeit2(arbeitszeitszuweisung)



aktivitätA.set_arbeitszeit1(person1.get_id(), 30)
aktivitätA.set_arbeitszeit1(person2.get_id(), 15)
print(aktivitätA.get_arbeitszeit())