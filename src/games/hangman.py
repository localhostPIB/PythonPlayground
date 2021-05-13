import random

print("hangman in Python")
woerter = 'Hallo Welt in Python'.split()
erraten = []
nutzereingabe = ""
fehlversuche = 7
ratewort = random.choice(woerter)

for buchstaben in ratewort:
    erraten.append('_')

while nutzereingabe != "bye":
    for ausgabe in erraten:
        print(ausgabe, end=' ')
    print()
    nutzereingabe = input("Ihr Vorschlag: ")
    x = 0
    for buchstaben in ratewort:
        if buchstaben.lower() == nutzereingabe.lower():
            print("Treffer")
            erraten[x] = buchstaben
        x += 1
    print()

    if '_' in erraten:
        # print('Noch nicht gewonnen')
        fehlversuche -= 1
        if fehlversuche == 0:
            print("Schade - verloren!")
            break
    else:
        print("Gewonnen, das Wort war: ", ratewort)
        break
