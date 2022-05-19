from bo import BusinessObject as bo
import datetime

class Zeitintervall(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self.__aktivitaet = None
        self.__start = None
        self.__ende = None
        self.__person = None
        self.__zeitintervall = None

    def get_projekt(self):
        return self.__projekt

    def set_projekt(self, value):
        self.__projekt = value

    #def set_ereignisbuchung(self, value):
    #    self.__ereignisbuchung = value

    #def get_ereignisbuchung(self):
    #    return self.__ereignisbuchung

    def get_start(self):
        return self.__start

    def get_ende(self):
        return self.__ende

    def get_zeitintervall(self):
        return self.__zeitintervall

    def set_projektlaufzeit(self, value):
        self.__zeitintervall = value

    def set_zeitintervall(self, ereignisbuchung):
        """ Zeitintervall wird ausgerechnet durch Ende und Start """
        self.__start = ereignisbuchung.get_startereignis()
        self.__ende = ereignisbuchung.get_endereignis()
        time_new = self.__ende - self.__start
        time_new = int(time_new.total_seconds() / 3600)
        self.__zeitintervall = time_new

    def get_person(self):
        return self.__person

    def set_person(self, ereignisbuchung):
        self.__person = ereignisbuchung.get_person()

    def get_aktivitaet(self):
        return self.__aktivitaet

    def set_aktivitaet(self, ereignisbuchung):
        self.__aktivitaet = ereignisbuchung.get_aktivitaet()



"""
        Wenn für Start und Ende ein Wert gesetzt wurden  
        if None not in (start, ende):
            self.__start = start
            self.__ende = ende
            time1 = start.get_start()
            time2 = ende.get_ende()
            time_new = time2 - time1
            time_new = int(time_new.total_seconds() / 3600)
            self.__zeit = time_new
        else:
            print("Sie haben ein Zeitinervall ohne Ereignisse gebucht.")
"""

"""
    def set_start(self, value):
        self.__start = value
"""

"""
    def set_ende(self, value):
        self.__ende = value
"""


"""
    def set_zeitintervall(self, time):
        time1 = time.get_start_ereignis()
        time2 = time.get_end_ereignis()
        time_new = time2 - time1
        time_new = int(time_new.total_seconds()/3600)
        self.time = time_new

    def get_zeitintervall(self):
        return self.time
"""




"""
    def get_zeitintervall(self):
        return self.__zeitintervall
"""