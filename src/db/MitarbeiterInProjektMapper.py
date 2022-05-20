from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt
from db.Mapper import Mapper

class MitarbeiterInProjektMapper(Mapper):

    def __init__(self):
        super().__init__()


    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM mitarbeiter_in_projekt")
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



    def insert(self, mitarbeiter_in_projekt):

        cursor = self._cnx.cursor()

        """ Hier wird die Mitarbeiter in Projekt Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO mitarbeiter_in_projekt (person_idd, projekt_id, verkaufte_stunden, letzte_aenderung) VALUES (%s,%s,%s,%s)"
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

        command = "DELETE FROM mitarbeiter_in_projekt WHERE person_idd={0} AND projekt_id={1}".format(person_idd,projekt_id)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return person_idd









