class Schrank:
    __zaehler = 0  # doppelt __ == private ; einfach _ protected unt ohne ist public
    """ https://www.tutorialsteacher.com/python/public-private-protected-modifiers  """

    def __init__(self, name, b, h, preis, abmessungen):
        self.__name = name
        self.__b = b
        self.__h = h
        self.__preis = preis
        self.__abmessungen = abmessungen
        Schrank.__zaehler += 1

    def __init__(self, name="Ikea Billy", b=2, h=4, preis=100, abmessungen=None):
        if abmessungen is None:
            abmessungen = [2, 5, 2]
        self.__name = name
        self.__b = b
        self.__h = h
        self.__preis = preis
        self.__abmessungen = abmessungen
        Schrank.__zaehler += 1

    def getPreis(self):
        return self.__preis * (self.getVolumen() / 4)

    def getAbmessungen(self):
        return self.__abmessungen

    def setAbmessungen(self, a):
        self.__abmessungen = a

    def setB(self, b):
        self.__b = b

    def setH(self, h):
        self.__h = h

    def setName(self, n):
        self.__name = n

    def getName(self):
        return self.__name

    def getB(self):
        return self.__b

    def getH(self):
        return self.__h

    def getVolumen(self):
        return self.__abmessungen[0] * self.__abmessungen[1] * self.__abmessungen[2]

    @staticmethod
    def getAnzahl():
        return Schrank.__zaehler
