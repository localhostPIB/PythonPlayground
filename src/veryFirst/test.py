def bspfunktionfuerrueckgabe(eingabewert):
    print("def: bspfunktionfuerrueckgabe", eingabewert)
    return eingabewert


if __name__ == "__main__":
    print("Datei wurde direkt aufgerufen und die Main wird ausgeführt")
else:
    print("Datei wurde als Modul aufgerufen")

print("Ich stehe in der Datei: " + __name__)