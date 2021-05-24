# -*- coding: utf-8 -*-

zeichenkette = input("Zeichenkette:")
zeichenkette2 = input("Zeichenkette:")

print("Anzahl der Zahlen: ",     sum(c.isdigit() for c in zeichenkette))
print("Anzahl der Zeichen: ",    sum(c.isalnum() for c in zeichenkette))
print("Anzahl der Buchstaben: ", sum(c.isalpha() for c in zeichenkette))
print("Anzahl der Zeichen: ",    str(zeichenkette2), zeichenkette.find(zeichenkette2))

exit(0)
