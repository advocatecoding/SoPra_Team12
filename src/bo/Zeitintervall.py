from bo import BusinessObject as bo
import datetime

class Zeitintervall(bo.BusinessObject):
    def __init__(self, ereignisbuchung=None):
        super().__init__()
        """ Wir prüfen ob überhaut eine ereignisbuchung gepassed wurde oder ob direkt ein Zeitintervall geucht wird ohen Ereignisse """
        if ereignisbuchung is not None:
            self.__aktivitaet = ereignisbuchung.get_aktivitaet()
            self.__person = ereignisbuchung.get_person()

            """ Zeitintervall wird ausgerechnet durch Ende und Start """
            start = ereignisbuchung.get_startereignis()
            ende = ereignisbuchung.get_endereignis()
            time_new = ende - start
            time_new = int(time_new.total_seconds() / 3600)
            self.__zeitintervall = time_new
    
    
    """ Die set-Methoden werden genutzt wenn keine Ereignisbuchung weitergegeben wird, sondern stattdessen direkt ein Zeitintervall gebucht wird, sowohl
        für eine Projektarbeit/Pause, als auch nur für eine Projektlaufzeit """
    def set_projektlaufzeit(self, value):
        self.__zeitintervall = value

    def get_zeitintervall(self):
        return self.__zeitintervall
    
    def set_zeitintervall(self, value):
        self.__zeitintervall = value

    def get_person(self):
        return self.__person

    def set_person(self, value):
        self.__person = value

    def get_aktivitaet(self):
        return self.__aktivitaet

    def set_aktivitaet(self, value):
        self.__aktivitaet = value
"""
    def set_zeitintervall(self, ereignisbuchung):
        self.__start = ereignisbuchung.get_startereignis()
        self.__ende = ereignisbuchung.get_endereignis()
        time_new = self.__ende - self.__start
        time_new = int(time_new.total_seconds() / 3600)
        self.__zeitintervall = time_new
"""
   