import random

spiel_aktiv = True
spieler_aktuell = 'X'

spielfeld = [" ",
             "1", "2", "3",
             "4", "5", "6",
             "7", "8", "9"]


def print_field():
    print(spielfeld[1] + "|" + spielfeld[2] + "|" + spielfeld[3])
    print(spielfeld[4] + "|" + spielfeld[5] + "|" + spielfeld[6])
    print(spielfeld[7] + "|" + spielfeld[8] + "|" + spielfeld[9])


def user_input():
    global spiel_aktiv
    while True:
        spielzug = input("Bitte Feld eingeben: ")

        if spielzug == 'q':
            spiel_aktiv = False
            return
        try:
            spielzug = int(spielzug)
        except ValueError:
            print("Bitte Zahl von 1 bis 9 eingeben")
        else:
            if spielzug >= 1 and spielzug <= 9:
                if spielfeld[spielzug] == 'X' or spielfeld[spielzug] == 'O':
                    print("Das Feld ist bereits belegt - ein anderes wählen!")
                else:
                    return spielzug
            else:
                print("Zahl muss zwischen 1 und 9 liegen")


def player_change():
    global spieler_aktuell
    if spieler_aktuell == 'X':
        spieler_aktuell = 'O'
    else:
        spieler_aktuell = 'X'

def kontrolle_gewonnen():
    if spielfeld[1] == spielfeld[2] == spielfeld[3]:
        return spielfeld[1]
    if spielfeld[4] == spielfeld[5] == spielfeld[6]:
        return spielfeld[4]
    if spielfeld[7] == spielfeld[8] == spielfeld[9]:
        return spielfeld[7]
    if spielfeld[1] == spielfeld[4] == spielfeld[7]:
        return spielfeld[1]
    if spielfeld[2] == spielfeld[5] == spielfeld[8]:
        return spielfeld[2]
    if spielfeld[3] == spielfeld[6] == spielfeld[9]:
        return spielfeld[3]
    if spielfeld[1] == spielfeld[5] == spielfeld[9]:
        return spielfeld[5]
    if spielfeld[7] == spielfeld[5] == spielfeld[3]:
        return spielfeld[5]


def kontrolle_auf_unentschieden():
    if (spielfeld[1] == 'X' or spielfeld[1] == 'O') \
            and (spielfeld[2] == 'X' or spielfeld[2] == 'O') \
            and (spielfeld[3] == 'X' or spielfeld[3] == 'O') \
            and (spielfeld[4] == 'X' or spielfeld[4] == 'O') \
            and (spielfeld[5] == 'X' or spielfeld[5] == 'O') \
            and (spielfeld[6] == 'X' or spielfeld[6] == 'O') \
            and (spielfeld[7] == 'X' or spielfeld[7] == 'O') \
            and (spielfeld[8] == 'X' or spielfeld[8] == 'O') \
            and (spielfeld[9] == 'X' or spielfeld[9] == 'O'):
        return ('unentschieden')


print_field()
while spiel_aktiv:
    print()
    print("Spieler " + spieler_aktuell + " am Zug")

    spielfeld_KI = []
    for moegliche_felder in spielfeld:
        if moegliche_felder != 'X' and moegliche_felder != 'O' and moegliche_felder != ' ':
            spielfeld_KI += moegliche_felder

    if spieler_aktuell == 'O':
        spielzug = int(random.choice(spielfeld_KI))
    else:
        spielzug = user_input()
    if spielzug:
        spielfeld[spielzug] = spieler_aktuell
        print_field()
        gewonnen = kontrolle_gewonnen()
        if gewonnen:
            print("Spieler " + gewonnen + " hat gewonnen!")
            spiel_aktiv = False
            break
        unentschieden = kontrolle_auf_unentschieden()
        if unentschieden:
            print("Spiel ist unentschieden ausgegangen")
            spiel_aktiv = False
        player_change()
print()