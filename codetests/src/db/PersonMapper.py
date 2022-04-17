from bo.Person import Person
from db.Mapper import Mapper

class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT vorname, nachname from Person")
        person_daten = cursor.fetchall()

        for (vorname, nachname) in person_daten:
            person = Person()
            person.set_vorname(vorname)
            person.set_nachname(nachname)
            print(person.get_vorname())
            result.append(person)
            print(result)

        self._cnx.commit()
        cursor.close()

        return result

""" Tesing """
if __name__ == '__main__':
    with PersonMapper() as mapper:
        result = mapper.find_all()
