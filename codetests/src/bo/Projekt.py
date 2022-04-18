from bo import BusinessObject as bo

class Projekt(bo.BusinessObject):
    def __init__(self,name,auftraggeber):
        super().__init__()
        self.__name = name
        self.__aktiviäten = list()
        self.__auftraggeber = auftraggeber
        self.__team = {}

    def set_name(self,name):
        self.__name = name
        return self.__name

    def get_name(self):
        return self.__name


    def set_auftraggeber(self,auftraggeber):
        self.__auftraggeber = auftraggeber
        return self.__auftraggeber

    def get_auftraggeber(self):
        return self.__get_auftraggeber


    def set_team(self,*args):
        z = 2
        for i in args:
            if (z%2 != 0):
                verkaufte_stunden = i
                self.__team[mitarbeiter] = verkaufte_stunden
            else:
                mitarbeiter = i
            z+=1

    def get_team(self):
        return self.__team


    def set_aktivitäten(self, *aktivitäten):
        self.__aktivitäten = aktivitäten
        return self.__aktivitäten

    def get_aktivitäten(self):
        return self.__aktivitäten
