from bo.Aktivitaet import Aktivitaet
from db.Mapper import Mapper
from bo.Projekt import Projekt

class AktivitaetMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Aktivitaet")
        aktivitaet_daten = cursor.fetchall()

        for (aktivitaet_id, projekt_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) in aktivitaet_daten:
            aktivitaet = Aktivitaet()
            aktivitaet.set_projektname(projekt_id)
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
        command = "SELECT * FROM Aktivitaet WHERE aktivitaet_id={0}".format(id)
        cursor.execute(command)
        aktivitaet_daten = cursor.fetchall()

        try:
            (aktivitaet_id, projekt_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) = aktivitaet_daten[0]
            aktivitaet = Aktivitaet()
            aktivitaet.set_projektname(projekt_id)
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

        command = "DELETE FROM Aktivitaet WHERE aktivitaet_id={}".format(aktivitaet)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return aktivitaet


    def update(self, aktivitaet):
        cursor = self._cnx.cursor()

        command = "UPDATE Aktivitaet " + "SET projekt_id=%s, bezeichnung=%s, dauer=%s, kapazitaet=%s, letzte_aenderung=%s WHERE aktivitaet_id=%s"
        data = (aktivitaet.get_projektname(), aktivitaet.get_name(), aktivitaet.get_dauer(), aktivitaet.get_kapazitaet(), aktivitaet.get_letzte_aenderung(),
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
        cursor.execute("SELECT MAX(aktivitaet_id) AS maxid FROM Aktivitaet ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            aktivitaet.set_id(maxid[0] + 1)


        """ Hier wird die Aktivitäts Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Aktivitaet (aktivitaet_id, projekt_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) VALUES (%s,%s,%s,%s,%s,%s)"
        data = (aktivitaet.get_id(), aktivitaet.get_projektname(), aktivitaet.get_name(), aktivitaet.get_dauer(), aktivitaet.get_kapazitaet(), aktivitaet.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return aktivitaet

    def find_all_aktivitaeten_by_projekt_id(self, projekt_id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Aktivitaet WHERE projekt_id={0}".format(projekt_id))
        projekt_daten = cursor.fetchall()

        for (aktivitaet_id, projekt_id, bezeichnung, dauer, kapazitaet, letzte_aenderung) in projekt_daten:
            projekt = Aktivitaet()
            projekt.set_projektname(projekt_id)
            projekt.set_name(bezeichnung)
            projekt.set_dauer(dauer)
            projekt.set_kapazitaet(kapazitaet)
            projekt.set_id(aktivitaet_id)
            projekt.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(projekt)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result


    def buchen_ansicht_frontend(self, person_id, projekt_id):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT Aktivitaet.aktivitaet_id, bezeichnung FROM Aktivitaet INNER JOIN Verkaufte_stunden_in_aktivitaet ON Aktivitaet.aktivitaet_id = Verkaufte_stunden_in_aktivitaet.aktivitaet_id  INNER JOIN Projekt ON Aktivitaet.projekt_id = Projekt.projekt_id WHERE Verkaufte_stunden_in_aktivitaet.person_id={0} AND Aktivitaet.projekt_id={1}".format(person_id,projekt_id))
        projekt_daten = cursor.fetchall()

        for (aktivitaet_id, bezeichnung) in projekt_daten:
            projekt = Aktivitaet()
            projekt.set_id(aktivitaet_id)
            projekt.set_name(bezeichnung)
            result.append(projekt)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result

