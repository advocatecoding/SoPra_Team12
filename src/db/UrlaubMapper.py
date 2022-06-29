from bo.Urlaub import Urlaub
from db.Mapper import Mapper

class UrlaubMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """ Wir suchen alle Urlaube """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Urlaub")
        urlaub_daten = cursor.fetchall()

        for (urlaub_id, person_id, start_datum, end_datum, letzte_aenderung) in urlaub_daten:
            urlaub = Urlaub()
            urlaub.set_id(urlaub_id)
            urlaub.set_person_id(person_id)
            urlaub.set_start_date(start_datum)
            urlaub.set_end_date(end_datum)
            urlaub.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(urlaub)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result


    def insert(self, urlaub):
        """ Einfügen eines neuen Urlaub-Objekts in die Datenbank.
        parameter: Urlaub Instanz, die in der Datenbank gespeichert werden soll
        return: Die Urlaubsinstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(urlaub_id) AS maxid FROM Urlaub")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            urlaub.set_id(maxid[0] + 1)


        """ Hier wird die Urlaub Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Urlaub (urlaub_id, person_id, start_datum, end_datum, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (urlaub.get_id(), urlaub.get_person_id(), urlaub.get_start_date(), urlaub.get_end_date(),urlaub.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return urlaub

    def find_by_id(self, id):
        """ Wir suchen den Urlaub mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Urlaub WHERE urlaub_id={0}".format(id)
        cursor.execute(command)
        urlaub_daten = cursor.fetchall()

        try:
            (urlaub_id, person_id, start_datum, end_datum, letzte_aenderung) = urlaub_daten[0]
            urlaub = Urlaub()
            urlaub.set_id(urlaub_id)
            urlaub.set_person_id(person_id)
            urlaub.set_start_date(start_datum)
            urlaub.set_end_date(end_datum)
            urlaub.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result = urlaub
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern urlaub_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result


    def delete(self, urlaub):
        """Löschen der Daten eines Urlaub-Objekts aus der Datenbank.

        :param Urlaub das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Urlaub WHERE urlaub_id={}".format(urlaub)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return urlaub



    def update(self, urlaub):
        """Wiederholtes Schreiben eines Urlaub-Objekts in die Datenbank.
        :param urlaub das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE Urlaub " + "SET person_id=%s, start_datum=%s, end_datum=%s, letzte_aenderung=%s WHERE urlaub_id=%s"
        data = (urlaub.get_person_id(), urlaub.get_start_date(), urlaub.get_end_date(), urlaub.get_letzte_aenderung(), urlaub.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()


if __name__ == '__main__':
    with UrlaubMapper() as mapper:
        result = mapper.find_all()