class Rechteck:

    def __init__(self, a=1, b=1):
        self.__a = a
        self.__b = b

    def getFlaeche(self):
        return self.__a * self.__b

    def setA(self, a):
        self.__a = a

    def setB(self, b):
        self.__b = b
