from bo.Zeitintervall import Zeitintervall

class Pause(Zeitintervall):
    def __init__(self, ereignisbuchung):
        super().__init__(ereignisbuchung)
        self.__aktivitaet = ereignisbuchung.get_aktivitaet()
        # self.__ereignisbuchung = ereignisbuchung
        self.__person = ereignisbuchung.get_person()
        """ Zeitintervall wird ausgerechnet durch Ende und Start """
        self.__start = ereignisbuchung.get_startereignis()
        self.__ende = ereignisbuchung.get_endereignis()
        time_new = self.__ende - self.__start
        time_new = int(time_new.total_seconds() / 3600)
        self.__zeitintervall = time_new