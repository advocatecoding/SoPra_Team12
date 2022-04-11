from bo import BusinessObject as bo
import datetime

class Zeitintervall(bo.BusinessObject):
    def __init__(self):
        super().__init__()
        self.time = 0

    def get_type(self, time):
        print(time.get_start_ereignis())

    def set_zeitintervall(self, time):
        time1 = time.get_start_ereignis()
        time2 = time.get_end_ereignis()
        time_new = time2 - time1
        time_new = int(time_new.total_seconds()/3600)
        self.time = time_new

    def get_zeitintervall(self):
        return self.time





"""
    def get_zeitintervall(self):
        return self.__zeitintervall
"""