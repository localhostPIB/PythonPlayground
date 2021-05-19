# -*- coding: utf-8 -*-
import math
import random


def zins():
    p = input("Zinssatz p [%] : ")
    n = input("Jahre : ")
    k = input("Anfangskapitalwert K [Euro] : ")
    result = round(float(k) * float(math.pow((float(p) / 100) + 1, int(n))), 2)
    print("Ergebnis:", result)
    exit(0)


def dreieckflaeche():
    a = input("a : ")
    b = input("b : ")
    c = input("c : ")
    s = (float(a) + float(b) + float(c)) / 2
    result = math.sqrt((s * (s - float(a)) * (s - float(b)) * (s - float(c))))
    print("Ergebnis:", result)
    exit(0)


def dutzent():
    n = input("n : ")
    g = int(n) / 144

    temp = int(g) * 144
    x = int(n) - temp
    s = int(x) / 60

    temp1 = int(s) * 60
    d = int(x) - temp1
    e = int(d) / 12

    rest = int(g) * 144 + int(s) * 60 + int(e) * 12
    rest = int(n) % int(rest)

    print(int(g), int(s), int(e), int(rest))
    exit(0)


def mitternachtsFormel():
    a = input("a : ")
    b = input("b : ")
    c = input("c : ")

    resultx1 = - (float(b) + math.sqrt(math.pow(float(b), 2) - (4 * float(a) * float(c)))) / (2 * float(a))
    resultx2 = - (float(b) - math.sqrt(math.pow(float(b), 2) - (4 * float(a) * float(c)))) / (2 * float(a))

    d = math.pow(float(b), 2) - (4 * float(a) * float(c))
    if d > 0:
        print("Zwei Lösungen")
        print(resultx1, "und", resultx2)
    elif d == 0:
        print("Genau eine Lösung")
        print(resultx1, "und", resultx2)
    elif d < 0:
        print("Keine reelle Lösung")
    exit(0)


def muenzwurf():
    kopf = 0
    zahl = 1
    a = random.randint(kopf, zahl)

    if a == 0:
        print("Kopf")
    else:
        print("Zahl")
    exit(0)


def schraubenTyp():
    durchmesser = input("Durchmesser der Schraube: ")
    laenge = input("Laenge der Schraube: ")

    if int(durchmesser) <= 3 and int(laenge) <= 20:
        print("Typ 1")
    elif 4 <= int(durchmesser) <= 6 and 21 <= int(laenge) <= 30:
        print("Typ 2")
    elif 7 <= int(durchmesser) <= 20 and 31 <= int(laenge) <= 50:
        print("Typ 3")

    exit(0)


def kalender():
    monat = input("Bitte geben sie eine Monatszahl ein: ")
    jahr = input("Bitte geben sie eine Jahreszahl ein: ")
    if int(monat) == 1 or int(monat) == 3 or int(monat) == 5 or int(monat) == 7 or int(monat) == 8 or int(monat) == 10 \
            or int(monat) == 12:

        tage = 31
    elif int(monat) == 4 or int(monat) == 6 or int(monat) == 9:
        tage = 30
    else:
        if int(jahr) % 4 == 0 and int(jahr) % 100 != 0:
            tage = 29
        else:
            tage = 28
    print(tage)
    exit(0)


def schleifensteuerung():
    for i in range(1, 6, 1):
        for j in range(1, 11, 1):
            for k in range(0, 10, 1):
                if i + j + k == 10:
                    print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")

    exit(0)


def muster():
    for i in range(1, 5, 1):
        print(" ")
        for y in range(0, i, 1):
            print("*".format(y, y*y))
    # todo
    exit(0)


muster()
schleifensteuerung()
kalender()
schraubenTyp()
mitternachtsFormel()
muenzwurf()
dutzent()
dreieckflaeche()
zins()
