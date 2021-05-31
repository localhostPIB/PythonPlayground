class Auftrag:
    __mwSt = 1.19
    __artikel = []

    def __init__(self):
        pass

    def add(self, schrank): # todo Typ beschränken
        self.__artikel.append(schrank)

    def getAuftragMitMehrwertsteuer(self):
        preis = 0
        for i in self.__artikel:
            preis += i.getPreis() * Auftrag.__mwSt

        return round(preis, 2)

    def getAuftragOhneMehrwertsteuer(self):
        preis = 0
        for i in self.__artikel:
            preis += i.getPreis() * (2 - self.__mwSt)

        return round(preis, 2)

    def getAuftragsliste(self):
        string = ""
        for i in self.__artikel:
            string += "\nSchrankname: " + str(i.getName()) + " Volumen: " + str(i.getVolumen()) + " Breite: " + str(
                i.getB()) + " Hoehe: " + str(i.getH())

        string += "\nPreis mit MwSt: " + str(self.getAuftragMitMehrwertsteuer()) + \
                  "\nPreis ohne MwSt: " + str(self.getAuftragOhneMehrwertsteuer())

        return string

    def getAnzahl(self):
        return len(self.__artikel)
