from bo.Person import Person
from db.Mapper import Mapper

class PersonMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT person_id, vorname, nachname, mail_adresse, benutzername, urlaubstage, ueberstunden from Person")
        person_daten = cursor.fetchall()

        for (person_id, vorname, nachname,  mail_adresse, benutzername, urlaubstage, ueberstunden) in person_daten:
            person = Person()
            person.set_vorname(vorname)
            person.set_nachname(nachname)
            person.set_benutzername(benutzername)
            person.set_mail_adresse(mail_adresse)
            person.set_urlaubstage(urlaubstage)
            person.set_ueberstunden(ueberstunden)
            person.set_id(person_id)
            result.append(person)
            print(result)

        self._cnx.commit()
        cursor.close()

        return result

""" Tesing """
if __name__ == '__main__':
    with PersonMapper() as mapper:
        result = mapper.find_all()
