from bo.Urlaub import Urlaub
from db.Mapper import Mapper

class UrlaubMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * from Urlaub")
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
        cursor.execute("SELECT MAX(urlaub_id) AS maxid FROM urlaub")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            urlaub.set_id(maxid[0] + 1)


        """ Hier wird die Urlaub Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO urlaub (urlaub_id, person_id, start_datum, end_datum, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (urlaub.get_id(), urlaub.get_person_id(), urlaub.get_start_date(), urlaub.get_end_date(),urlaub.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return urlaub



    def delete(self, urlaub):
        """Löschen der Daten eines Urlaub-Objekts aus der Datenbank.

        :param Urlaub das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM urlaub WHERE urlaub_id={}".format(urlaub)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return urlaub



    def update(self, urlaub):
        cursor = self._cnx.cursor()

        command = "UPDATE urlaub " + "SET person_id=%s, start_datum=%s, end_datum=%s, letzte_aenderung=%s WHERE urlaub_id=%s"
        data = (urlaub.get_person_id(), urlaub.get_start_date(), urlaub.get_end_date(), urlaub.get_letzte_aenderung(), urlaub.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()










if __name__ == '__main__':
    with UrlaubMapper() as mapper:
        result = mapper.find_all()