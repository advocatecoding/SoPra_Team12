from bo.Pause import Pause
from db.Mapper import Mapper

class PauseMapper(Mapper):

    def __init__(self):
        super().__init__()

    def find_all(self):
        result = []
        cursor = self._cnx.cursor()
        cursor.execute("SELECT * FROM Pause")
        pause_daten = cursor.fetchall()

        for (pause_id, person_id, start_pause, ende_pause, letzte_aenderung) in pause_daten:
            pause = Pause()
            pause.set_id(pause_id)
            pause.set_person_id(person_id)
            pause.set_start_pause(start_pause)
            pause.set_ende_pause(ende_pause)
            pause.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result.append(pause)
        """
        for i in result:
            print(i.get_name())
        """
        self._cnx.commit()
        cursor.close()

        return result


    def insert(self, pause):
        """ Einfügen eines neuen Pausen-Objekts in die Datenbank.
        parameter: Pausen Instanz, die in der Datenbank gespeichert werden soll
        return: Die Pauseninstanz mit korrigierter bzw. inkrementierte ID
        """

        cursor = self._cnx.cursor()
        cursor.execute("SELECT MAX(pause_id) AS maxid FROM Pause")
        tuples = cursor.fetchall()

        for (maxid) in tuples:
            pause.set_id(maxid[0] + 1)


        """ Hier wird die Pause Instanz in die Datenbank mit dem Insert Befehl gespeichert """
        command = "INSERT INTO Pause (pause_id, person_id, start_pause, ende_pause, letzte_aenderung) VALUES (%s,%s,%s,%s,%s)"
        data = (pause.get_id(), pause.get_person_id(), pause.get_start_pause(), pause.get_ende_pause(), pause.get_letzte_aenderung())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()

        return pause

    def find_by_id(self, id):
        """ Wir suchen die Pause mit der jeweiligen ID """
        result = None

        cursor = self._cnx.cursor()
        command = "SELECT * FROM Pause WHERE pause_id={0}".format(id)
        cursor.execute(command)
        pause_daten = cursor.fetchall()

        try:
            (pause_id, projekt_id, person_id, start_pause, ende_pause, letzte_aenderung) = pause_daten[0]
            pause = Pause()
            pause.set_id(pause_id)
            pause.set_projekt_id(projekt_id)
            pause.set_person_id(person_id)
            pause.set_start_pause(start_pause)
            pause.set_ende_pause(ende_pause)
            pause.set_letzte_aenderung_fuer_get_methode(letzte_aenderung)
            result = pause
        except IndexError:
            """ Tritt auf, wenn es beim SELECT-Aufruf kein Ergebnis liefert, sondern pause_daten leer ist """
            result = None

        self._cnx.commit()
        cursor.close()
        print(result)
        return result


    def delete(self, pause):
        """Löschen der Daten eines Pause-Objekts aus der Datenbank.

        :param Pause das aus der DB zu löschende "Objekt"
        """
        cursor = self._cnx.cursor()

        command = "DELETE FROM Pause WHERE pause_id={}".format(pause)
        cursor.execute(command)

        self._cnx.commit()
        cursor.close()
        return pause



    def update(self, pause):
        cursor = self._cnx.cursor()

        command = "UPDATE Pause " + "SET projekt_id =%s, person_id=%s, start_pause=%s, ende_pause=%s, letzte_aenderung=%s WHERE pause_id=%s"
        data = (pause.get_projekt_id(), pause.get_person_id(), pause.get_start_pause(), pause.get_ende_pause(), pause.get_letzte_aenderung(), pause.get_id())
        cursor.execute(command, data)

        self._cnx.commit()
        cursor.close()










if __name__ == '__main__':
    with PauseMapper() as mapper:
        result = mapper.find_all()