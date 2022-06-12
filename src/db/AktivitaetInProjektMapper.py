from db.Mapper import Mapper
from bo.AktivitaetenInProjekt import AktivitaetInProjekt
from bo.Projekt import Projekt
from bo.Aktivitaet import Aktivitaet


class AktivitaetInProjektMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Aktivitaet_in_Projekt")
        daten = cursor.fetchall()

        for (aktivitaet_idd, projekt_id, letzte_aenderung) in daten:
            aktivitaet1 = AktivitaetInProjekt()
            aktivitaet1.set_aktivitaet(aktivitaet_idd)
            aktivitaet1.set_projekt(projekt_id)
            aktivitaet1.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(aktivitaet1)
            print(result)

        self._cnx.commit()
        cursor.close()

        return result

    def find_aktivitaeten_by_projekt_id(self, projekt_id):
        # result = []
        aktivitaten = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT aktivitaet_idd, projekt_id, aktivitaet_in_projekt.letzte_aenderung FROM Aktivitaet INNER JOIN Aktivitaet_in_Projekt "
            "WHERE aktivitaet_idd = aktivitaet_id AND projekt_id={}".format(projekt_id))
        aktivitaten_daten = cursor.fetchall()

        for (aktivitaet_idd, projekt_id, letzte_aenderung) in aktivitaten_daten:
            aktivitaet = AktivitaetInProjekt()
            aktivitaet.set_aktivitaet(aktivitaet_idd)
            aktivitaet.set_projekt(projekt_id)
            aktivitaet.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            """ In "aktivitaeten" werden die Aktivitaeten-Objekte gespeichert """
            aktivitaten.append(aktivitaet)
            projekt = Projekt()
            projekt.set_id(projekt_id)
            projekt.set_aktivitaeten(aktivitaten)
            # result.append(projekt)
        print(projekt.get_aktivitaeten())
        self._cnx.commit()
        cursor.close()
        """ AktivitaetenObjekte werden zurückgegeben """
        return aktivitaten

    def insert(self, aktivitaet_in_projekt):

        cursor = self._cnx.cursor()

        """ Hier wird die Aktivität in der Projekt Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Aktivitaet_in_Projekt (aktivitaet_idd, projekt_id) VALUES (%s,%s)"
        data = (aktivitaet_in_projekt.get_aktivitaet(), aktivitaet_in_projekt.get_projekt())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return aktivitaet_in_projekt



    def delete(self, aktivitaet_idd, projekt_id):
        """Löschen der Daten einer Aktivität in Projekt Objekts aus der Datenbank.

        :param aktivitaet_idd und die projekt_id notwendig  das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Aktivität_in_Projekt WHERE aktivitaet_idd={0} AND projekt_id={1}".format(aktivitaet_idd, projekt_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return projekt_id









