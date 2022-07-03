from bo.Mitarbeiterinprojekt import MitarbeiterInProjekt
from db.Mapper import Mapper
from bo.VerkaufteStundenInAktivitaet import VerkaufteStundenInAktivitaet
from bo.SollZeit import Sollzeit
from bo.MitarbeiterAnsicht import MitarbeiterAnsicht

"""
 * @author [Aykut Demir](https://github.com/AykutDemirr)
"""

class VerkaufteStundenInAktivitaetMapper(Mapper):

    def __init__(self):
        super().__init__()


    def find_all(self):
        """ Wir suchen alle Verkaufte Stunden in Aktivität """
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Verkaufte_stunden_in_aktivitaet")
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
        command = "INSERT INTO Verkaufte_stunden_in_aktivitaet (aktivitaet_id, person_id, gebuchte_stunden, letzte_aenderung) VALUES (%s,%s,%s,%s)"
        data = (averkaufte_stunden.get_aktivitaet(), averkaufte_stunden.get_person(), averkaufte_stunden.get_gebuchte_stunden(), averkaufte_stunden.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return averkaufte_stunden



    def find_by_id(self, projekt_id):
        """ Wir suchen die Verkaufte Stunden in Aktivität mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT gebuchte_stunden, bezeichnung FROM Verkaufte_stunden_in_aktivitaet INNER JOIN Person ON Verkaufte_stunden_in_aktivitaet.person_id = Person.person_id INNER JOIN Zeitintervallbuchung ON Verkaufte_stunden_in_aktivitaet.aktivitaet_id = Zeitintervallbuchung.aktivitaet_id INNER JOIN Aktivitaet ON Verkaufte_stunden_in_aktivitaet.aktivitaet_id = Aktivitaet.aktivitaet_id WHERE Zeitintervallbuchung.projekt_id={0} GROUP BY Zeitintervallbuchung.aktivitaet_id, vorname ORDER BY bezeichnung, vorname ASC;".format(projekt_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (gebuchte_stunden,bezeichnung) in projekt_daten:
            projekt = Sollzeit()
            projekt.set_gebuchte_stunden(gebuchte_stunden)
            projekt.set_bezeichnung(bezeichnung)
            result.append(projekt)


        self._cnx.commit()
        cursor.close()
        return result




    def mitarbeiteransicht_find_by_id(self, projekt_id):
        """ Wir suchen die Mitarbeiteransicht mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT vorname, nachname, bezeichnung, SUM(gearbeitete_zeit) FROM Zeitintervallbuchung INNER JOIN Person ON Zeitintervallbuchung.person_id = Person.person_id INNER JOIN Aktivitaet ON Zeitintervallbuchung.aktivitaet_id = Aktivitaet.aktivitaet_id WHERE Zeitintervallbuchung.projekt_id={0} GROUP BY bezeichnung, vorname ORDER BY bezeichnung, vorname ASC;".format(projekt_id)
        cursor.execute(command)
        projekt_daten = cursor.fetchall()

        for (vorname, nachname, bezeichnung, gearbeitete_zeit) in projekt_daten:
            projekt = MitarbeiterAnsicht()
            projekt.set_person(vorname)
            projekt.set_nachname(nachname)
            projekt.set_aktivitaet(bezeichnung)
            projekt.set_gearbeitete_zeit(gearbeitete_zeit)
            result.append(projekt)


        self._cnx.commit()
        cursor.close()
        return result




    def persoenliche_mitarbeiteransicht_find_by_id(self, person_id):
        """ Wir suchen die persönliche Mitarbeiteransicht mit der jeweiligen ID """
        result = []

        cursor = self._cnx.cursor()
        command = "SELECT vorname, projektname, bezeichnung, SUM(gearbeitete_zeit) FROM Zeitintervallbuchung INNER JOIN Person ON Zeitintervallbuchung.person_id = Person.person_id INNER JOIN Projekt ON Zeitintervallbuchung.projekt_id = Projekt.projekt_id INNER JOIN Aktivitaet ON Zeitintervallbuchung.aktivitaet_id = Aktivitaet.aktivitaet_id WHERE Zeitintervallbuchung.person_id={0} GROUP BY bezeichnung ORDER BY projektname ASC".format(person_id)
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