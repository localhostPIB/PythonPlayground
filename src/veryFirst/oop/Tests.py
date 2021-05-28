import unittest
from Kreis import Kreis
from Rechteck import Rechteck
from Schrank import Schrank


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_Kreis(self):
        kreis = Kreis('Rot')
        self.assertEqual(kreis.getFarbe(), 'Rot')

    def test_Rechteck(self):
        rechteck = Rechteck(2, 4)
        self.assertEqual(rechteck.getFlaeche(), 8)

    def test_Schrank(self):
        abmessungen = [5, 2, 10]
        schrank1 = Schrank("Ikea B", 4, 2, 1)
        schrank2 = Schrank()
        self.assertEqual(Schrank.getAnzahl(), 2)


if __name__ == '__main__':
    unittest.main()
