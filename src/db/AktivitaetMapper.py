from bo.Aktivitaet import Aktivitaet
from db.Mapper import Mapper
from bo.Projekt import Projekt

class AktivitaetMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM aktivitaet")
        aktivitaet_daten = cursor.fetchall()

        for (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) in aktivitaet_daten:
            aktivitaet = Aktivitaet()
            aktivitaet.set_name(bezeichnung)
            aktivitaet.set_dauer(dauer)
            aktivitaet.set_kapazitaet(kapazitaet)
            aktivitaet.set_id(aktivitaet_id)
            aktivitaet.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(aktivitaet)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, id):
        """ Wir suchen die Aktivität mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Aktivitaet WHERE projekt_id={0}".format(id)
        cursor.execute(command)
        aktivitaet_daten = cursor.fetchall()

        try:
            (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) = aktivitaet_daten[0]
            aktivitaet = Aktivitaet()
            aktivitaet.set_name(bezeichnung)
            aktivitaet.set_dauer(dauer)
            aktivitaet.set_kapazitaet(kapazitaet)
            aktivitaet.set_id(aktivitaet_id)
            aktivitaet.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result = aktivitaet
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern aktivitaet_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result



    def delete(self, aktivitaet):
        """Löschen der Daten eines Aktivitäten-Objekts aus der Datenbank.

        :param Aktivität das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM aktivitaet WHERE aktivitaet_id={}".format(aktivitaet)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return aktivitaet


    def update(self, aktivitaet):
        cursor = self._cnx.cursor()

        command = "UPDATE aktivitaet " + "SET bezeichnung=%s, dauer=%s, kapazitaet=%s, letzte_aenderung=%s WHERE aktivitaet_id=%s"
        data = (aktivitaet.get_name(), aktivitaet.get_dauer(), aktivitaet.get_kapazitaet(), aktivitaet.get_letzte_aenderung(),
                aktivitaet.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()


    def insert(self, aktivitaet):
        """ Einfügen eines neuen Aktivitätetens-Objekts in die Datenbank.
        parameter: Aktivität Instanz die in der Datenbank gespeichert werden soll
        return: Die Akitivtät Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(aktivitaet_id) AS maxid FROM aktivitaet ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            aktivitaet.set_id(maxid[0] + 1)


        """ Hier wird die Aktivitäts Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO aktivitaet (aktivitaet_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (aktivitaet.get_id(), aktivitaet.get_name(), aktivitaet.get_dauer(), aktivitaet.get_kapazitaet(), aktivitaet.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return aktivitaet




if __name__ == '__main__':
    with AktivitaetMapper() as mapper:
        result = mapper.find_aktivitaeten_by_projekt_id(1)
        print(result)