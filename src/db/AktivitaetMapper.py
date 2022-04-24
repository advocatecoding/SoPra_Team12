from bo.Aktivitaet import Aktivitaet
from db.Mapper import Mapper
from bo.Projekt import Projekt

class AktivitaetMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        pass

    def find_aktivitaeten_by_projekt_id(self, projekt_id):
        #result = []
        aktivitaten = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT  projekt_id, bezeichnung, aktivitaet_id, letzte_aenderung FROM Aktivitaet INNER JOIN Aktivitaet_in_Projekt "
                       "WHERE aktivitaet_idd = aktivitaet_id AND projekt_id={}".format(projekt_id))
        aktivitaten_daten = cursor.fetchall()

        for (projekt_id, bezeichnung, aktivitaet_id, letzte_aenderung) in aktivitaten_daten:
            aktivitaet = Aktivitaet()
            aktivitaet.set_id(aktivitaet_id)
            aktivitaet.set_name(bezeichnung)
            aktivitaet.set_letzte_aenderung(letzte_aenderung)
            """ In "aktivitaeten" werden die Aktivitaeten-Objekte gespeichert """
            aktivitaten.append(aktivitaet)
            projekt = Projekt()
            projekt.set_id(projekt_id)
            projekt.set_aktivitaeten(aktivitaten)
            #result.append(projekt)
        print(projekt.get_aktivitaeten())
        self._cnx.commit()
        cursor.close()
        """ AktivitaetenObjekte werden zurückgegeben """
        return aktivitaten


if __name__ == '__main__':
    with AktivitaetMapper() as mapper:
        result = mapper.find_aktivitaeten_by_projekt_id(1)
        print(result)