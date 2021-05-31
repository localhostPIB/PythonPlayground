class Student:
    __matrikelNr = 0
    __nachName = ""
    __vorName = ""
    __klausurListe = []

    def __init__(self, matrikelNr, nachName, vorName, klausurListe=None):
        self.klausurListe = klausurListe
        self.__matrikelNr = matrikelNr
        self.__nachName = nachName
        self.__vorName = vorName

    def getMatrikel(self):
        return self.__matrikelNr

    def getNachName(self):
        return self.__nachName

    def getVorName(self):
        return self.__vorName

    def pruefeMatrikel(self, matrikel):
        if self.__matrikelNr is matrikel:
            return True
        return False

    def addKlausur(self, klausur):  # todo Typ beschränken
        self.__klausurListe.append(klausur)

    def schreibeDaten(self):
        sumNote = 0
        list = []
        for i in self.__klausurListe:
            sumNote += i.getNote()
            list.append("Infos: " + i.getDaten())

        string = "Notenschnitt: " + str(sumNote / len(self.__klausurListe))
        list.append(string)
        return list.__str__()