from bo.Projektarbeit import Projektarbeit
from db.Mapper import Mapper

class ProjektarbeitMapper(Mapper):
    """
     * @author [Aykut Demir](https://github.com/AykutDemirr)
     * @author [Dennis Kühnberger](https://github.com/Dennis-248)
    """

    def __init__(self):
        super().__init__()

    def find_all(self):
        """ Wir suchen alle Projektarbeiten """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Projektarbeit")
        projektarbeit_daten = cursor.fetchall()

        for (projektarbeit_id, projekt_id, person_id, aktivitaet_id, start, ende, letzte_aenderung) in projektarbeit_daten:
            projektarbeit = Projektarbeit()
            projektarbeit.set_id(projektarbeit_id)
            projektarbeit.set_projekt_id(projekt_id)
            projektarbeit.set_person_id(person_id)
            projektarbeit.set_aktivitaet_id(aktivitaet_id)
            projektarbeit.set_start(start)
            projektarbeit.set_ende(ende)
            projektarbeit.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(projektarbeit)

        self._cnx.commit()
        cursor.close()

        return result

    def insert(self, projektarbeit):
        """ Einfügen eines neuen Projektarbeit-Objekts in die Datenbank.
        parameter: Projektarbeit Instanz, die in der Datenbank gespeichert werden soll
        return: Die Projektarbeitsinstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(projektarbeit_id) AS maxid FROM Projektarbeit")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projektarbeit.set_id(maxid[0] + 1)


        """ Hier wird die Projektarbeit Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Projektarbeit (projektarbeit_id, projekt_id, person_id, aktivitaet_id, start, ende, letzte_aenderung) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        data = (projektarbeit.get_id(),projektarbeit.get_projekt_id(), projektarbeit.get_person_id(), projektarbeit.get_aktivitaet_id(),
                projektarbeit.get_start(), projektarbeit.get_ende(), projektarbeit.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projektarbeit
