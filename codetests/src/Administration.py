#from bo.Projekt import Projekt
from bo.Aktivität import Aktivität
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

import datetime


class Administration(object):

    def __init__(self):
        pass

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
    print(zeitinervallbuchung1.get_aktivität())