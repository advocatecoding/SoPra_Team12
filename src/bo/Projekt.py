from bo import BusinessObject as bo

class Projekt(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self._projektname = ""
        self._aktivitaeten = list()
        self._auftraggeber = ""
        self.__team = {}

    def set_name(self,name):
        """Setzen des Projektnamens."""
        self._projektname = name
        return self._projektname

    def get_name(self):
        """Auslesen des Projektnamens."""
        return self._projektname


    def set_auftraggeber(self,auftraggeber):
        """Setzen des Auftraggebers."""
        self._auftraggeber = auftraggeber
        return self._auftraggeber

    def get_auftraggeber(self):
        """Auslesen des Auftraggebers."""
        return self._auftraggeber


    """ Ist das hier überhaupt nötig
    def set_dauer(self, value):
        self.__dauer = value
        return self.__dauer

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

    def get_team(self):
        """Auslesen des Projektteams inklusive der verkauften Zeiten."""
        return self.__team


    def set_aktivitaeten(self, *aktivitäten):
        """Setzen der Aktivitäten."""
        self._aktivitaeten = aktivitäten
        return self._aktivitaeten

    def get_aktivitaeten(self):
        """Auslesen der Aktivitäten."""
        return self._aktivitaeten

