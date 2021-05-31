class Klausur:
    __fachbezeichnung = ""
    __semesterkuerzel = ""
    __note = 0

    def __init__(self, fachbezeichnung, semesterkuerzel,note):
        self.__fachbezeichnung = fachbezeichnung
        self.__semesterkuerzel = semesterkuerzel
        self.__note = note

    def getNote(self):
        return self.__note

    def getDaten(self):
        return "Fachbezeichnung: " + self.__fachbezeichnung + " Semesterkuerzel:" + str(self.__note)
