from bo.Gehen import Gehen
from bo.Kommen import Kommen
from bo.Arbeitszeitkonto import Arbeitszeitkonto
from bo.Ereignisbuchung import Ereignisbuchung
from bo.Urlaub import Urlaub
from bo.Person import Person
from bo.Zeitintervallbuchung import Zeitinverallbuchung
from bo.Zeitintervall import Zeitintervall
from bo.Projektarbeit import Projektarbeit
from bo.Aktivitaet import Aktivitaet
from bo.Pause import Pause
from bo.Startbuchung import Startbuchung
from bo.Endbuchung import Endbuchung
from bo.AktivitaetenInProjekt import AktivitaetInProjekt
from bo.VerkaufteStundenInAktivitaet import VerkaufteStundenInAktivitaet

from db.ProjektMapper import ProjektMapper
from db.PersonMapper import PersonMapper
from db.AktivitaetMapper import AktivitaetMapper
from db.UrlaubMapper import UrlaubMapper
from bo.Projekt import Projekt
from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt
from db.MitarbeiterInProjektMapper import MitarbeiterInProjektMapper
from db.AktivitaetInProjektMapper import AktivitaetInProjektMapper
from db.VerkaufteStundenInAktivitaetMapper import VerkaufteStundenInAktivitaetMapper
import datetime


