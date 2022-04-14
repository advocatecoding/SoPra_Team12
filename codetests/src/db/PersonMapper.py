from bo.Person import Person
from db.Mapper import Mapper

class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        #result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Person")
        person_daten = cursor.fetchall()

        print(person_daten)
        cursor.close()

""" Tesing """
if __name__ == '__main__':
    with PersonMapper() as mapper:
        result = mapper.find_all()
