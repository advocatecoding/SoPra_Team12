from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt
from db.Mapper import Mapper
from bo.Projekt import Projekt


class MitarbeiterInProjektMapper(Mapper):

    def __init__(self):
        super().__init__()


    def find_all(self):
        """ Wir suchen alle Mitarbeiter in Projekten """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Mitarbeiter_in_Projekt")
        daten = cursor.fetchall()

        for (person_idd, projekt_id, verkaufte_stunden, letzte_aenderung) in daten:
            mitarbeiter1 = MitarbeiterInProjekt()
            mitarbeiter1.set_person(person_idd)
            mitarbeiter1.set_projekt(projekt_id)
            mitarbeiter1.set_verkaufte_stunden(verkaufte_stunden)
            mitarbeiter1.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(mitarbeiter1)
            print(result)

        self._cnx.commit()
        cursor.close()

        return result

    def find_by_id(self, person_idd):
        """ Wir suchen den Mitarbeiter in Projekt mit der jeweiligen Person ID """
        # result = []
        personl = []
        cursor = self._cnx.cursor()
        cursor.execute(
            "SELECT person_idd, projekt_id, verkaufte_stunden, Mitarbeiter_in_Projekt.letzte_aenderung FROM Person INNER JOIN Mitarbeiter_in_Projekt "
            "ON person_idd = person_id AND person_idd={}".format(person_idd))
        person_daten = cursor.fetchall()

        for (person_idd, projekt_id, verkaufte_stunden, letzte_aenderung) in person_daten:
            person = MitarbeiterInProjekt()
            person.set_person(person_idd)
            person.set_projekt(projekt_id)
            person.set_verkaufte_stunden(verkaufte_stunden)
            person.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            """ In "person" werden die MitarbeiterInProjekt-Objekte gespeichert """
            personl.append(person)
            projekt = Projekt()
            projekt.set_id(projekt_id)
            # result.append(projekt)
        print(projekt.get_aktivitaeten())
        self._cnx.commit()
        cursor.close()
        """ AktivitaetenObjekte werden zurückgegeben """
        return personl

    """ letzte Änderung noch hinzufügen, in der Datenbank. Gleiches Problem wie bei person_id und person_idd"""


    def insert(self, mitarbeiter_in_projekt):
        """ Einfügen eines neuen Mitarbeiter_in_Projekt-Objekts in die Datenbank.
        parameter: Mitarbeiter_in_Projekt Instanz die in der Datenbank gespeichert werden soll
        return: Die Mitarbeiter_in_Projekt Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()

        """ Hier wird die Mitarbeiter in Projekt Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Mitarbeiter_in_Projekt (person_idd, projekt_id, verkaufte_stunden, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (mitarbeiter_in_projekt.get_person(), mitarbeiter_in_projekt.get_projekt(), mitarbeiter_in_projekt.get_verkaufte_stunden(), mitarbeiter_in_projekt.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return mitarbeiter_in_projekt



    def delete(self, person_idd, projekt_id):
        """Löschen der Daten eines Mitarbeiter in Projekt Objekts aus der Datenbank.

        :param person_id und die projekt_id notwendig  das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Mitarbeiter_in_Projekt WHERE person_idd={0} AND projekt_id={1}".format(person_idd, projekt_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return person_idd









