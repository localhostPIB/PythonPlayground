import random

# https://www.python-lernen.de/

count = 0
zahl = random.randint(0, 100)

while count <= 7:
    eingabe = int(input("Rate mal: "))
    if zahl == eingabe:
        print("Richtig!!! " + str(eingabe))
        break

    elif eingabe > zahl:
        print("Die eingegebene Zahl " + str(eingabe) + " ist leider zu gross !!")

    elif eingabe < zahl:
        print("Die eingegebene Zahl " + str(eingabe) + " ist leider zu klein !!")

    count = count + 1
    versuche = 8 - count

    if versuche > 0:
        print("Noch " + str(versuche) + " Versuche !")
    else:
        print("Zu viele Versuche, sorry, richtig war " + str(zahl))
print("")
print("Game Over")
