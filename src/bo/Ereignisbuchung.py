from bo import BusinessObject as bo


class Ereignisbuchung(bo.BusinessObject):
    def __init__(self, ereignis):
        super().__init__()
        self.__ereignis = ereignis
        self.__ereignis_type = type(self.__ereignis).__name__


    def get_ereignis_type(self):
        return self.__ereignis_type



"""
    def __init__(self, start_ereignis, end_ereignis):
        super().__init__()
        self.__start_ereignis = start_ereignis
        self.__end_ereignis = end_ereignis

    def set_start_ereignis(self, value):
        self.__start_ereignis = value.get_start()
        print(type(self.__start_ereignis))

    def get_start_ereignis(self):
        return self.__start_ereignis

    def set_end_ereignis(self, value):
        self.__end_ereignis = value.get_end()

    def get_end_ereignis(self):
        return self.__end_ereignis
"""