from bo.Zeitintervall import Zeitintervall

class Pause(Zeitintervall):
    def __init__(self, ereignisbuchung=None):
        super().__init__(ereignisbuchung)
        if ereignisbuchung is not None:
            self.__aktivitaet = ereignisbuchung.get_aktivitaet()
            # self.__ereignisbuchung = ereignisbuchung
            self.__person = ereignisbuchung.get_person()
            """ Zeitintervall wird ausgerechnet durch Ende und Start """
            start = ereignisbuchung.get_startereignis()
            ende = ereignisbuchung.get_endereignis()
            time_new = ende - start
            time_new = int(time_new.total_seconds() / 3600)
            self.__zeitintervall = time_new