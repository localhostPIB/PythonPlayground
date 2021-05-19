# -*- coding: utf-8 -*-

def start():
    eingabe = -1
    while eingabe != 4:
        try:
            eingabe = einlesenFunktion()
            execute(eingabe)
        except ValueError:
            print("Funktion unbekannt !!")


def execute(eingabe):
    if int(eingabe) == 4:
        exit(0)
    else:
        print(eingabe)


def einlesenFunktion():
    print("========================================================")
    print("Bitte wählen Sie eine Option:")
    print("1 Funktion 1")
    print("2 Funktion 2")
    print("3 Funktion 3")
    print("4 Programm beenden")
    i = input("Ihre Eingabe: ")

    return i


start()
