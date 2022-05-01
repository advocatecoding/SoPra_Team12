from bo.Person import Person
from db.Mapper import Mapper

class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Person")
        person_daten = cursor.fetchall()

        for (person_id, vorname, nachname,  mail_adresse, benutzername, urlaubstage, ueberstunden, letzte_aenderung) in person_daten:
            person = Person()
            person.set_vorname(vorname)
            person.set_nachname(nachname)
            person.set_benutzername(benutzername)
            person.set_mail_adresse(mail_adresse)
            person.set_urlaubstage(urlaubstage)
            person.set_ueberstunden(ueberstunden)
            person.set_id(person_id)
            person.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(person)
            print(result)

        self._cnx.commit()
        cursor.close()

        return result



    def delete(self, person):
        """Löschen der Daten eines Person-Objekts aus der Datenbank.

        :param person das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM person WHERE person_id={}".format(person)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return person

    def insert(self, person):
        """ Einfügen eines neuen Person-Objekts in die Datenbank.
        parameter: Person Instanz die in der Datenbank gespeichert werden soll
        return: Die Person Instanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(person_id) AS maxid FROM person ")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            person.set_id(maxid[0] + 1)


        """ Hier wird die Person Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO person (person_id, vorname, nachname, mail_adresse, benutzername, urlaubstage, ueberstunden, letzte_aenderung) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
        data = (person.get_id(), person.get_vorname(), person.get_nachname(), person.get_mail_adresse(), person.get_benutzername(), person.get_urlaubstage(), person.get_ueberstunden(), person.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return person




""" Tesing """
if __name__ == '__main__':
    with PersonMapper() as mapper:
        result = mapper.find_all()
