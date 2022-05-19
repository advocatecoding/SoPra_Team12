from bo import BusinessObject as bo

class Projekt(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._projektname = ""
        self._aktivitaeten = list()
        self._auftraggeber = ""
        """ Wir durch ein Zeitintervall Objekt festgelegt """
        self.__projektlaufzeit = None
        self.__team = {}
        self._projektleiter = None


    def get_projektlaufzeit(self):
        return self.__projektlaufzeit

    def set_projektlaufzeit(self, value):
        self.__projektlaufzeit = value

    def set_projektleiter(self,projektleiter):
        """Setzen des Projektleiters."""
        self._projektleiter = projektleiter

    def get_projektleiter(self):
        """Auslesen des Projektleiters."""
        return self._projektleiter

    def set_name(self, name):
        """Setzen des Projektnamens."""
        self._projektname = name

    def get_name(self):
        """Auslesen des Projektnamens."""
        return self._projektname


    def set_auftraggeber(self,auftraggeber):
        """Setzen des Auftraggebers."""
        self._auftraggeber = auftraggeber

    def get_auftraggeber(self):
        """Auslesen des Auftraggebers."""
        return self._auftraggeber


    """ Ist das hier überhaupt nötig
    def set_dauer(self, value):
        self.__dauer = value

    def get_dauer(self):
        return self.__get_dauer

    """


    def set_team(self,*args):
        """Setzen des Projektteams inklusive der verkauften Zeiten."""
        z = 2
        for i in args:
            if z%2 != 0:
                verkaufte_stunden = i
                self.__team[mitarbeiter] = verkaufte_stunden
            else:
                mitarbeiter = i
            z+=1


    def set_team1(self, mitarbeiter, verkaufte_stunden):
         self.__team[mitarbeiter] = verkaufte_stunden



    def get_team(self):
        """Auslesen des Projektteams inklusive der verkauften Zeiten."""
        return self.__team


    def set_aktivitaeten(self, *aktivitäten):
        """Setzen der Aktivitäten."""
        self._aktivitaeten = aktivitäten

    def get_aktivitaeten(self):
        """Auslesen der Aktivitäten."""
        return self._aktivitaeten


    def from_dict(dictionary=dict()):
        """Umwandeln eines Python dict() in ein Projekt()."""
        obj = Projekt()
        obj.set_id(dictionary["id"])
        obj.set_projektleiter(dictionary["projektleiter"])
        obj.set_name(dictionary["projektname"])
        obj.set_auftraggeber(dictionary["auftraggeber"])
        obj.set_letzte_aenderung()

        return obj


