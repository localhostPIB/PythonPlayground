# -*- coding: utf-8 -*-

class Pkw():
    """ Klasse für das Erstellen von Autos """

    def __init__(self, farbe, baujahr, kmstand, sitze, marke):
        self.farbe = farbe
        self.baujahr = baujahr
        self.kmstand = kmstand
        self.sitze = sitze
        self.marke = marke


trabi = Pkw("weiß", 1981, 143000, 4, "Trabi")
