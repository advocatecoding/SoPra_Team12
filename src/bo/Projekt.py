from bo import BusinessObject as bo

class Projekt(bo.BusinessObject):
    def __init__(self,name,auftraggeber):
        super().__init__()
        self.__name = name
        self.__aktiviäten = list()
        self.__auftraggeber = auftraggeber
        self.__team = {}

    def set_name(self,name):
        """Setzen des Projektnamens."""
        self.__name = name
        return self.__name

    def get_name(self):
        """Auslesen des Projektnamens."""
        return self.__name


    def set_auftraggeber(self,auftraggeber):
        """Setzen des Auftraggebers."""
        self.__auftraggeber = auftraggeber
        return self.__auftraggeber

    def get_auftraggeber(self):
        """Auslesen des Auftraggebers."""
        return self.__get_auftraggeber


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
            if (z%2 != 0):
                verkaufte_stunden = i
                self.__team[mitarbeiter] = verkaufte_stunden
            else:
                mitarbeiter = i
            z+=1

    def get_team(self):
        """Auslesen des Projektteams inklusive der verkauften Zeiten."""
        return self.__team


    def set_aktivitäten(self, *aktivitäten):
        """Setzen der Aktivitäten."""
        self.__aktivitäten = aktivitäten
        return self.__aktivitäten

    def get_aktivitäten(self):
        """Auslesen der Aktivitäten."""
        return self.__aktivitäten