class Administration(object):

    def __init__(self):
        pass

    """Person"""
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

    def get_all_personen(self):
        """ Wir geben alle Personen aus """
        with PersonMapper() as mapper:
            return mapper.find_all()

    def get_person_by_id(self, person_id):
        """ Wir geben die Person mit der angegebenen ID zurück """
        with PersonMapper() as mapper:
            return mapper.find_by_id(person_id)

    def get_person_by_benutzername(self, benutzername):
        """ Wir geben die Person mit dem angegebenen Benutzernamen zurück """
        with PersonMapper() as mapper:
            return mapper.find_by_benutzername(benutzername)

    def delete_person_by_person_id(self, person_id):
        with PersonMapper() as mapper:
            #person = self.get_all_personen()
            return mapper.delete(person_id)
        """ if not (person is None):
                for person_id in person:
                    self.delete(person_id)
        """

    def update_person(self, person):
        person.set_letzte_aenderung()

        with PersonMapper() as mapper:
            return mapper.update(person)


    """Projekt"""
    def create_projekt(self, projektleiter, projektname, auftraggeber):
            """Ein Projekt anlegen."""
            projekt = Projekt()
            projekt.set_id(1211)
            projekt.set_projektleiter(projektleiter)
            projekt.set_name(projektname)
            projekt.set_auftraggeber(auftraggeber)
            """ Kein Attribut wird vergeben, da datetime.now() ausgeführt und gespeichert wird"""
            projekt.set_letzte_aenderung()

            with ProjektMapper() as mapper:
                return mapper.insert(projekt)

    def get_all_projekte(self):
        """ Wir geben alle Projekte aus """
        with ProjektMapper() as mapper:
            return mapper.find_all()

    def delete_projekt_by_id(self, projekt_id):
        with ProjektMapper() as mapper:
            return mapper.delete(projekt_id)

    def update_projekt(self, projekt):
        projekt.set_letzte_aenderung()

        with ProjektMapper() as mapper:
            return mapper.update(projekt)


    """Aktivität"""
    def create_aktivitaet(self, bezeichnung, dauer, kapazitaet):
        """Eine Aktivität anlegen."""

        aktivitaet = Aktivitaet()
        aktivitaet.set_id(1211)
        aktivitaet.set_name(bezeichnung)
        aktivitaet.set_dauer(dauer)
        aktivitaet.set_kapazitaet(kapazitaet)
        """ Kein Attribut wird vergeben, da datetime.now() ausgeführt und gespeichert wird"""
        aktivitaet.set_letzte_aenderung()

        with AktivitaetMapper() as mapper:
            return mapper.insert(aktivitaet)

    def get_all_aktivitaeten(self):
        """ Wir geben alle Aktivitäten aus """
        with AktivitaetMapper() as mapper:
            return mapper.find_all()

    def get_aktivitaet_by_id(self, aktivitaet_id):
        """ Wir geben die Aktivität mit der angegebenen ID zurück """
        with AktivitaetMapper() as mapper:
            return mapper.find_by_id(aktivitaet_id)

    def get_aktivitaeten_by_projekt_id(self, projekt_id):
        with AktivitaetInProjektMapper() as mapper:
            return mapper.find_aktivitaeten_by_projekt_id(projekt_id)

    def delete_aktivitaet_by_aktivitaet_id(self, aktivitaet_id):
        with AktivitaetMapper() as mapper:
            return mapper.delete(aktivitaet_id)

    def update_aktivitaet(self, aktivitaet):
        aktivitaet.set_letzte_aenderung()

        with AktivitaetMapper() as mapper:
            return mapper.update(aktivitaet)

    def create_aktivitaet_in_projekt(self, aktivitaet, projekt):
            """Aktivität in Projekt anlegen."""
            aktivitaet_in_projekt = AktivitaetInProjekt()
            aktivitaet_in_projekt.set_aktivitaet(aktivitaet)
            aktivitaet_in_projekt.set_projekt(projekt)
            aktivitaet_in_projekt.set_letzte_aenderung()

            with AktivitaetInProjektMapper() as mapper:
                return mapper.insert(aktivitaet_in_projekt)

    @property
    def get_all_aktivitaet_in_projekt(self):
        """Wir geben alle Aktivitäten in einem Projekt aus"""
        with AktivitaetInProjektMapper() as mapper:
            return mapper.find_all()

    def get_aktivitaet_in_projekt_by_id(self, projekt_id):
        """ Wir geben die Aktivitäten der Projekte mit der angegebenen ID zurück """
        with AktivitaetInProjektMapper() as mapper:
            return mapper.find_by_id(projekt_id)

    def delete_aktivitaet_in_projekt_by_id(self, aktivitaet_idd, projekt_id):
        """Löschen einer Aktivitaet-Instanz mit der Projekt Id"""
        with AktivitaetInProjektMapper() as mapper:
            return mapper.delete(aktivitaet_idd, projekt_id)


    """Urlaub"""
    def create_urlaub(self, person_id, start_datum, end_datum):
        """Urlaub anlegen."""

        urlaub = Urlaub()
        urlaub.set_id(1211)
        urlaub.set_person_id(person_id)
        urlaub.set_start_date(start_datum)
        urlaub.set_end_date(end_datum)
        urlaub.set_letzte_aenderung()
        """ Kein Attribut wird vergeben, da datetime.now() ausgeführt und gespeichert wird"""

        with UrlaubMapper() as mapper:
            return mapper.insert(urlaub)

    def get_all_urlaub(self):
        """Wir geben Urlaub von allen aus"""
        with UrlaubMapper() as mapper:
            return mapper.find_all()

    def get_urlaub_by_id(self, urlaub_id):
        """ Wir geben den Urlaub mit der angegebenen ID zurück """
        with UrlaubMapper() as mapper:
            return mapper.find_by_id(urlaub_id)

    def delete_urlaub_by_urlaub_id(self, urlaub_id):
        with UrlaubMapper() as mapper:
            return mapper.delete(urlaub_id)

    def update_urlaub(self, urlaub):
        urlaub.set_letzte_aenderung()

        with UrlaubMapper() as mapper:
            return mapper.update(urlaub)

    """Mitarbeiter"""
    def create_mitarbeiter_in_projekt(self, mitarbeiter, projekt, verkaufte_stunden):
            """Mitarbeiter in Projekt anlegen."""
            mitarbeiter_in_projekt = MitarbeiterInProjekt()
            mitarbeiter_in_projekt.set_person(mitarbeiter)
            mitarbeiter_in_projekt.set_projekt(projekt)
            mitarbeiter_in_projekt.set_verkaufte_stunden(verkaufte_stunden)
            mitarbeiter_in_projekt.set_letzte_aenderung()

            with MitarbeiterInProjektMapper() as mapper:
                return mapper.insert(mitarbeiter_in_projekt)

    def get_all_mitarbeiter_in_projekt(self):
        """Wir geben alle Mitarbeiter in einem Projekt aus"""
        with MitarbeiterInProjektMapper() as mapper:
            return mapper.find_all()

    def get_mitarbeiter_in_projekt_by_idd(self, person_idd):
        """ Wir geben die Mitarbeiter der jeweiligen Projekte mit der angegebenen ID zurück """
        with MitarbeiterInProjektMapper() as mapper:
            return mapper.find_by_id(person_idd)

    def get_person_by_person_id_and_projekt_by_projekt_id(self, person_idd, projekt_id):
        with MitarbeiterInProjektMapper() as mapper:
            return mapper.delete(person_idd, projekt_id)

    def get_projekt_by_id(self, projekt_id):
        """ Wir geben die Projekte mit der angegebenen ID zurück """
        with ProjektMapper() as mapper:
            return mapper.find_by_id(projekt_id)

    def get_all_projekte_by_mitarbeiter_id(self, person_id):
        """ Wir geben die Projekte mit der angegebenen ID zurück """
        with ProjektMapper() as mapper:
            return mapper.find_projektnamen(person_id)






    def projekte_by_projektleiter(self, projektleiter):
        with ProjektMapper() as mapper:
            return mapper.projektleiter(projektleiter)


    def get_all_verkaufte_stunden_in_aktivitaet(self):
        """ Wir geben alle verkaufte_stunden_in_aktivitaet aus """
        with VerkaufteStundenInAktivitaetMapper() as mapper:
            return mapper.find_all()


    def create_verkaufte_stunden_in_aktivitaet(self, mitarbeiter, aktivitaet, gebuchte_stunden):
            """verkaufte_stunden_in_aktivitaet anlegen."""
            averkaufte_stunden = VerkaufteStundenInAktivitaet()
            averkaufte_stunden.set_person(mitarbeiter)
            averkaufte_stunden.set_aktivitaet(aktivitaet)
            averkaufte_stunden.set_gebuchte_stunden(gebuchte_stunden)
            averkaufte_stunden.set_letzte_aenderung()

            with VerkaufteStundenInAktivitaetMapper() as mapper:
                return mapper.insert(averkaufte_stunden)


    def get_sollzeit_by_id(self, projekt_id):
        with VerkaufteStundenInAktivitaetMapper() as mapper:
            return mapper.find_by_id(projekt_id)


    def get_mitarbeiteransicht_by_id(self, projekt_id):
        with VerkaufteStundenInAktivitaetMapper() as mapper:
            return mapper.mitarbeiteransicht_find_by_id(projekt_id)


    def get_persoenliche_mitarbeiteransicht_by_id(self, person_id):
        with VerkaufteStundenInAktivitaetMapper() as mapper:
            return mapper.persoenliche_mitarbeiteransicht_find_by_id(person_id)



    """ Buchungen """
    def create_startbuchung(self, zeitpunkt, person):
        """ Startbuchung für Aktivitäten oder Pausen anlegen """
        startbuchung = Startbuchung()
        startbuchung.set_id(1211)
        startbuchung.set_zeitpunkt(zeitpunkt)
        startbuchung.set_person(person)

    def create_ereignisbuchung(self, startereignis, endereignis):
        ereignisbuchung = Ereignisbuchung(startereignis, endereignis)
        ereignisbuchung.set_id(1211)

    def create_zeitintervall(self, ereignisbuchung):

        zeitintervall = Zeitintervall()


