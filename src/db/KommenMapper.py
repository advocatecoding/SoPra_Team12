from bo.Kommen import Kommen
from db.Mapper import Mapper

class KommenMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Kommen")
        kommen_daten = cursor.fetchall()

        for (kommen_id, person_id, start_kommen, letzte_aenderung) in kommen_daten:
            kommen = Kommen()
            kommen.set_id(kommen_id)
            kommen.set_person_id(person_id)
            kommen.set_start_kommen(start_kommen)
            kommen.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(kommen)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, kommen):
        """ Einfügen eines neuen Kommen-Objekts in die Datenbank.
        parameter: Kommen Instanz, die in der Datenbank gespeichert werden soll
        return: Die Kommeninstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(kommen_id) AS maxid FROM Kommen")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            kommen.set_id(maxid[0] + 1)


        """ Hier wird die Kommen Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Kommen (kommen_id, person_id, start_kommen, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (kommen.get_id(), kommen.get_person_id(), kommen.get_start_kommen(), kommen.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return kommen

if __name__ == '__main__':
    with KommenMapper() as mapper:
        result = mapper.find_all()