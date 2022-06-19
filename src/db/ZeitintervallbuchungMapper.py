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