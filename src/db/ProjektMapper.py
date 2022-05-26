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


    def find_by_id(self, id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Projekt WHERE projekt_id={0}".format(id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        try:
            (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung) = projekt_daten[0]
            print(projekt_daten)
            projekt = Projekt()
            projekt.set_name(projektname)
            projekt.set_auftraggeber(auftraggeber)
            projekt.set_id(projekt_id)
            projekt.set_projektleiter(person_id)
            projekt.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result = projekt
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern projekt_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result


    def insert(self, projekt):
        """ Einfügen eines neuen Projekt-Objekts in die Datenbank.
        parameter: Projekt Instanz die in der Datenbank gespeichert werden soll
        return: Die Projekt Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(projekt_id) AS maxid FROM projekt ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projekt.set_id(maxid[0] + 1)


        """ Hier wird die Projekt Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO projekt (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (projekt.get_id(), projekt.get_projektleiter(), projekt.get_name(), projekt.get_auftraggeber(), projekt.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projekt



    def delete(self, projekt):
        """Löschen der Daten eines Projekt-Objekts aus der Datenbank.

        :param projekt das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM projekt WHERE projekt_id={}".format(projekt)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return projekt



    def update(self, projekt):
        cursor = self._cnx.cursor()

        command = "UPDATE projekt " + "SET person_id=%s, projektname=%s, auftraggeber=%s, letzte_aenderung=%s WHERE projekt_id=%s"
        data = (projekt.get_projektleiter(), projekt.get_name(), projekt.get_auftraggeber(), projekt.get_letzte_aenderung(), projekt.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()










if __name__ == '__main__':
    with ProjektMapper() as mapper:
        result = mapper.find_all()