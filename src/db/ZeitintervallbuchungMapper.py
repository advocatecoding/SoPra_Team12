from bo.Zeitintervallbuchung import Zeitinverallbuchung
from bo.Kommen import Kommen
from bo.Gehen import Gehen
from bo.Ereignisbuchung import Ereignisbuchung
from bo.Zeitintervall import Zeitintervall

from db.Mapper import Mapper


class ZeitintervallbuchungMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_by_projekt_id(self, id):
        """ Wir suchen die jeweilige Zeitintervallbuchung mithilfe der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Zeitintervallbuchung WHERE projekt_id={0}".format(id)
        cursor.execute(command)
        zb_daten = cursor.fetchall()

        try:
            for (zeit_id, projekt_id, person_id, aktivitaet_id, gearbeitete_zeit, letzte_aenderung) in zb_daten:
                buchung = Zeitinverallbuchung()
                buchung.set_id(zeit_id)
                buchung.set_projekt_id(projekt_id)
                buchung.set_person_id(person_id)
                buchung.set_aktivitaet_id(aktivitaet_id)
                buchung.set_zeitintervall(gearbeitete_zeit)
                buchung.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
                result.append(buchung)
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern aktivitaet_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result

    def insert(self, zeitintervallbuchung):
        """ Einfügen eines neuen Zeitintervallbuchungs-Objekts in die Datenbank.
        parameter: Zeitintervallbuchung Instanz die in der Datenbank gespeichert werden soll
        return: Die Zeitintervallbuchung Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(zeit_id) AS maxid FROM Zeitintervallbuchung ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            zeitintervallbuchung.set_id(maxid[0] + 1)

        """ Hier wird die Person Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO zeitintervallbuchung (zeit_id, projekt_id, person_id, aktivitaet_id, gearbeitete_zeit, letzte_aenderung) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (zeitintervallbuchung.get_id(), zeitintervallbuchung.get_projekt_id(),zeitintervallbuchung.get_person_id(),zeitintervallbuchung.get_aktivitaet(),
                zeitintervallbuchung.get_zeitintervall(), zeitintervallbuchung.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return zeitintervallbuchung
    
    def find_all(self):
        pass


