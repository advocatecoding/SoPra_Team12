from bo.Projekt import Projekt
from db.Mapper import Mapper

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
 * @author [Dennis Kühnberger](https://github.com/Dennis-248)
 * @author [Nicola Pany](https://github.com/NicolaPany)
 * @author [Talha Yildirim](https://github.com/talha16)
"""

class ProjektMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        """ Wir suchen alle Projekte """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT projektname, auftraggeber, projekt_id, person_id, letzte_aenderung from Projekt")
        projekt_daten = cursor.fetchall()

        for (projektname, auftraggeber, projekt_id,  person_id, letzte_aenderung) in projekt_daten:
            projekt = Projekt()
            projekt.set_name(projektname)
            projekt.set_auftraggeber(auftraggeber)
            projekt.set_id(projekt_id)
            projekt.set_projektleiter(person_id)
            projekt.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(projekt)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result


    def find_by_id(self, id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Projekt WHERE projekt_id={0}".format(id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        try:
            (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung) = projekt_daten[0]
            projekt = Projekt()
            projekt.set_name(projektname)
            projekt.set_auftraggeber(auftraggeber)
            projekt.set_id(projekt_id)
            projekt.set_projektleiter(person_id)
            projekt.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result = projekt
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern projekt_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        return result


    def insert(self, projekt):
        """ Einfügen eines neuen Projekt-Objekts in die Datenbank.
        parameter: Projekt Instanz die in der Datenbank gespeichert werden soll
        return: Die Projekt Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(projekt_id) AS maxid FROM Projekt ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            projekt.set_id(maxid[0] + 1)


        """ Hier wird die Projekt Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Projekt (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (projekt.get_id(), projekt.get_projektleiter(), projekt.get_name(), projekt.get_auftraggeber(), projekt.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return projekt



    def delete(self, projekt):
        """Löschen der Daten eines Projekt-Objekts aus der Datenbank.

        :param projekt das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Projekt WHERE projekt_id={}".format(projekt)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return projekt



    def update(self, projekt):
        """Wiederholtes Schreiben eines Projekt-Objekts in die Datenbank.
        :param projekt das Objekt, das in die DB geschrieben werden soll
        """
        cursor = self._cnx.cursor()

        command = "UPDATE Projekt " + "SET person_id=%s, projektname=%s, auftraggeber=%s, letzte_aenderung=%s WHERE projekt_id=%s"
        data = (projekt.get_projektleiter(), projekt.get_name(), projekt.get_auftraggeber(), projekt.get_letzte_aenderung(), projekt.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

    def projektleiter(self, person_id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result1 = []

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Projekt WHERE person_id={0}".format(person_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (projekt_id, person_id, projektname, auftraggeber, letzte_aenderung) in projekt_daten:
            projekt1 = Projekt()
            projekt1.set_id(projekt_id)
            projekt1.set_projektleiter(person_id)
            projekt1.set_name(projektname)
            projekt1.set_auftraggeber(auftraggeber)
            projekt1.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result1.append(projekt1)

        self._cnx.commit()
        cursor.close()
        return result1



    def find_projektnamen(self, person_id):
        """ Wir suchen den Projektnamen mit der jeweiligen ID """
        result1 = []

        cursor = self._cnx.cursor()
        command = "SELECT projektname, auftraggeber, Projekt.projekt_id FROM Mitarbeiter_in_Projekt JOIN Projekt ON Mitarbeiter_in_Projekt.projekt_id = Projekt.projekt_id JOIN Person ON Mitarbeiter_in_Projekt.person_idd = Person.person_id WHERE Person.person_id={}".format(person_id)

        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (projektname,auftraggeber,projekt_id) in projekt_daten:
            projekt1 = Projekt()
            projekt1.set_name(projektname)
            projekt1.set_auftraggeber(auftraggeber)
            projekt1.set_id(projekt_id)
            result1.append(projekt1)

        self._cnx.commit()
        cursor.close()
        return result1





if __name__ == '__main__':
    with ProjektMapper() as mapper:
        result = mapper.find_all()