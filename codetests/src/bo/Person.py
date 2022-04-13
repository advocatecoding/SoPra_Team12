from bo import BusinessObject as bo

class Person(bo.BusinessObject):

    def __init__(self, name):
        super().__init__()
        self.__name = name


    def get_name(self):
        return self.__name