from abc import ABC

class BusinessObject(ABC):
    def __init__(self):
        self.__id = 0

    def get_id(self):
        return self.id

    def set_id(self, value):
        self.__id = value