from bo.Projektarbeit import Projektarbeit
from db.Mapper import Mapper

class ProjektarbeitMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Zeitintervallbuchung")
        projektarbeit_daten = cursor.fetchall()

        for (zeit_id, projekt_id, person_id, aktivitaet_id, gearbeitete_zeit, letzte_aenderung) in projektarbeit_daten:
            projektarbeit = Projektarbeit()
            projektarbeit.set_id(zeit_id)
            projektarbeit.set_projekt_id(projekt_id)
            projektarbeit.set_person_id(person_id)
            projektarbeit.set_aktivitaet_id(aktivitaet_id)
            projektarbeit.set_gearbeitete_zeit(gearbeitete_zeit)
            projektarbeit.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(projektarbeit)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, projektarbeit):
        """ Einfügen eines neuen Projektarbeit-Objekts in die Datenbank.
        parameter: Projektarbeit Instanz, die in der Datenbank gespeichert werden soll
        return: Die Projektarbeitsinstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(zeit_id) AS maxid FROM Zeitintervall")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projektarbeit.set_id(maxid[0] + 1)


        """ Hier wird die Projektarbeit Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Zeitintervallbuchung (zeit_id, projekt_id, person_id, aktivitaet_id, gearbeitete_zeit, letzte_aenderung) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (projektarbeit.get_id(), projektarbeit.get_projekt_id(), projektarbeit.get_person_id(), projektarbeit.get_aktivitaet_id(),
                projektarbeit.get_gearbeitete_zeit(), projektarbeit.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projektarbeit

if __name__ == '__main__':
    with ProjektarbeitMapper() as mapper:
        result = mapper.find_all()