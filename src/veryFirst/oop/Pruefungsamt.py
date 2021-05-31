from Student import Student
import re


class Pruefungsamt:
    __studentenListe = []

    def __init__(self, studentenListe=None):
        self.__studentenListe = studentenListe

    def addStudent(self, student):
        self.__studentenListe.append(student)

    def schreibeDaten(self):
        s = ""
        for i in self.__studentenListe:
            s += str(i.getMatrikel()) + " Nachname: " + str(i.getNachName()) + " Vorname: " + str(i.getVorName()) + "\n"

        return s

    # Lineare Suche
    def findeStudent(self, matrikel):
        for i in self.__studentenListe:
            if i.getMatrikel() == matrikel:
                return "Vorname: " + i.getVorName() + " Nachname: " + i.getNachName()

    def getStudent(self, matrikel, vorname, nachname):
        if self.findeStudent(matrikel) is None:
            student = Student(matrikel, nachname, vorname)
            self.addStudent(student)
            return student
        return self.findeStudent(matrikel)

    def schreibeNotenliste(self, student):
        f = open("Notenliste_" + str(student.getMatrikel()) + "_" + student.getNachName() + "_" + student.getVorName(), "w")
        f.write(student.schreibeDaten())
        f.close()

    def leseDaten(self, file):
        f = open(file, "r")
        reg = r'(\d{6})'
        pattern = re.compile(reg)
        p = pattern.search(f.name)
        mNr = p.group(0)
        student = self.findeStudent(mNr)
        f.close()
