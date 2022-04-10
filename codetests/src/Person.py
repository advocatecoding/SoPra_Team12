class Person:

    def __init__(self, name, id):
        self.__name = name
        self.__id = id


    def get_id(self):
        return self.__id