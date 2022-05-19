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
from bo.Aktivitaet import Aktivitaet
from bo.Pause import Pause
from bo import BusinessObject as bo
from bo.Projekt import Projekt


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

    def update_person(self, person):
        person.set_letzte_aenderung()

        with PersonMapper() as mapper:
            return mapper.update(person)




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

if __name__ == '__main__':
    mitarbeiter1 = Person()
    mitarbeiter1.set_vorname("Mikasa")

    arbeitszeitkonto_von_mikasa = Arbeitszeitkonto()
    """ Das Arbeitszeitkonto von Mikasa  """
    arbeitszeitkonto_von_mikasa.set_owner(mitarbeiter1)

    aktivitaet1 = Aktivitaet()
    aktivitaet1.set_name("Kriegshammertitan aufhalten")

    zeitintervall_projekt = Zeitintervall()
    zeitintervall_projekt.set_projektlaufzeit(100)

    projekt1 = Projekt()
    projekt1.set_name("Marley erobern")
    projekt1.set_projektlaufzeit(100)

    #aktivität1.get_id()
    kommen = datetime.datetime(2022, 1,1,12,00)
    gehen = datetime.datetime(2022, 1,1, 14, 00)

    kommen1 = Kommen(kommen, aktivitaet1,mitarbeiter1)
    #kommen1.set_aktivitaet(aktivitaet1)
    #kommen1.set_person(mitarbeiter1)

    gehen1 = Gehen(gehen, aktivitaet1, mitarbeiter1)
    #gehen1.set_aktivitaet()

    ereignisbuchung1 = Ereignisbuchung(kommen1, gehen1)

    projektarbeit1 = Projektarbeit(ereignisbuchung1)
    pause1 = Pause(ereignisbuchung1)

    zeitintervall1 = Zeitintervall(ereignisbuchung1)
    zeitintervall1.set_id(1)

    #zeitintervall1.get_type(ereignisbuchung1)

    #pause1 = Pause()
    #pause1.set_zeitintervall(ereignisbuchung1)
    #zeitintervall1.set_zeitintervall(ereignisbuchung1)
    #projektarbeit1.set_zeitintervall(ereignisbuchung1)
    #zu_buchende_zeit = zeitintervall1.get_zeit()
    #zu_buchende_zeit = pause1.get_zeitintervall()
    zeitinervallbuchung1 = Zeitinverallbuchung(projektarbeit1)
    #zeitinervallbuchung1.set_zeitintervallbuchung(zu_buchende_zeit)
    zeitintervallbuchung2 = Zeitinverallbuchung(pause1)
    print(zeitintervallbuchung2.get_buchungsart())

    print(zeitinervallbuchung1.get_person().get_vorname())
    print(zeitinervallbuchung1.get_zeitintervall())
    print(zeitinervallbuchung1.get_aktivitaet().get_name())
    print(zeitinervallbuchung1.get_buchungsart())


"""
Szenario 1: Mitarbeiter bucht ein Zeitintervall 
arbeitsdauer = "2"

projektarbeit1 = Projektarbeit()
projektarbeit1.set_person(mitarbeiter1)
projektarbeit1.set_aktivitaet(aktivitaet1)
projektarbeit1.set_zeit(arbeitsdauer)

zeitintervallbuchung1 = Zeitinverallbuchung(projektarbeit1)
arbeitszeitkonto_von_mikasa.add_buchung(zeitintervallbuchung1)

Szenario 2: Mitarbeiter bucht ein Ereignis 
# 12 Uhr -> Timestamp
arbeits_start1 = datetime.datetime(2022,1,1,12,00)
arbeits_ende1 = datetime.datetime(2022,1,1,14,00)

kommen1 = Kommen(arbeits_start1)
kommen1.set_aktivitaet(aktivitaet1)
gehen1 = Gehen(arbeits_ende1)
gehen1.set_aktivitaet(aktivitaet1)

ereignisbuchung1 = Ereignisbuchung(kommen1)
ereignisbuchung1 = Ereignisbuchung(gehen1)
#ereignisbuchung1.add_buchung(kommen1)
#ereignisbuchung1.add_buchung(gehen1)
#print(ereignisbuchung1.get_ereignis_type())
print(ereignisbuchung1.get_startereignis())
#print(ereignisbuchung2.get_ereignis_type())


 Szenario 3: Mitarbeiter bucht ein 2 Ereignisse, welche als Zeitintervallbuchung gespeichert werden 
projektarbeit3 = Zeitintervall(kommen1, gehen1)
print(projektarbeit3.get_zeit())

Szenario 4: Projektdauer wird durch Zeitintervall festgelegt 
projektdauer = "430"
zeitintervall_projekt = Zeitintervall()
zeitintervall_projekt.set_projekt(projekt1)
zeitintervall_projekt.set_zeit(projektdauer)
projekt1.set_projektlaufzeit(zeitintervall_projekt)
print(projekt1.get_projektlaufzeit().get_zeit())

"""




















