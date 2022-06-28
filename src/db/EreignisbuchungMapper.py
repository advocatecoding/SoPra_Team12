from bo.Ereignisbuchung import Ereignisbuchung
from db.Mapper import Mapper

class EreignisbuchungMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Ereignisbuchung")
        ereignisbuchung_daten = cursor.fetchall()

        for (ereignisbuchung_id, kommen_id, gehen_id, letzte_aenderung) in ereignisbuchung_daten:
            ereignisbuchung = Ereignisbuchung()
            ereignisbuchung.set_id(ereignisbuchung_id)
            ereignisbuchung.set_kommen_id(kommen_id)
            ereignisbuchung.set_gehen_id(gehen_id)
            ereignisbuchung.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(ereignisbuchung)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, ereignisbuchung):
        """ Einfügen eines neuen Ereignisbuchung-Objekts in die Datenbank.
        parameter: Ereignisbuchung Instanz, die in der Datenbank gespeichert werden soll
        return: Die Ereignisbuchunginstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(ereignisbuchung_id) AS maxid FROM Ereignisbuchung")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            ereignisbuchung.set_id(maxid[0] + 1)


        """ Hier wird die Ereignisbuchung Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Ereignisbuchung (ereignisbuchung_id, kommen_id, gehen_id, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (ereignisbuchung.get_id(), ereignisbuchung.get_kommen_id(), ereignisbuchung.get_gehen_id(), ereignisbuchung.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return ereignisbuchung

if __name__ == '__main__':
    with EreignisbuchungMapper() as mapper:
        result = mapper.find_all()