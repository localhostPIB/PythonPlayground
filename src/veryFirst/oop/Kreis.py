import math


class Kreis:
    # Klassenvariable
    __anzahl = 0

    # Konstruktor
    def __init__(self, r=1, x=0, y=0):
        self.__x = x
        self.__y = y
        if r > 0:
            self.__radius = r
        Kreis.__anzahl = Kreis.__anzahl + 1
        self.__anzahl += 1

    def __init__(self, farbe='Blau', r=1, x=1, z=1):
        self.__farbe = farbe
        self.__r = r
        self.__x = x
        self.__z = z

    def __init__(self, r=1, x=0, y=0, z=1):
        self.__radius = r
        self.__x = y
        self.__y = y
        self.__z = y

    def __init__(self, farbe):
        self.__farbe = farbe
        Kreis.__anzahl = Kreis.__anzahl + 1
        self.__anzahl = self.__anzahl + 1

    # Berechnen der Kreisflaeche
    def getFlaeche(self):
        return math.pi * self.__radius * self.__radius

    # Verschieben des Kreismittelpunktes
    def verschiebe(self, dx, dy):
        self.__x = self.__x + dx
        self.__y = self.__y + dy

    def getFarbe(self):
        return self.__farbe

    def getRadius(self):
        return self.__radius

    # Berechnen des Kreisumfangs
    def getUmfang(self):
        return 2 * math.pi * self.__radius

    def getMittelpunkt(self):
        return [self.__x, self.__y]

    def setRadius(self, r):
        if self.__r > 0:
            self.__radius = r

    def setFarbe(self, farbe):
        self.__farbe = farbe

    def setMittelpunkt(self, x, y):
        self.__x = x
        self.__y = y

    @staticmethod
    def getAnzahl():
        return Kreis.__anzahl
