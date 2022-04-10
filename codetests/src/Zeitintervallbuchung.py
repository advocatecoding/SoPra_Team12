

class Zeitinverallbuchung:

    def __init__(self):
        self.__person = None
        self.__aktivität = None
        self.__buchungsart = None


    def set_zeitintervallbuchung(self, zeit, person, aktivität, buchungsart):
        if type(buchungsart) == Projektarbeit:
            """Wenn Zeitintervall eine Projektarbeit ist -> Keine Pause"""
            aktivität.set_gearbeitet(zeit)


