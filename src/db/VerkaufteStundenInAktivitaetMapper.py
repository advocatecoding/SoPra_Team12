from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt
from db.Mapper import Mapper
from bo.VerkaufteStundenInAktivitaet import VerkaufteStundenInAktivitaet
from bo.SollZeit import Sollzeit
from bo.MitarbeiterAnsicht import MitarbeiterAnsicht


class VerkaufteStundenInAktivitaetMapper(Mapper):

    def __init__(self):
        super().__init__()


    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM verkaufte_stunden_in_aktivitaet")
        person_daten = cursor.fetchall()

        for (aktivitaet_id, person_id, gebuchte_stunden, letzte_aenderung) in person_daten:
            agebuchte_stunden = VerkaufteStundenInAktivitaet()
            agebuchte_stunden.set_aktivitaet(aktivitaet_id)
            agebuchte_stunden.set_person(person_id)
            agebuchte_stunden.set_gebuchte_stunden(gebuchte_stunden)
            agebuchte_stunden.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(agebuchte_stunden)
            print(result)

        self._cnx.commit()
        cursor.close()
        print(result)
        return result




    def insert(self, averkaufte_stunden):

        cursor = self._cnx.cursor()

        """ Hier wird die verkaufte_stunden_in_Aktivität Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO verkaufte_stunden_in_aktivitaet (aktivitaet_id, person_id, gebuchte_stunden, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (averkaufte_stunden.get_aktivitaet(), averkaufte_stunden.get_person(), averkaufte_stunden.get_gebuchte_stunden(), averkaufte_stunden.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return averkaufte_stunden



    def find_by_id(self, projekt_id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "select gebuchte_stunden FROM verkaufte_stunden_in_aktivitaet Inner Join Person on verkaufte_stunden_in_aktivitaet.person_id = person.person_id Inner Join Zeitintervallbuchung on verkaufte_stunden_in_aktivitaet.aktivitaet_id = Zeitintervallbuchung.aktivitaet_id where zeitintervallbuchung.projekt_id={0} group by zeitintervallbuchung.aktivitaet_id, vorname order by vorname ASC;".format(projekt_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (gebuchte_stunden) in projekt_daten:
            projekt = Sollzeit()
            projekt.set_gebuchte_stunden(gebuchte_stunden)
            result.append(projekt)


        self._cnx.commit()
        cursor.close()
        return result




    def mitarbeiteransicht_find_by_id(self, projekt_id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "select vorname, bezeichnung, SUM(gearbeitete_zeit) FROM zeitintervallbuchung Inner Join Person on zeitintervallbuchung.person_id = person.person_id Inner Join Aktivitaet on zeitintervallbuchung.aktivitaet_id = Aktivitaet.aktivitaet_id where zeitintervallbuchung.projekt_id={0} group by bezeichnung, vorname order by vorname ASC;".format(projekt_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (vorname, bezeichnung, gearbeitete_zeit) in projekt_daten:
            projekt = MitarbeiterAnsicht()
            projekt.set_person(vorname)
            projekt.set_aktivitaet(bezeichnung)
            projekt.set_gearbeitete_zeit(gearbeitete_zeit)
            result.append(projekt)


        self._cnx.commit()
        cursor.close()
        return result




    def persoenliche_mitarbeiteransicht_find_by_id(self, person_id):
        """ Wir suchen das Projekt mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = " select vorname, projektname, bezeichnung, SUM(gearbeitete_zeit) FROM zeitintervallbuchung Inner Join Person on zeitintervallbuchung.person_id = person.person_id Inner Join Projekt on zeitintervallbuchung.projekt_id = projekt.projekt_id Inner Join Aktivitaet on zeitintervallbuchung.aktivitaet_id = Aktivitaet.aktivitaet_id where zeitintervallbuchung.person_id={0} group by bezeichnung order by projektname ASC;".format(person_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (vorname, projektname, bezeichnung, gearbeitete_zeit) in projekt_daten:
            projekt = MitarbeiterAnsicht()
            projekt.set_person(vorname)
            projekt.set_projekt(projektname)
            projekt.set_aktivitaet(bezeichnung)
            projekt.set_gearbeitete_zeit(gearbeitete_zeit)
            result.append(projekt)


        self._cnx.commit()
        cursor.close()
        return result