from bo.Projekt import Projekt
from db.Mapper import Mapper

class ProjektMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT projektname, auftraggeber, projekt_id, person_id, letzte_aenderung from Projekt")
        projekt_daten = cursor.fetchall()

        for (projektname, auftraggeber, projekt_id,  person_id, letzte_aenderung) in projekt_daten:
            print(projekt_daten)
            projekt = Projekt()
            projekt.set_name(projektname)
            projekt.set_auftraggeber(auftraggeber)
            projekt.set_id(projekt_id)
            projekt.set_projektleiter(person_id)
            projekt.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(projekt)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result


if __name__ == '__main__':
    with ProjektMapper() as mapper:
        result = mapper.find_all()