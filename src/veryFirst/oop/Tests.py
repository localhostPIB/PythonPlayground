import unittest
from Kreis import Kreis
from Rechteck import Rechteck
from Schrank import Schrank
from Auftrag import Auftrag
from Klausur import Klausur
from Student import Student
from Pruefungsamt import Pruefungsamt


class MyTestCase(unittest.TestCase):

    def test_Kreis(self):
        kreis = Kreis('Rot')
        a = kreis.getAnzahl()
        self.assertEqual(kreis.getFarbe(), 'Rot')

    def test_Rechteck(self):
        rechteck = Rechteck(2, 4)
        self.assertEqual(rechteck.getFlaeche(), 8)

    def test_Schrank(self):
        abmessungen = [5, 2, 10]
        schrank1 = Schrank("Ikea B", 1, 2, 1)
        schrank2 = Schrank()
        self.assertEqual(Schrank.getAnzahl(), 2)

    def test_Auftrag(self):
        auftrag = Auftrag()
        schrank0 = Schrank("Ikea A", 4, 2, 100)
        schrank1 = Schrank("Ikea B", 7, 2, 50)
        auftrag.add(schrank0)
        auftrag.add(schrank1)

    def test_Student(self):
        list =[]
        klausur0 = Klausur("Prog.1", "KI", 3.5)
        klausur1 = Klausur("Prog.2", "KI", 3.0)
        student0 = Student(111111, "Adam", "Eve")
        student1 = Student(222222, "Freddy", "Krueger")
        list.append(student0)
        list.append(student1)
        pruefungsamt = Pruefungsamt(list)
        student0.addKlausur(klausur0)
        student0.addKlausur(klausur1)
        pruefungsamt.getStudent(333333, "Jason", "Voorhees")
        pruefungsamt.getStudent(333333, "Jason", "Voorhees")
        pruefungsamt.schreibeDaten()
        pruefungsamt.leseDaten("Notenliste_111111_Adam_Eve")


if __name__ == '__main__':
    unittest.main()
