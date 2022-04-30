#from bo.Projekt import Projekt
from bo.Aktivitaet import Aktivitaet
from bo.Gehen import Gehen
from bo.Kommen import Kommen
from bo.Arbeitszeitkonto import Arbeitszeitkonto
from bo.Ereignisbuchung import Ereignisbuchung
from bo.Ereignis import Ereignis
from bo.Urlaub import Urlaub
from bo.Person import Person
from bo.Zeitintervallbuchung import Zeitinverallbuchung
from bo.Zeitintervall import Zeitintervall
from bo.Projektarbeit import Projektarbeit
from bo.Pause import Pause
from bo import BusinessObject as bo
from db.ProjektMapper import ProjektMapper
from db.PersonMapper import PersonMapper
from db.AktivitaetMapper import AktivitaetMapper

import datetime


class Administration(object):

    def __init__(self):
        pass

    def get_all_personen(self):
        """ Wir geben alle Personen aus """
        with PersonMapper() as mapper:
            return mapper.find_all()

    def get_all_projekte(self):
        """ Wir geben alle Personen aus """
        with ProjektMapper() as mapper:
            return mapper.find_all()
        
    def get_aktivitaeten_by_projekt_id(self, projekt_id):
        with AktivitaetMapper() as mapper:
            return mapper.find_aktivitaeten_by_projekt_id(projekt_id)

    def get_person_by_person_id(self, person_id):
        with PersonMapper() as mapper:
            #person = self.get_all_personen()
            return mapper.delete(person_id)
        """ if not (person is None):
                for person_id in person:
                    self.delete(person_id)
            """

    def create_person(self, vorname, nachname, mail_adresse, benutzername):
        """Eine Person anlegen."""

        person = Person()
        person.set_id(1211)
        person.set_vorname(vorname)
        person.set_nachname(nachname)
        person.set_mail_adresse(mail_adresse)
        person.set_benutzername(benutzername)
        person.set_urlaubstage(30)
        person.set_ueberstunden(0)
        """ Kein Attribut wird vergeben, da datetime.now() ausgeführt und gespeichert wird"""
        person.set_letzte_aenderung()

        with PersonMapper() as mapper:
            return mapper.insert(person)





""" Projekt test 
        if __name__ == '__main__':
            mitarbeiter1 = Person("Aykut")
            mitarbeiter1.set_id(1)
            mitarbeiter2 = Person("Talha")
            mitarbeiter2.set_id(2)

            projekt1 = Projekt("Autonomes fahren", "Mercedes")
            print(projekt1.get_name())
            projekt1.set_id(1)

            projekt1.set_team(mitarbeiter2, 30, mitarbeiter1, 15)
            print("Team:", projekt1.get_team())

            Aktivität1 = Aktivität("Pfeilen", 200, 14)
            Aktivität2 = Aktivität("Dressurreiten", 200, 14)

            projekt1.set_aktivitäten(Aktivität1, Aktivität2)
            print(projekt1.get_aktivitäten())
        """

"""

if __name__ == '__main__':
    mitarbeiter1 = Person("Harry")
    mitarbeiter1.set_id(1)
    mitarbeiter1.get_id()
    aktivität1 = Aktivität("UseCase erstellen")
    aktivität1.set_id(1)

    #aktivität1.get_id()
    kommen = datetime.datetime(2022, 1,1,12,00)
    gehen = datetime.datetime(2022, 1,1, 14, 00)
    kommen1 = Kommen(kommen)
    gehen1 = Gehen(gehen)
    ereignisbuchung1 = Ereignisbuchung(kommen1.get_start(), gehen1.get_end())
    zeitintervall1 = Zeitintervall()
    zeitintervall1.set_id(1)
    #zeitintervall1.get_type(ereignisbuchung1)
    projektarbeit1 = Projektarbeit()
    #pause1 = Pause()
    #pause1.set_zeitintervall(ereignisbuchung1)
    zeitintervall1.set_zeitintervall(ereignisbuchung1)
    #projektarbeit1.set_zeitintervall(ereignisbuchung1)
    zu_buchende_zeit = zeitintervall1.get_zeitintervall()
    #zu_buchende_zeit = pause1.get_zeitintervall()
    zeitinervallbuchung1 = Zeitinverallbuchung()
    zeitinervallbuchung1.set_zeitintervallbuchung(zu_buchende_zeit, mitarbeiter1.get_id(), aktivität1.get_id(), zeitintervall1.get_id())

    print(zeitinervallbuchung1.get_person())
    print(zeitinervallbuchung1.get_zeit())
    print(zeitinervallbuchung1.get_aktivität())"""