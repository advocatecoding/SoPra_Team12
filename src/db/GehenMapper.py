from bo.Gehen import Gehen
from db.Mapper import Mapper

"""
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
 * @author [Manuel Bräuninger](https://github.com/manu-br)
"""

class GehenMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """ Wir suchen alle Gehen """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Gehen")
        gehen_daten = cursor.fetchall()

        for (gehen_id, person_id, ende, letzte_aenderung) in gehen_daten:
            gehen = Gehen()
            gehen.set_id(gehen_id)
            gehen.set_person_id(person_id)
            gehen.set_ende(ende)
            gehen.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(gehen)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, gehen):
        """ Einfügen eines neuen Gehen-Objekts in die Datenbank.
        parameter: Gehen Instanz, die in der Datenbank gespeichert werden soll
        return: Die Geheninstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(gehen_id) AS maxid FROM Gehen")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            gehen.set_id(maxid[0] + 1)


        """ Hier wird die Gehen Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Gehen (gehen_id, person_id, ende, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (gehen.get_id(), gehen.get_person_id(), gehen.get_ende(), gehen.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return gehen

if __name__ == '__main__':
    with GehenMapper() as mapper:
        result = mapper.find_all()