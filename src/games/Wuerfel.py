import random


def w1():
    max1 = 0
    max2 = 0
    for i in range(1, 10, 1):
        spieler1 = random.randint(1, 6)
        spieler2 = random.randint(1, 6)

        if spieler1 > max1:
            max1 = spieler1

        if spieler2 > max2:
            max2 = spieler2

    if max1 > max2:
        print("Spieler 1 ist ist gewinner", max1)

    if max2 > max1:
        print("Spieler 2 ist ist gewinner", max2)

    if max2 == max1:
        print("Unentschieden")

    exit(0)


def w2():
    a = True
    spieler1 = 0
    spieler2 = 0

    while a:
        spieler1 += random.randint(1, 6)
        spieler2 += random.randint(1, 6)

        if spieler1 >= 100:
            print("Spieler 1 hat gewonnen ")
            break

        if spieler2 >= 100:
            print("Spieler 2 hat gewonnen ")
            break

    exit(0)


def w3():
    a = True
    count1 = 0
    count2 = 0
    first = random.randint(1, 6)
    second = random.randint(1, 6)

    while a:
        spieler1 = random.randint(1, 6)
        if first == spieler1:
            count1 += 1
        else:
            first = spieler1

        spieler2 = random.randint(1, 6)
        if second == spieler2:
            count2 += 1
        else:
            second = spieler2

        if count1 >= 3:
            print("Spieler 1 hat gewonnen")
            break

        if count2 >= 3:
            print("Spieler 2 hat gewonnen")
            break

    exit(0)


def w4():
    a = True

    while a:
        spieler1 = random.randint(1, 6)
        spieler2 = random.randint(1, 6)

        if spieler1 == 6:
            print("spieler 1 hat gewonnen")
            break

        if spieler2 == 6:
            print("spieler 2 hat gewonnen")
            break

    exit(0)


w4()
w3()
w2()
w1()
