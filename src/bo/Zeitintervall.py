from bo import BusinessObject as bo
import datetime

class Zeitintervall(bo.BusinessObject):
    def __init__(self, start=None, ende=None):
        super().__init__()
        self.__zeit = 0
        self.__person = None
        self.__aktivitaet = None
        self.__projekt = None

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


    def get_projekt(self):
        return self.__projekt

    def set_projekt(self, value):
        self.__projekt = value


    def get_start(self):
        return self.__start

    def get_ende(self):
        return self.__ende

    def get_zeit(self):
        return self.__zeit

    def set_zeit(self, value):
        self.__zeit = value

    def get_person(self):
        return self.__person

    def set_person(self, value):
        self.__person = value

    def get_aktivitaet(self):
        return self.__aktivitaet

    def set_aktivitaet(self, value):
        self.__aktivitaet = value


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