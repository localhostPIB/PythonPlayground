# -*- coding: utf-8 -*-
import random

zufallsantworten = ["Oh, wirklich", "Interessant ...", "Das kann man so sehen", "Ich verstehe ..., hmmm... Okay, oh ha"]
reaktionsantworten = {"hallo": "Guten Tag", "geht": "Was verstehst du darunter?", "schlecht": "warum ?",
                      "essen": "Ich habe leider keinen Geschmackssinn :("}

print("Willkommen beim Chatbot: Chatter")
print("Worüber würden Sie gerne heute sprechen?")
print("Zum Beenden einfach 'bye' eintippen")
print("")

nutzereingabe = ""

while nutzereingabe != "bye":
    nutzereingabe = input("Ihre Frage/Antwort: ")
    nutzereingabe = nutzereingabe.lower()
    nutzerwoerter = nutzereingabe.split()
    print(nutzereingabe)

    for einzelwoerter in nutzerwoerter:
        if einzelwoerter in reaktionsantworten:
            print(reaktionsantworten[einzelwoerter])
        else:
            if nutzereingabe != "bye":
                print(random.choice(zufallsantworten))

print("Einen schönen Tag und viel Erfolg, wünsche ich Dir. Bis zum nächsten Mal")
exit(0)