if __name__ == '__main__':

    mitarbeiter1 = Person()
    mitarbeiter1.set_vorname("Mikasa")

    aktivitaet1 = Aktivitaet()
    aktivitaet1.set_name("Kriegshammertitan aufhalten")

    zeitintervall_projekt = Zeitintervall()

    projekt1 = Projekt()
    projekt1.set_name("Marley erobern")
    #projekt1.set_projektlaufzeit(zeitintervall_projekt.get_zeitintervall())
    #projekt1.set_projektlaufzeit(100)

    #aktivität1.get_id()
    startzeit = datetime.datetime(2022,1,1,12,00)
    endzeit = datetime.datetime(2022,1,1,20,00)

    buchungstart = datetime.datetime(2022,1,1,12,00)
    buchungende = datetime.datetime(2022,1,1,15,00)

    kommen1 = Kommen(startzeit,mitarbeiter1)
    gehen1 = Gehen(endzeit, mitarbeiter1)

    startbuchung1 = Startbuchung(buchungstart, mitarbeiter1)
    endbuchung1 = Endbuchung(buchungende, mitarbeiter1)


    """ Ereignisbuchung extrahiert die Daten von Kommen und Gehen (Objekte werden nicht mitgeschleppt) """
    ereignisbuchung1 = Ereignisbuchung(kommen1, gehen1)

    projektarbeit1 = Projektarbeit(ereignisbuchung1)
    projektarbeit1.set_id(1)

    """ Fall 2: Pause durch 2 Ereignisse buchen """
    pause1 = Pause(ereignisbuchung1)
    pause1.set_id(1)

    zeitinervallbuchung1 = Zeitinverallbuchung(projektarbeit1, aktivitaet1)
    zeitintervallbuchung2 = Zeitinverallbuchung(pause1, aktivitaet1)

    """ Fall 3: Pause direkt durch Zeitintervall buchen (ohne Ereignisse) """
    pause2 = Pause()
    pause2.set_zeitintervall(0.2)
    pause2.set_person(mitarbeiter1)
    pause2.set_aktivitaet(aktivitaet1)
    
    zeitintervallbuchung3 = Zeitinverallbuchung(pause2, aktivitaet1)
    
    """ Projektarbeit von 7h """
    projektarbeit2 = Projektarbeit()
    projektarbeit2.set_zeitintervall(7)
    projektarbeit2.set_person(mitarbeiter1)
    projektarbeit2.set_aktivitaet(aktivitaet1)
    
    
    zeitintervallbuchung4 = Zeitinverallbuchung(projektarbeit2, aktivitaet1)

    arbeitszeitkonto_von_mikasa = Arbeitszeitkonto(mitarbeiter1)
    """ Das Arbeitszeitkonto von Mikasa  """
    arbeitszeitkonto_von_mikasa.add_buchung(zeitinervallbuchung1)
    arbeitszeitkonto_von_mikasa.add_buchung(zeitintervallbuchung3)
    arbeitszeitkonto_von_mikasa.add_buchung(zeitintervallbuchung4)
